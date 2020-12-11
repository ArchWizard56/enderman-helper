import aiohttp
from utils import config

async def sendCommand(command):
    headers = {
        "Accept": "application/vnd.pterodactyl+json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.api.apiKey}"
    }
    async with aiohttp.ClientSession() as session:
        url = f"{config.api.apiUrl}/client/servers/{config.server.id}/command"
        async with session.post(url, headers=headers, json={"command": command}) as r:
            return r.status

async def sendSignal(signal):
    headers = {
        "Accept": "application/vnd.pterodactyl+json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.api.apiKey}"
    }
    async with aiohttp.ClientSession() as session:
        url = f"{config.api.apiUrl}/client/servers/{config.server.id}/power"
        async with session.post(url, headers=headers, json={"signal": signal}) as r:
            return r.status 