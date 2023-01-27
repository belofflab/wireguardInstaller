apt install git -y

cd /home/ && git clone https://github.com/russianosint/wireguard-up.git

bash /home/wireguard-up/install.sh

cp /home/wireguard-up/vpn.service /etc/systemd/system/vpn.service

systemctl enable vpn
systemctl start vpn
