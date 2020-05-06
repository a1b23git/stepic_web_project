 
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
#sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/gunicorn.conf.py
gunicorn -c /etc/gunicorn.d/gunicorn.conf.py ask.wsgi:application
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello:app &
cd ask/
gunicorn --bind 0.0.0.0:8000 ask.wsgi &

