FROM python:3.9.0

WORKDIR /home/

RUN echo "adsf"

RUN git clone https://github.com/ClearRoot/web_image_upscaler.git

WORKDIR /home/web_image_upscaler/

RUN pip install -r requirements.txt

RUN pip install --upgrade pip

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=ImageUpscaler.settings.deploy && python manage.py migrate --settings=ImageUpscaler.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=ImageUpscaler.settings.deploy ImageUpscaler.wsgi --bind 0.0.0.0:8000"]