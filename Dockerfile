FROM alpine:3.21

# Install required packages
RUN apk add --no-cache \
    bash \
    curl \
    git \
    masscan \
    python3 \
    py3-pip && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Set Python as default environment
CMD [ "bash" ]
