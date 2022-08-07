sudo apt-get update -y

git clone https://github.com/BangAwal/fintax-intern-test.git
cd fintax-intern-test/

pip3 install Flask 
pip3 install gunicorn 

sudo systemctl restart nginx
sleep 15

sudo fuser -k 8000/tcp
gunicorn -b 0.0.0.0:8000 alphaServer:app