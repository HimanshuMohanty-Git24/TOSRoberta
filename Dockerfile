FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.port", "7860"]