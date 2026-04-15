ipmopt requests

API_KEY = "ТВОЙ_API_KEY"

url = 
"https://oupenrouter.ai/api/v1/chat/completions"

headers = {
  "Authorization": f"Beaber
  {API_KEY}",
  "Content-Type": "applications/json"
}
data = {
  "model": "openai/gpt-3.5-turbo",
  "messages": [
    {'role': 'user', 'content':
'Hello! Say something about AI.'}
  ]
}
response = requests.post(url,
headers=headers, json=data)
print(response.json())
