import requests

base_url = 'https://www.subsurfaceio.app'

data = dict(
    language='en',
    fines_content=34.0,
    percent_sand=64.0,
    percent_gravel=2.0,
    liquid_limit=38.0,
    plasticity_index=12.0,
)

model_response = requests.post(
    f'{base_url}/soil-classification',
    json=dict(
        model=dict(system='USCS') | data
    ),
)

function_sequence_response = requests.post(
    f'{base_url}/function-sequence',
    params=dict(
        function_sequence='SoilClassificationUSCS'
    ),
    json=data,
)

print(model_response.json())
print(function_sequence_response.json())
