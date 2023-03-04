import requests

def locate_phone(AIzaSyB8EqyDTxOQ3aLGmkZ-zn27bGk3YNQq5kM , 0896-5302-8380):
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={AIzaSyB8EqyDTxOQ3aLGmkZ-zn27bGk3YNQq5kM}'
    headers = {'content-type': 'application/json'}
    data = {'considerIp': 'false',
            'wifiAccessPoints': [],
            'cellTowers': [{'cellId': 42, 'locationAreaCode': 021, 'mobileCountryCode': 510, 'mobileNetworkCode': 11}]}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        location = response.json()['location']
        accuracy = response.json()['accuracy']
        print(f'Phone {phone_number} is at ({location["lat"]}, {location["lng"]}), accuracy: {accuracy} meters')
    else:
        print('Unable to locate phone')

# contoh penggunaan
api_key = 'YOUR_API_KEY'
phone_number = '555-1234'
locate_phone(api_key, phone_number)
