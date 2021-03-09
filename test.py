import requests
import json

BASE = "http://127.0.0.1:5000/"

data = [{"likes":1000, "views":250000, "name":"Tim"},
        {"likes":10, "views":9000000, "name":"How"},
        {"likes":1700, "views":1200, "name":"Bad-Boy"}
    ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/1")
print(response.json())