FROM nginx:stable

# Install python
RUN apt-get update && apt-get -y install python-dev build-essential python-pip certbot && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app
RUN pip --no-cache-dir install -r /app/requirements.txt

COPY configs/authorizer.cfg /etc/scitokens-auth/authorizer.cfg
COPY configs/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

CMD ["/bin/bash", "/app/tools/run_app.sh"]
