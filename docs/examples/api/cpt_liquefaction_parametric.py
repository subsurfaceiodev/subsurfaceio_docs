"""Build a liquefaction surface over PGA and magnitude."""

import httpx2
import numpy as np
import polars as pl
import plotly.graph_objects as go

base_url = 'https://www.subsurfaceio.app'

# Load sounding CSV.
sounding = pl.read_csv(
    'https://docs.subsurfaceio.app/assets/CPTU-1.csv',
    skip_rows=9,
    n_rows=281,
    ignore_errors=True,
)

# Convert MPa to kPa.
sounding = sounding.with_columns(
    [
        pl.col('SCPT_FRES') * 1000,
        pl.col('SCPT_PWP') * 1000,
    ]
)
columns = sounding.to_dict(as_series=False)

# Remap columns to API field names.
inputs = dict(
    cone_area_ratio=0.8,
    water_table_present=True,
    water_table=0.7,
    remove_loose_sand_criteria=True,
    relative_density_constant=350,
    sensitivity_constant=7,
    constant_volume_friction_angle=32,
    is_fine_soil_criteria='sbtn',
    liquefaction_max_depth=20,
    liquefaction_severity_number_max_depth=20,
    lateral_displacement_min_thickness=0,
    site_ground_condition='level_ground',
    liquefaction_potential_index_method='iwasaki1978',
    stone_column_arrangement=None,
    depth=columns['SCPT_DPTH'],
    cone_tip_resistance=columns['SCPT_RES'],
    sleeve_friction=columns['SCPT_FRES'],
    pore_pressure=columns['SCPT_PWP'],
)

# Build the PGA × magnitude grid.
pga = np.arange(0.1, 0.5, 0.05)
magnitude = np.arange(6, 8, 0.25)
pga_grid, magnitude_grid = np.meshgrid(pga, magnitude)
surface = np.full_like(pga_grid, np.nan, dtype=float)

x_label = 'peak_ground_acceleration'
y_label = 'moment_magnitude'
z_label = 'liquefaction_potential_index_sum'

with httpx2.Client(base_url=base_url) as client:
    # One vectorized call: pass the full grid as columns.
    response = client.post(
        '/function-sequence',
        params=dict(
            function_sequence='CPTLiquefactionRobertson',
            output='all',
        ),
        json=inputs | dict(
            peak_ground_acceleration=np.vstack(np.ravel(pga_grid)).tolist(),
            moment_magnitude=np.vstack(np.ravel(magnitude_grid)).tolist(),
        ),
    )
    response.raise_for_status()
    surface[:] = np.reshape(response.json()['1d'][z_label], pga_grid.shape)

fig = go.Figure(data=[go.Surface(x=pga_grid, y=magnitude_grid, z=surface)])
fig.update_layout(
    scene=dict(
        xaxis_title=x_label,
        yaxis_title=y_label,
        zaxis_title=z_label,
    )
)
fig.show()
