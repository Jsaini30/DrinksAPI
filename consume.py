from urllib import response
from webbrowser import get
import requests

response = requests.post("http://127.0.0.1:8000/drinks", data ={"name": "test" ,"description": "sweet as hell" })
print(response.json())
response = requests.get("http://127.0.0.1:8000/drinks/3")
print(response.json())