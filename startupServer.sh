sudo apt-get update -y
sudo apt-get install python3-virtualenv -y
sudo apt-get install python3-venv -y

git clone https://github.com/BangAwal/fintax-intern-test.git
cd fintax-intern-test/

sudo python3 -m venv venv
source venv/bin/activate
pip install Flask 
pip install gunicorn 

sudo systemctl restart nginx

sudo fuser -k 8000/tcp
gunicorn -b 0.0.0.0:8000 alphaServer:app