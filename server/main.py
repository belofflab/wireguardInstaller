import os
import subprocess

from fastapi import FastAPI

app = FastAPI()



@app.get('/address/block')
async def block_address(address: str):
  subprocess.check_output(
        f"docker exec -t wireguard iptables -A  INPUT s {address} -j DROP", shell=True)

@app.get('/address/allow')
async def allow_address(address: str):
  subprocess.check_output(
        f"docker exec -t wireguard iptables -A  INPUT s {address} -j ACCEPT", shell=True)

@app.get('/configs')
async def get_configs():
  return {'configs':[file for file in os.listdir('/root/wireguard/config') if file.startswith('peer')]}

# @app.get('/generate_peer')
# async def generate_peer():
#   privkey = subprocess.check_output(
#         "docker exec -t wireguard wg genkey", shell=True).decode("utf-8").strip()
#   pubkey = subprocess.check_output(
#       f"docker exec -t echo '{privkey}' | wg pubkey", shell=True).decode("utf-8").strip()
#   psk = subprocess.check_output(
#       "docker exec -t wg genkey", shell=True).decode("utf-8").strip()
#   addresses = subprocess.check_output("docker exec -t wireguard wg show", shell=True)
#   address = addresses.decode("utf-8").strip().split('allowed ips')[-1]
#   clean_address =  re.findall( r'[0-9]+(?:\.[0-9]+){3}', address)[0]
#   clean_address.replace(clean_address.split('.')[-1], str(int(clean_address.split('.')[-1]) + 1))
#   return (privkey, pubkey, psk)