"""Plot a simple line."""

import httpx2
import plotly.io as pio

base_url = 'https://www.subsurfaceio.app'

data = dict(
    plot_model=dict(
        plot_type='line',
        x=[0, 1, 2, 3, 4],
        y=[0, 1, 4, 9, 16],
    ),
)

with httpx2.Client(base_url=base_url) as client:
    response = client.post('/geotech-plot', json=data)
    response.raise_for_status()

fig = pio.from_json(response.content)
fig.show()
