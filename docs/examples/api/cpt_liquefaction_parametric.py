"""Sweep liquefaction over PGA and magnitude for one CPT."""

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
    liquefaction_settings=dict(
        peak_ground_acceleration=0.14,
        moment_magnitude=6.9,
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
    x_range=dict(start=0.1, end=0.5, step=0.05),
    y_range=dict(start=6, end=8, step=0.25),
)

with httpx2.Client(base_url=base_url) as client:
    response = client.post(
        '/in-situ-test/liquefaction-parametric/calculate',
        json=dict(test=test, analysis=analysis),
    )
    response.raise_for_status()
    calculated = response.json()

    pl.DataFrame(calculated['results']['data']).glimpse()

    figure_response = client.post(
        '/in-situ-test/liquefaction-parametric/figure',
        params=dict(field='liquefaction_potential_index_sum'),
        json=calculated,
    )
    figure_response.raise_for_status()

fig = pio.from_json(figure_response.content)
fig.show()
