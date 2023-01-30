sudo apt update -y
sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
sudo apt update -y
apt-cache policy docker-ce
sudo apt install docker-ce -y


sudo curl -L "https://github.com/docker/compose/releases/download/v2.13.0/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# cd /home/wireguard-up/ && docker-compose up -d 
docker run -d \
--sysctl net.ipv6.conf.all.disable_ipv6=0 \
--cap-add NET_ADMIN \
--name wg-manager \
#--net host \
-p "51800-51900:51800-51900/udp" \
-p "8888:8888" \
-v wg-manager:/config \
-e HOST="0.0.0.0" \
-e PORT="8888" \
-e ADMIN_USERNAME="admin" \
-e ADMIN_PASSWORD="admin" \
perara/wg-manager
