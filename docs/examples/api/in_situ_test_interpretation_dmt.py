import requests
import polars as pl
import plotly.io as pio


def get_results():
    params = dict(
        function_sequence='DMTInterpretationMarchetti',
        output='all',
    )

    data = dict(
        water_table_present=True,
        water_table=1.5,
        elasticity_to_constrained_modulus_ratio=0.8,
        depth=basic_data['Depth (m)'],
        corrected_pressure_p0=basic_data['P0 (kPa)'],
        corrected_pressure_p1=basic_data['P1 (kPa)'],
        corrected_pressure_p2=basic_data['P2 (kPa)'],
    )

    response = requests.post(
        f'{base_url}/function-sequence',
        params=params,
        json=data,
    )
    return response


def plot_results(data):
    data['test_id'] = 'DMT-1'

    form_data = dict(
        reverse_y=True,
        sharex=False,
        plot_model=dict(
            plot_type='line',
            data_frame=data,
            x=['corrected_pressure_p0', 'corrected_pressure_p1', 'corrected_pressure_p2', 'material_index'],
            y='depth',
            facet_col='variable',
            color='test_id',
            color_discrete_sequence=['black']
        )
    )

    response = requests.post(
        f'{base_url}/geotech-plot',
        json=form_data
    )
    return response


base_url = 'https://www.subsurfaceio.app'

basic_data = pl.read_csv(
    'https://docs.subsurfaceio.app/assets/DMT-1_data.csv',
)

basic_data = basic_data.to_dict(as_series=False)

results_json = get_results().json()['1d']
df = pl.DataFrame(results_json)
df.glimpse()

fig = pio.from_json(plot_results(results_json).content)
fig.show()
