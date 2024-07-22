import requests


def fetch_airtable_data():
    api_key="patGL9FyDR30dspFy.2af1a7220a2698b0b5d62ac14983a1353bcca22bfe4e60b8a42ff798500c7352"
    id="appXvz23CV0sTzjLC"
    table_name="BC_Gheata"
    url=f'https://api.airtable.com/v0/appXvz23CV0sTzjLC/Plan_LD'
    headers={'Authorization':f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json()


# data = fetch_airtable_data()
# print(data)


def send_data_to_metricool():

    url="metricool_endpoint"
    headers ={
        'Authorization': f'Bearer {url}',
        'Content-Type':'applicatiom/json'
    }

    response = requests.get(url, headers=headers)
    return response.json()

airtable_data = fetch_airtable_data()

if 'records' in airtable_data:
    metricool_Data = {'data':airtable_data['records']}

result = send_data_to_metricool(metricool_Data)