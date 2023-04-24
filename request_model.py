import requests

'''

r = requests.get('https://www.w3schools.com/python/module_requests.asp')

print(r.text)



f = open('index.html','w')
f.write(r.text)
'''

'''
payload = {'adity': 'value1', 'key2': 'value2'}

r = requests.post('https://httpbin.org/post?adity==b', data=payload)
print(r.text)
'''
'''
url = 'https://assets.mixkit.co/active_storage/sfx/1489/1489.wav'

r = requests.get(url)

fp = open('mp3.wav','wb')
fp.write(r.content)
fp.close()
'''

url = 'https://download.pexels.com/vimeo/357646800/pexels-joseph-redfield-2889410.mp4?'

r = requests.get(url)

fp = open('video.mp4','wb')
fp.write(r.content)
fp.close()