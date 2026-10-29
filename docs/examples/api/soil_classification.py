"""Classify a soil from index properties."""

import httpx2

base_url = 'https://www.subsurfaceio.app'

# Inputs shared by both single-specimen call styles.
data = dict(
    language='en',
    fines_content=34.0,
    percent_sand=64.0,
    percent_gravel=2.0,
    liquid_limit=38.0,
    plasticity_index=12.0,
)

# Two specimens. language broadcasts; the other fields are one value per row.
# The same body with function_sequence=SoilClassificationAASHTO is the AASHTO
# batch. USDA uses percent_sand and percent_clay.
batch = dict(
    language='en',
    fines_content=[34.0, 58.0],
    percent_sand=[64.0, 42.0],
    percent_gravel=[2.0, 0.0],
    liquid_limit=[38.0, 49.0],
    plasticity_index=[12.0, 21.0],
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

    # Many specimens: results_format=records returns one object per row.
    batch_response = client.post(
        '/function-sequence',
        params=dict(
            function_sequence='SoilClassificationUSCS',
            results_format='records',
        ),
        json=batch,
    )
    batch_response.raise_for_status()

print(model_response.json()['results'])
print(function_sequence_response.json())
print(batch_response.json()['data'])
