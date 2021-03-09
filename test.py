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
for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i))
    print(response.json())

input()
response = requests.patch(BASE + "video/2",{'views':99, 'likes':1785648})
print(response.json())
