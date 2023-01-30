import os
import subprocess

from fastapi import FastAPI

app = FastAPI()

def clean_iptables(address: str ):
  iptables_address = subprocess.check_output('docker exec -t wireguard iptables -L INPUT --line-number', shell=True).decode('utf-8').split('\n')
  matches = [iptable for iptable in iptables_address if address in iptable]
  if len(matches) > 1:
    subprocess.check_output(f'docker exec -t wireguard iptables -D INPUT {matches[0].split(" ")[0]}', shell=True)
  else:
    for match in matches:
      subprocess.check_output(f'docker exec -t wireguard iptables -D INPUT {match.split(" ")[0]}', shell=True)

@app.get('/address/block')
async def block_address(address: str):
  clean_iptables(address=address)
  subprocess.check_output(f"docker exec -t wireguard iptables -A INPUT -s {address}/32 -j DROP", shell=True)

@app.get('/address/allow')
async def allow_address(address: str):
  clean_iptables(address=address)
  subprocess.check_output(f"docker exec -t wireguard iptables -A INPUT -s {address}/32 -j ACCEPT", shell=True)