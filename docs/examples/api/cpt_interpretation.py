"""Interpret a CPT sounding."""

import httpx2
import polars as pl
import plotly.io as pio

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
    depth=columns['SCPT_DPTH'],
    cone_tip_resistance=columns['SCPT_RES'],
    sleeve_friction=columns['SCPT_FRES'],
    pore_pressure=columns['SCPT_PWP'],
)

with httpx2.Client(base_url=base_url) as client:
    # Run interpretation. results_format='ndim' returns 0d / 1d groups instead.
    response = client.post(
        '/function-sequence',
        params=dict(
            function_sequence='CPTInterpretationRobertson',
            output='all',
            results_format='records',
        ),
        json=inputs,
    )
    response.raise_for_status()
    rows = response.json()['data']
    for row in rows:
        row['test_id'] = 'CPTU-1'

    pl.DataFrame(rows, infer_schema_length=None).glimpse()

    # Plot selected columns vs depth.
    plot_response = client.post(
        '/geotech-plot',
        json=dict(
            reverse_y=True,
            sharex=False,
            plot_model=dict(
                plot_type='line',
                data_frame=rows,
                x=[
                    'cone_tip_resistance',
                    'sleeve_friction',
                    'pore_pressure',
                    'soil_behavior_type_index',
                    'modified_soil_behavior_type_index',
                ],
                y='depth',
                facet_col='variable',
                color='test_id',
                color_discrete_sequence=['black'],
            ),
        ),
    )
    plot_response.raise_for_status()

fig = pio.from_json(plot_response.content)
fig.show()
