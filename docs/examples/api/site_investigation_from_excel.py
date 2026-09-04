"""Load a site investigation from a local workbook."""

import httpx2

base_url = 'https://www.subsurfaceio.app'

# Local workbooks. Replace these paths before running.
excel_path = 'path/to/your.xlsx'
cpetit_path = 'path/to/your-cpetit.xlsx'

with httpx2.Client(base_url=base_url) as client:
    # Native workbook: multipart field `source`, project id in the query.
    with open(excel_path, 'rb') as workbook:
        excel_response = client.post(
            '/site-investigation/from-excel',
            params=dict(project_id='My Project'),
            files=dict(source=workbook),
        )
    excel_response.raise_for_status()
    print(excel_response.json()['project_metadata'])

    # CPeT-IT export: same field, plus how the file was exported.
    with open(cpetit_path, 'rb') as workbook:
        cpetit_response = client.post(
            '/site-investigation/from-cpetit-excel',
            params=dict(exported_as='custom'),
            files=dict(source=workbook),
        )
    cpetit_response.raise_for_status()
    print(cpetit_response.json()['project_metadata'])
