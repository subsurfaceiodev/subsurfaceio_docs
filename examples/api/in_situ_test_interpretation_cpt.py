import requests
import numpy as np
import pandas as pd
import plotly.io as pio


def get_results():
    params = dict(
        function_sequence='CPTInterpretationRobertson',
        combine_inputs_results=True,
    )

    data = dict(
        cone_area_ratio=0.8,
        water_table_present=True,
        water_table=0.7,
        remove_loose_sand_criteria=True,
        relative_density_constant=350,
        sensitivity_constant=7,
        constant_volume_friction_angle=32,
        is_fine_soil_criteria='sbtn',
        depth=basic_data['SCPT_DPTH'],
        cone_tip_resistance=basic_data['SCPT_RES'],
        sleeve_friction=basic_data['SCPT_FRES'],
        pore_pressure=basic_data['SCPT_PWP'],
    )

    response = requests.post(
        f'{base_url}/function-sequence',
        params=params,
        json=data,
    )
    return response


def plot_results(data):
    data['test_id'] = 'CPTU-1'

    form_data = dict(
        reverse_y=True,
        sharex=False,
        plot_model=dict(
            plot_type='line',
            data_frame=data,
            x=['cone_tip_resistance', 'sleeve_friction', 'pore_pressure', 'soil_behavior_type_index',
               'modified_soil_behavior_type_index'],
            y='depth',
            facet_col='variable',
            color='test_id',
            color_discrete_sequence=['black']
        )
    )

    response = requests.post(
        f'{base_url}/plot',
        json=form_data,
    )
    return response


base_url = 'https://www.subsurfaceio.app'

basic_data = pd.read_csv(
    f'{base_url}/dash/assets/CPTU-1.csv',
    skiprows=9,
    nrows=280
)

# MPa to kPa
basic_data['SCPT_FRES'] *= 1000
basic_data['SCPT_PWP'] *= 1000

basic_data = basic_data.replace({np.nan: None})
basic_data = basic_data.to_dict('list')

results_json = get_results().json()['1d']
df = pd.DataFrame(results_json)
print(df.to_string())

fig = pio.from_json(plot_results(results_json).content)
fig.show()
