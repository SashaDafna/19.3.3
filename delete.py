import requests

# делаем запрос DELETE
res = requests.delete(f"https://petstore.swagger.io/v2/pet/111", headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())
