FROM nginx:1.22.1
LABEL org.opencontainers.image.authors='slavas62@gmail.com'

RUN apt-get update && apt-get install -y \
  supervisor \
  gcc \
  python3-dev \
  python3-venv \
  python3-gdal \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#  python-virtualenv \

ENV work_dir=/app

WORKDIR ${work_dir}

# RUN virtualenv --python=python3 --system-site-packages /env
RUN python3 -m venv --system-site-packages /env

ADD . .

RUN /env/bin/pip install --upgrade pip

RUN cp ./docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf &&\
    cp ./docker/nginx.conf /etc/nginx/conf.d/default.conf &&\
    /env/bin/pip install -r requirements.txt

RUN /env/bin/python /app/manage.py collectstatic --noinput

VOLUME /env/www/media

EXPOSE 80

# set default locale for python
ENV LANG=C.UTF-8 

CMD ["./docker/docker_start.sh"]
