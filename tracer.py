#!/usr/bin/env python3   
import urllib.parse, requests, json
from oauthlib.oauth2 import WebApplicationClient

print('Authorization starts..   ')
dest = 'https://public-api.wordpress.com/oauth2/authorize?client_id=78848&redirect_uri=https://wayofphoenix.wordpress.com&response_type=token&blog=wayofphoenix'
params = {}
params['client_id'] = 78848
params['redirect_uri'] = 'https://wayofphoenix.wordpress.com'
params['response_type'] = 'token'
params['blog'] = 'wayofphoenix'

param_string = urllib.parse.urlencode(params).replace('%3A', ':').replace('%2F', '/')
auth_string = 'https://public-api.wordpress.com/oauth2/authorize'
res = auth_string + '?' + param_string
if res != dest:
    print('Error')
else: 
    print("Authorize url: {}".format(res))
request1 = requests.get(dest)
print("Authorize request status_code: {}".format(request1.status_code))
print('Auhorize request history: {}'.format(request1.history))
for h in request1.history: 
    print('History status_code: {}. History url: {}'.format(h.status_code, h.url))

res1 = 'https://wayofphoenix.wordpress.com/#access_token=voBjmz1mN8iBkq%5E9dOG0o*BOTnXyr(5%26$z4*Wq7ahPO9bLZl*f(DF7xuAovzdJpH&expires_in=1209600&token_type=bearer&site_id=115426326&scope='
print('Trying to post message..')
site_id = '115426326'
url4post = 'https://public-api.wordpress.com/rest/v1/sites/' + site_id + '/posts/new'
payload = {'content': 'super test!'}
access_token = 'voBjmz1mN8iBkq%5E9dOG0o*BOTnXyr(5%26$z4*Wq7ahPO9bLZl*f(DF7xuAovzdJpH'
headers = {'authorization': 'Bearer ' + access_token}

r = requests.post(url4post, data=json.dumps(payload), headers=headers)
#print(r.text)
print('Post request status_code: {}'.format(r.status_code))
print('Post request text: {}'.format(r.text))