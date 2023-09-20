import requests

# делаем запрос GET
status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'},
                   headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())
