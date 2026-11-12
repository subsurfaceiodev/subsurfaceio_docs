"""Sweep CPT footing capacity and settlement over width and embedment."""

import httpx2
import polars as pl
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'

# Load sounding CSV.
sounding = pl.read_csv(
    'https://docs.subsurfaceio.app/assets/CPTU-1.csv',
    skip_rows=9,
    n_rows=280,
    ignore_errors=True,
)

# Convert MPa to kPa.
sounding = sounding.with_columns(
    [
        pl.col('SCPT_FRES') * 1000,
        pl.col('SCPT_PWP') * 1000,
    ]
)

test = dict(
    type='CPT',
    metadata=dict(test_id='CPTU-1'),
    test_metadata=dict(
        water_table_present=True,
        water_table=0.7,
    ),
    data=[
        dict(
            depth=record['SCPT_DPTH'],
            cone_tip_resistance=record['SCPT_RES'],
            sleeve_friction=record['SCPT_FRES'],
            pore_pressure=record['SCPT_PWP'],
        )
        for record in sounding.to_dicts()
    ],
)

analysis = dict(
    x_range=dict(start=1.0, end=4.0, step=0.5),
    y_range=dict(start=0.5, end=2.0, step=0.5),
)

with httpx2.Client(base_url=base_url) as client:
    capacity_response = client.post(
        '/in-situ-test/footing-capacity-parametric/calculate',
        json=dict(test=test, analysis=analysis),
    )
    capacity_response.raise_for_status()
    capacity = capacity_response.json()
    pl.DataFrame(capacity['results']['data']).glimpse()

    capacity_figure = client.post(
        '/in-situ-test/footing-capacity-parametric/figure',
        params=dict(field='ultimate_bearing_capacity'),
        json=capacity,
    )
    capacity_figure.raise_for_status()

    settlement_response = client.post(
        '/in-situ-test/footing-settlements-parametric/calculate',
        json=dict(test=test, analysis=analysis),
    )
    settlement_response.raise_for_status()
    settlement = settlement_response.json()
    pl.DataFrame(settlement['results']['data']).glimpse()

    settlement_figure = client.post(
        '/in-situ-test/footing-settlements-parametric/figure',
        params=dict(field='footing_settlement_sum'),
        json=settlement,
    )
    settlement_figure.raise_for_status()

pio.from_json(capacity_figure.content).show()
pio.from_json(settlement_figure.content).show()
