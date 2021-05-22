import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '91**********',
  'message': 'hey' ,
  'key': 'textbelt',
})
print(resp.json())
