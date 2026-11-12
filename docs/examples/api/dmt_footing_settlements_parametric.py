"""Sweep DMT footing settlement over width and embedment."""

import httpx2
import polars as pl
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'

# Load sounding CSV.
sounding = pl.read_csv(
    'https://docs.subsurfaceio.app/assets/DMT-1.csv',
    infer_schema_length=None,
)

test = dict(
    type='DMT',
    metadata=dict(test_id='DMT-1'),
    test_metadata=dict(
        water_table_present=True,
        water_table=1.5,
        free_air_correction_a_reading=15.0,
        free_air_correction_b_reading=40.0,
        vented_control_unit_reading_a=3.0,
        vented_control_unit_reading_b=24.0,
    ),
    data=[
        dict(
            depth=record['Depth (m)'],
            raw_a_reading=record['Raw A reading (kPa)'],
            raw_b_reading=record['Raw B reading (kPa)'],
            raw_c_reading=record['Raw C reading (kPa)'],
        )
        for record in sounding.to_dicts()
    ],
)

analysis = dict(
    x_range=dict(start=1.0, end=4.0, step=0.5),
    y_range=dict(start=0.5, end=2.0, step=0.5),
)

with httpx2.Client(base_url=base_url) as client:
    response = client.post(
        '/in-situ-test/footing-settlements-parametric/calculate',
        json=dict(test=test, analysis=analysis),
    )
    response.raise_for_status()
    calculated = response.json()

    pl.DataFrame(calculated['results']['data']).glimpse()

    figure_response = client.post(
        '/in-situ-test/footing-settlements-parametric/figure',
        params=dict(field='footing_settlement_sum'),
        json=calculated,
    )
    figure_response.raise_for_status()

fig = pio.from_json(figure_response.content)
fig.show()
