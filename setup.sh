apt install git python3-pip -y

cd /home/ && git clone https://github.com/russianosint/wireguard-up.git

bash /home/wireguard-up/install.sh

cp /home/wireguard-up/vpn.service /etc/systemd/system/vpn.service

systemctl enable vpn
systemctl start vpn


pip3 install fastapi uvicorn

cp /home/wireguard-up/server.service /etc/systemd/system/server.service

systemctl enable server
systemctl start server

curl -X POST 'https://api.belofflab.com/api/v1/vpn/create?server_address='$(hostname -I | cut -d' ' -f1)''