FROM python:3.12.7-slim

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /

CMD ["streamlit", "run", "PartyTime.py"]