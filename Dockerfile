FROM python:3.12.5-alpine3.20

RUN apk add --no-cache \
    bash \
    curl \
    git \
    masscan
    
WORKDIR /app
COPY . /app

RUN python - m pipenv lock -r > deploy-requirements.txt --system --deploy --ignore-pipfile && \
    pip install --no-cache-dir -r deploy-requirements.txt

CMD ["python", "lib/checkdep.py" ]
