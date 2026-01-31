# Demo ГИП Геотрон

**Install Postgresql**

```console

docker run --name postgres --restart=always -p 5432:5432 -v /data/postgres:/var/lib/postgresql/data -e    POSTGRES_PASSWORD=ololo -d mdillon/postgis:9.4
```

**Create database**


```console

docker exec -it postgres psql -U postgres -c 'CREATE DATABASE rks_site;' && docker exec -it postgres psql -d rks_site -U postgres -c 'CREATE EXTENSION postgis;'

```

** Run **
```
# virtualenv
virtualenv --python=python3 /project/rks-site
cd /project/rks-site && source bin/activate

# clone project

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Build and run docker**

```console
docker build -t rks-site .
./run.sh
```
