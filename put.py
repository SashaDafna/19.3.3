import requests

# делаем запрос PUT
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 1424, "category": {"id": 0, "name": "string"},
        "name": "Perreito_Salvaje", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
res = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print(res.status_code)
print(res.json())
