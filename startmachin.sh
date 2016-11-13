docker kill $(docker ps -a -q)&&docker rm $(docker ps -a -q)
docker-compose build
docker-compose up -d
docker-compose run web python /project/mysite/manage.py migrate --noinput --no-initial-data
