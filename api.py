import requests

response = requests.get(
    "https://raw.githubusercontent.com/solana-labs/token-list/main/src/tokens/solana.tokenlist.json")

output = response.json()
for i in output['tokens']:
    if i.get('extensions'):
        print(i.get('extensions').get('discord'))