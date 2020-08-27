import requests
import json

endpoint_url='http://api.spotify.com/v1/recommendations?'

access_token="BQDdryAM2DGkzjjiUGYpOEXDUa2NNOYpPhtEq62AHOelXoekPlqqMFLcmxFsaU2yCwjS3G1v_MVAU198VNhq7FUvIVcSz7AqobaYfpHM2hQYjnWh4GAlM4fo2IcYxD7O_KZPiKk6IQhP14-MfysKXnglJ8iZ4EHPr9dq5YlbvQM"
uris=[]

#FILTERS
limit = 10 #number of songs
market = "AU" #country
seed_genres = "pop" #genres
target_danceability = 0.2
seed_artists = '47mIJdHORyRerp4os813jD'

#QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}&target_danceability={target_danceability}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

#print(response)
json_response = response.json()
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

endpoint_url=f"https://api.spotify.com/v1/users/derrickjun/playlists"

request_body = json.dumps({
          "name": "Generator", #name of playlist
          "description": "sick beats", #description
          "public": False # let's keep it between us - for now
        })

response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":"Bearer " + access_token})


#adding songs to playlist
playlist_id = response.json()['id']
endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", "Authorization":f"Bearer {access_token}"})
print(response.status_code)
