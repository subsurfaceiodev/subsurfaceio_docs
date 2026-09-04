"""Interpret and plot a multi-test site investigation."""

import httpx2
import polars as pl
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'


def get_cpt_test():
    # Load sounding CSV.
    data_frame = pl.read_csv(
        'https://docs.subsurfaceio.app/assets/CPTU-1.csv',
        skip_rows=9,
        n_rows=281,
        ignore_errors=True,
    )

    # Convert MPa to kPa.
    data_frame = data_frame.with_columns(
        [
            pl.col('SCPT_FRES') * 1000,
            pl.col('SCPT_PWP') * 1000,
        ]
    )

    # Remap columns to API field names.
    return dict(
        type='CPT',
        metadata=dict(test_id='CPTU-1'),
        data=[
            dict(
                depth=record['SCPT_DPTH'],
                cone_tip_resistance=record['SCPT_RES'],
                sleeve_friction=record['SCPT_FRES'],
                pore_pressure=record['SCPT_PWP'],
            )
            for record in data_frame.to_dicts()
        ],
    )


def get_dmt_test():
    # Load sounding CSV.
    data_frame = pl.read_csv('https://docs.subsurfaceio.app/assets/DMT-1.csv')

    # Remap columns to API field names.
    return dict(
        type='DMT',
        metadata=dict(test_id='DMT-1'),
        data=[
            dict(
                depth=record['Depth (m)'],
                raw_a_reading=record['A (kPa)'],
                raw_b_reading=record['B (kPa)'],
                raw_c_reading=record['C (kPa)'],
            )
            for record in data_frame.to_dicts()
        ],
    )


def get_ist_test():
    # Load sounding CSV.
    data_frame = pl.read_csv(
        'https://docs.subsurfaceio.app/assets/Gibbs%20B-1%20vs.csv',
        skip_rows=9,
        n_rows=16,
        ignore_errors=True,
    )

    # Remap columns to API field names.
    return dict(
        type='IST',
        metadata=dict(test_id='Gibbs B-1 vs'),
        data=[
            dict(
                depth=record['GIND_DPTH'],
                shear_velocity=record['GIND_VS'],
                compressional_velocity=record['GIND_VP'],
            )
            for record in data_frame.to_dicts()
        ],
    )


site_payload = dict(
    project_metadata=dict(project_id='Treasure Island'),
    in_situ_tests=[
        get_cpt_test(),
        get_dmt_test(),
        get_ist_test(),
    ],
)

with httpx2.Client(base_url=base_url) as client:
    # Fill missing borehole unit weights from blow counts, when present.
    correlate_response = client.post(
        '/site-investigation/correlate-null-unit-weight',
        json=site_payload,
    )
    correlate_response.raise_for_status()
    site = correlate_response.json()

    # Run interpretation, then liquefaction, on the assembled site.
    interpretation_response = client.post(
        '/site-investigation/calculate-interpretation',
        json=site,
    )
    interpretation_response.raise_for_status()
    site = interpretation_response.json()

    liquefaction_response = client.post(
        '/site-investigation/calculate-liquefaction',
        json=site,
    )
    liquefaction_response.raise_for_status()
    site = liquefaction_response.json()

    cpt = site['in_situ_tests'][0]
    pl.from_records(cpt['interpretation']['data'], infer_schema_length=None).glimpse()
    pl.from_records(cpt['liquefaction']['data'], infer_schema_length=None).glimpse()

    # Plot raw measurements, combined interpretation, and liquefaction.
    plot_specs = [
        [
            'cone_tip_resistance',
            'sleeve_friction',
            'pore_pressure',
            'soil_behavior_type_index',
            'modified_soil_behavior_type_index',
        ],
        [
            'unit_weight',
            'undrained_shear_strength',
            'overconsolidation_ratio',
            'friction_angle',
            'constrained_modulus',
            'shear_velocity',
            'soil_behavior_type_index',
            'material_index',
        ],
        [
            'liquefaction_safety_factor',
            'liquefaction_probability',
            'liquefaction_potential_index',
            'liquefaction_severity_number',
            'lateral_displacement_index',
            'liquefaction_settlement',
        ],
    ]
    for x_fields in plot_specs:
        plot_response = client.post(
            '/site-investigation/plot',
            json=site,
            params=dict(x=x_fields, y='depth'),
        )
        plot_response.raise_for_status()
        pio.from_json(plot_response.content).show()
