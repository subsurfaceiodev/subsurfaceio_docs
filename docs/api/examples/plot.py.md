---
title: Plot
---

```py title='plot.py'
import requests
import plotly.io as pio

url = 'https://www.subsurfaceio.app/plot'

data = {
    'plot_model': {
        'plot_type': 'line',
        'x': [0, 1, 2, 3, 4],
        'y': [0, 1, 4, 9, 16],
    }
}

response = requests.post(
    url,
    json=data,
)
fig = pio.from_json(response.content)
fig.show()

```
