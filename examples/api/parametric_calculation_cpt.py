import requests
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def get_results(**kwargs):
    params = dict(
        function_sequence='CPTLiquefactionRobertson',
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
        is_fine_soil_criteria='ic_cutoff',
        liquefaction_max_depth=20,
        liquefaction_severity_number_max_depth=20,
        lateral_displacement_min_thickness=0,
        site_ground_condition='level_ground',
        liquefaction_potential_index_method='iwasaki1978',
        depth=basic_data['SCPT_DPTH'],
        cone_tip_resistance=basic_data['SCPT_RES'],
        sleeve_friction=basic_data['SCPT_FRES'],
        pore_pressure=basic_data['SCPT_PWP'],
    ) | kwargs

    response = requests.post(
        f'{base_url}/function-sequence',
        params=params,
        json=data,
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

x = np.arange(0.1, 0.5, 0.05)
y = np.arange(6, 8, 0.25)
z = []

X, Y = np.meshgrid(x, y)
Z = np.full_like(X, np.nan, dtype=float)

x_label = 'peak_ground_acceleration'
y_label = 'moment_magnitude'
z_label = 'liquefaction_potential_index_sum'

res = get_results(
    peak_ground_acceleration=np.vstack(np.ravel(X)).tolist(),
    moment_magnitude=np.vstack(np.ravel(Y)).tolist(),
).json()['1d'][z_label]
Z[:] = np.reshape(res, X.shape)

fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])

fig.update_layout(
    scene=dict(
        xaxis_title=x_label,
        yaxis_title=y_label,
        zaxis_title=z_label
    )
)

fig.show()
