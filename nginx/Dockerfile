FROM nginx:latest
LABEL maintainer="Eduardo Rojas Tejo <eduardo.rojast@sonda.com>"

ARG DOCKER_HTTP_USER=registry
ARG DOCKER_HTTP_PASS=1q2w3e4r5t

RUN  rm /etc/nginx/conf.d/default.conf && \
    apt-get update && \
    apt-get install -y --no-install-recommends apache2-utils && \
    rm -r /var/lib/apt/lists/* && \    
    htpasswd -cb /etc/nginx/.docker-htpasswd ${DOCKER_HTTP_USER} ${DOCKER_HTTP_PASS}

ADD nginx.conf /etc/nginx/
COPY sites/*.conf /etc/nginx/sites-available/

CMD ["nginx"]
EXPOSE 80 443