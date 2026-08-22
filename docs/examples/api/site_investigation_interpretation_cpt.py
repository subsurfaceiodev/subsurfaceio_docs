import httpx2
import polars as pl
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'


def get_site_investigation_payload():
    basic_data = pl.read_csv(
        'https://docs.subsurfaceio.app/assets/CPTU-1.csv',
        skip_rows=9,
        n_rows=280,
        ignore_errors=True
    )

    # MPa to kPa
    basic_data = basic_data.with_columns(
        [
            pl.col('SCPT_FRES') * 1000,
            pl.col('SCPT_PWP') * 1000,
        ]
    )

    basic_data = basic_data.to_dicts()

    cpt_test = dict(
        type='CPT',
        metadata=dict(
            test_id='CPTU-1'
        ),
        data=[dict(
            depth=data['SCPT_DPTH'],
            cone_tip_resistance=data['SCPT_RES'],
            sleeve_friction=data['SCPT_FRES'],
            pore_pressure=data['SCPT_PWP'],
        ) for data in basic_data]
    )

    site_investigation = dict(
        project_metadata=dict(project_id='Treasure Island'),
        in_situ_tests=[cpt_test]

    )
    return site_investigation


with httpx2.Client(base_url=base_url) as client:
    calculation_response = client.post(
        '/site-investigation/calculate-interpretation',
        json=get_site_investigation_payload()
    )
    calculated_site = calculation_response.json()
    interpretation_data = calculated_site['in_situ_tests'][0]['interpretation']['data']
    df = pl.from_records(interpretation_data)
    print(df.glimpse())

    plot_response = client.post(
        '/site-investigation/plot',
        json=calculated_site,
        params=dict(
            x=['cone_tip_resistance', 'sleeve_friction', 'pore_pressure', 'soil_behavior_type_index',
               'modified_soil_behavior_type_index'],
            y='depth'
        )
    )

    fig = pio.from_json(plot_response.content)
    fig.show()
