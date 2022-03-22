import http.client

conn = http.client.HTTPSConnection("google-finance4.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "shindonghyun",
    'x-rapidapi-host': "google-finance4.p.rapidapi.com"
    }

conn.request("GET", "/market-trends/?t=indexes&hl=en&gl=US", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))