---
title: Parameters info
---

```py title='parameters.py'
import requests

url = 'https://www.subsurfaceio.app/parameters'

response = requests.get(
    url,
)

print(response.json())

```
