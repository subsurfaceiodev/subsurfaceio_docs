"""Build a liquefaction surface over PGA and magnitude."""

import httpx2
import numpy as np
import polars as pl
import plotly.graph_objects as go

base_url = 'https://www.subsurfaceio.app'

# Load sounding CSV.
sounding = pl.read_csv('https://docs.subsurfaceio.app/assets/DMT-1_data.csv')
columns = sounding.to_dict(as_series=False)

# Remap columns to API field names.
inputs = dict(
    water_table_present=True,
    water_table=1.5,
    elasticity_to_constrained_modulus_ratio=0.8,
    stone_column_arrangement=None,
    depth=columns['Depth (m)'],
    corrected_pressure_p0=columns['P0 (kPa)'],
    corrected_pressure_p1=columns['P1 (kPa)'],
    corrected_pressure_p2=columns['P2 (kPa)'],
    liquefaction_max_depth=20,
    liquefaction_severity_number_max_depth=20,
    lateral_displacement_min_thickness=0,
    site_ground_condition='level_ground',
    liquefaction_potential_index_method='iwasaki1978',
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
            function_sequence='DMTLiquefactionMarchetti',
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
