import requests

url = "http://127.0.0.1:5000/chat"
msg = input("Pergunte algo para o chatbot: ")

response = requests.post(url, json={"message": msg})
print("Resposta:", response.json()["response"])
