import httpx2
import polars as pl
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'


def get_cpt_test():
    data_frame = pl.read_csv(
        'https://docs.subsurfaceio.app/assets/CPTU-1.csv',
        skip_rows=9,
        n_rows=280,
        ignore_errors=True
    )

    # MPa to kPa
    data_frame = data_frame.with_columns(
        [
            pl.col('SCPT_FRES') * 1000,
            pl.col('SCPT_PWP') * 1000,
        ]
    )

    data_records = data_frame.to_dicts()

    cpt_test = dict(
        type='CPT',
        metadata=dict(
            test_id='CPTU-1'
        ),
        data=[dict(
            depth=record['SCPT_DPTH'],
            cone_tip_resistance=record['SCPT_RES'],
            sleeve_friction=record['SCPT_FRES'],
            pore_pressure=record['SCPT_PWP'],
        ) for record in data_records]
    )
    return cpt_test


def get_dmt_test():
    data_frame = pl.read_csv(
        'https://docs.subsurfaceio.app/assets/DMT-1.csv',
        infer_schema_length=None
    )

    data_records = data_frame.to_dicts()

    dmt_test = dict(
        type='DMT',
        metadata=dict(
            test_id='DMT-1'
        ),
        data=[dict(
            depth=record['Depth (m)'],
            raw_a_reading=record['A (kPa)'],
            raw_b_reading=record['B (kPa)'],
            raw_c_reading=record['C (kPa)'],
        ) for record in data_records]
    )
    return dmt_test


def get_ist_test():
    data_frame = pl.read_csv(
        'https://docs.subsurfaceio.app/assets/Gibbs%20B-1%20vs.csv',
        skip_rows=9,
        n_rows=9,
        ignore_errors=True
    )

    data_records = data_frame.to_dicts()

    ist_test = dict(
        type='IST',
        metadata=dict(
            test_id='Gibbs B-1 vs'
        ),
        data=[dict(
            depth=record['GIND_DPTH'],
            shear_velocity=record['GIND_VS'],
            compressional_velocity=record['GIND_VP'],
        ) for record in data_records]
    )

    return ist_test


def get_site_investigation_payload():
    site_payload = dict(
        project_metadata=dict(project_id='Treasure Island'),
        in_situ_tests=[
            get_cpt_test(),
            get_dmt_test(),
            get_ist_test()
        ]

    )
    return site_payload


with httpx2.Client(base_url=base_url) as client:
    interpretation_response = client.post(
        '/site-investigation/calculate-interpretation',
        json=get_site_investigation_payload()
    )
    site = interpretation_response.json()

    liquefaction_response = client.post(
        '/site-investigation/calculate-liquefaction',
        json=site
    )

    site = liquefaction_response.json()

    cpt_interpretation_data = site['in_situ_tests'][0]['interpretation']['data']
    cpt_interpretation_df = pl.from_records(
        cpt_interpretation_data,
        infer_schema_length=None
    )
    cpt_interpretation_df.glimpse()

    cpt_liquefaction_data = site['in_situ_tests'][0]['liquefaction']['data']
    cpt_liquefaction_df = pl.from_records(
        cpt_liquefaction_data,
        infer_schema_length=None
    )
    cpt_liquefaction_df.glimpse()

    dmt_interpretation_data = site['in_situ_tests'][1]['interpretation']['data']
    dmt_interpretation_df = pl.from_records(
        dmt_interpretation_data,
        infer_schema_length=None
    )
    dmt_interpretation_df.glimpse()

    dmt_liquefaction_data = site['in_situ_tests'][1]['liquefaction']['data']
    dmt_liquefaction_df = pl.from_records(
        dmt_liquefaction_data,
        infer_schema_length=None
    )
    dmt_liquefaction_df.glimpse()

    plot_response1 = client.post(
        '/site-investigation/plot',
        json=site,
        params=dict(
            x=[
                'cone_tip_resistance',
                'sleeve_friction',
                'pore_pressure',
                'soil_behavior_type_index',
                'modified_soil_behavior_type_index',
            ],
            y='depth'
        )
    )

    plot_response2 = client.post(
        '/site-investigation/plot',
        json=site,
        params=dict(
            x=[
                'corrected_pressure_p0',
                'corrected_pressure_p1',
                'corrected_pressure_p2',
                'material_index',
            ],
            y='depth'
        )
    )

    plot_response3 = client.post(
        '/site-investigation/plot',
        json=site,
        params=dict(
            x=[
                'unit_weight',
                'undrained_shear_strength',
                'overconsolidation_ratio',
                'friction_angle',
                'constrained_modulus',
                'shear_velocity',
                'soil_behavior_type_index',
                'material_index',
            ],
            y='depth'
        )
    )

    plot_response4 = client.post(
        '/site-investigation/plot',
        json=site,
        params=dict(
            x=[
                'liquefaction_safety_factor',
                'liquefaction_probability',
                'liquefaction_potential_index',
                'liquefaction_severity_number',
                'lateral_displacement_index',
                'liquefaction_settlement',
            ],
            y='depth'
        )
    )

    fig1 = pio.from_json(plot_response1.content)
    fig2 = pio.from_json(plot_response2.content)
    fig3 = pio.from_json(plot_response3.content)
    fig4 = pio.from_json(plot_response4.content)

    fig1.show()
    fig2.show()
    fig3.show()
    fig4.show()
