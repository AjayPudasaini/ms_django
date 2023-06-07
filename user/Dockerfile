FROM python:3.10.6

RUN mkdir ms_django_user_app_v1
WORKDIR /ms_django_user_app_v1
COPY /user/ /ms_django_user_app_v1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

