"""Classify a soil from index properties."""

import httpx2

base_url = 'https://www.subsurfaceio.app'

# Inputs shared by both call styles.
data = dict(
    language='en',
    fines_content=34.0,
    percent_sand=64.0,
    percent_gravel=2.0,
    liquid_limit=38.0,
    plasticity_index=12.0,
)

with httpx2.Client(base_url=base_url) as client:
    # Dedicated model endpoint: wrap inputs in `model`.
    model_response = client.post(
        '/soil-classification/calculate',
        json=dict(model=dict(system='USCS') | data),
    )
    model_response.raise_for_status()

    # Generic pipeline endpoint: send the same inputs flat.
    function_sequence_response = client.post(
        '/function-sequence',
        params=dict(function_sequence='SoilClassificationUSCS'),
        json=data,
    )
    function_sequence_response.raise_for_status()

print(model_response.json()['results'])
print(function_sequence_response.json())
