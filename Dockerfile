FROM python:3.12.8-alpine3.21

RUN apk add --no-cache \
    bash \
    curl \
    git \
    masscan \
    jq \
    libpcap \
    libpcap-dev 
    
WORKDIR /app
COPY . /app
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN python -m pip install --upgrade pip
RUN jq -r '.default \
        | to_entries[] \
        | .key + .value.version' \
        Pipfile.lock > requirements.txt 
RUN    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "entrypoint.py" ]