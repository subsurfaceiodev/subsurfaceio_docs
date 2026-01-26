---
title: Calculate
---

```py title='soil_classification.py'
import requests

url = 'https://www.subsurfaceio.app/function-sequence'

params = dict(
    function_sequence='SoilClassificationUSCS'
)

data = dict(
    fines_content=34,
    percent_sand=64,
    percent_gravel=2,
    liquid_limit=38,
    plasticity_index=12,
)

response = requests.post(
    url,
    params=params,
    json=data,
)

print(response.json())

```
