import requests

def f(url):
	headers = {'Accept': 'application/json'}
	r = requests.get(url, headers=headers)
	rjson = r.json()
	return rjson

def process_url(url):
	rjson = f(url)
	if rjson["message"] == "This is not the end":
		print(f"new url: {rjson['follow']}")
		process_url(rjson["follow"])
	else:
		print(rjson)

# Start the process
url = "https://letsrevolutionizetesting.com/challenge"
process_url(url)
