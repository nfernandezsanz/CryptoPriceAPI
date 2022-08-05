FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install libssl-dev
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet 
RUN python3 -m nltk.downloader vader_lexicon
RUN python3 -m nltk.downloader omw-1.4
RUN python3 -m nltk.downloader stopwords
RUN python3 -m spacy download en
COPY . /code/