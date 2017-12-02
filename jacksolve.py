import urllib.request, json
with urllib.request.urlopen("https://s3-eu-west-1.amazonaws.com/yoco-testing/tests.json") as url:
    data = json.loads(url.read().decode())
    print(data)