"""Write a site investigation to Excel and KML."""

import httpx2

base_url = 'https://www.subsurfaceio.app'

site = dict(
    project_metadata=dict(project_id='Treasure Island'),
    in_situ_tests=[
        dict(
            type='CPT',
            metadata=dict(
                test_id='CPTU-1',
                latitude=37.824806,
                longitude=-122.374042,
            ),
            data=[
                dict(
                    depth=1.2,
                    cone_tip_resistance=16.9,
                    sleeve_friction=130.5,
                    pore_pressure=None,
                ),
            ],
        ),
    ],
)

with httpx2.Client(base_url=base_url) as client:
    # Download a workbook of the site.
    excel_response = client.post(
        '/site-investigation/write-excel',
        json=site,
    )
    excel_response.raise_for_status()
    with open('site_investigation.xlsx', 'wb') as workbook:
        workbook.write(excel_response.content)

    # Download a map of the test locations.
    kml_response = client.post(
        '/site-investigation/write-kml-map',
        json=site,
    )
    kml_response.raise_for_status()
    with open('site_investigation.kml', 'wb') as kml_file:
        kml_file.write(kml_response.content)

print('site_investigation.xlsx')
print('site_investigation.kml')
