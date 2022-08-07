sudo apt-get update -y
sudo apt install python3-pip -y
sudo apt install gunicorn -y

pip3 install Flask 
pip3 install gunicorn 
pip3 install flask-restful

git clone https://github.com/BangAwal/fintax-intern-test.git
cd fintax-intern-test/

sudo systemctl restart nginx
sleep 10

sudo fuser -k 8000/tcp
gunicorn -b 0.0.0.0:8000 alphaServer:app