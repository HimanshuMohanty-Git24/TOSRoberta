FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Download the spaCy model
RUN python -m spacy download en_core_web_sm

# Link the spaCy model
RUN python -m spacy link en_core_web_sm en

COPY . /code

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.port", "7860"]
