import requests

url = 'https://www.subsurfaceio.app/parameter_registry'

response = requests.get(
    url,
)

print(response.json())
