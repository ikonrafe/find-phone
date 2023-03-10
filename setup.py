import requests

api_key = 'AIzaSyAuUqm6atdaFjkBmo3k9pge86qH31am1FU'

phone_number = '6281236022306'

def locate_phone(api_key, phone_number):

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}'

    headers = {'content-type': 'application/json'}

    data = {

        'considerIp': 'false',

        'wifiAccessPoints': [],

        'cellTowers': [{

            'cellId': 35148066,

            'locationAreaCode': 36,

            'mobileCountryCode': 510,

            'mobileNetworkCode': 10

        }]

    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:

        location = response.json()['location']

        accuracy = response.json()['accuracy']

        print(f'Phone {phone_number} is at ({location["lat"]}, {location["lng"]}), accuracy: {accuracy} meters')

    else:

        print('Unable to locate phone')

# contoh penggunaan

locate_phone(api_key, phone_number)



