"""Interpret a DMT sounding."""

import httpx2
import polars as pl
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'

# Load sounding CSV.
sounding = pl.read_csv('https://docs.subsurfaceio.app/assets/DMT-1_data.csv')
columns = sounding.to_dict(as_series=False)

# Remap columns to API field names.
inputs = dict(
    water_table_present=True,
    water_table=1.5,
    elasticity_to_constrained_modulus_ratio=0.8,
    depth=columns['Depth (m)'],
    corrected_pressure_p0=columns['P0 (kPa)'],
    corrected_pressure_p1=columns['P1 (kPa)'],
    corrected_pressure_p2=columns['P2 (kPa)'],
)

with httpx2.Client(base_url=base_url) as client:
    # Run interpretation. results_format='ndim' returns 0d / 1d groups instead.
    response = client.post(
        '/function-sequence',
        params=dict(
            function_sequence='DMTInterpretationMarchetti',
            output='all',
            results_format='records',
        ),
        json=inputs,
    )
    response.raise_for_status()
    rows = response.json()['data']
    for row in rows:
        row['test_id'] = 'DMT-1'

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
                    'corrected_pressure_p0',
                    'corrected_pressure_p1',
                    'corrected_pressure_p2',
                    'material_index',
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
