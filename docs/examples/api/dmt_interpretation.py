"""Interpret a DMT sounding."""

import httpx2
import polars as pl
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'

# Load sounding CSV.
sounding = pl.read_csv(
    'https://docs.subsurfaceio.app/assets/DMT-1.csv',
    infer_schema_length=None
)
columns = sounding.to_dict(as_series=False)

# Remap columns to API field names.
inputs = dict(
    water_table_present=True,
    water_table=1.5,
    free_air_correction_a_reading=15.0,
    free_air_correction_b_reading=40.0,
    vented_control_unit_reading_a=3.0,
    vented_control_unit_reading_b=24.0,
    elasticity_to_constrained_modulus_ratio=0.8,
    depth=columns['Depth (m)'],
    raw_a_reading=columns['Raw A reading (kPa)'],
    raw_b_reading=columns['Raw B reading (kPa)'],
    raw_c_reading=columns['Raw C reading (kPa)'],
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
