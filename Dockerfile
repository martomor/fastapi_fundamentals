FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/

RUN chmod u+x start.sh

EXPOSE 8000

CMD ["./start.sh"]