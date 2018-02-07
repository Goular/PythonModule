import requests

files = {
    'file': open('favicon.ico', 'rb')
}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)
