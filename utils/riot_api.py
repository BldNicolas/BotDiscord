import requests
import json
import os

class Api:
    base_url = "https://api.henrikdev.xyz/valorant/"
    head = { 'accept' : 'application/json',
        'Authorization': os.getenv('HENRIK_TOKEN')}
    
    @staticmethod
    def call(endpoint:str):
        response = requests.get(
            f"{Api.base_url}{endpoint}",
            headers=Api.head
        )
        response.raise_for_status()
        return json.loads(response.text)
    
    @staticmethod
    def getPlayer(playerName:str, playerTag:str):
        response = Api.call(f"v1/account/{playerName}/{playerTag}")
        return response.get('data')
    
    @staticmethod
    def getMMR(playerName:str, playerTag):
        player = Api.getPlayer(playerName, playerTag)
        response = Api.call(
            f"v2/mmr/{player.get('region')}/{player.get('name')}/{player.get('tag')}"
        )
        return response
