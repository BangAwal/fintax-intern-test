sudo apt-get update -y

git clone https://github.com/BangAwal/fintax-intern-test.git
cd fintax-intern-test/

sudo apt-get install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx

sudo mv default /etc/nginx/sites-available/default
sudo systemctl restart nginx