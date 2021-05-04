import requests
import datetime
state_map={}
x = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/states')
print('Choose a State from the below list:')
for state in x.json()['states']:
    state_map[state['state_name']]=state['state_id']
    print(state['state_name'])

st=state_map[input('Select a State:')]

x = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/'+str(st))
for district in x.json()['districts']:
    print(district['district_name'],district['district_id'])