FROM php:7.1-fpm-alpine

# install system dependencies
RUN apk add --no-cache git \
  icu-dev \
  libpng-dev \
  supervisor

# install PHP extensions, composer, and hirak/prestissimo
RUN apk add --no-cache --virtual .build-deps autoconf gcc g++ make linux-headers && \
  docker-php-ext-install intl pdo_mysql mysqli exif bcmath gd zip sockets && \
  pecl install redis grpc && docker-php-ext-enable redis grpc && \
  docker-php-source delete && \
  apk del .build-deps && \
  curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/bin/composer && chmod +x /usr/bin/composer && \
  composer global require hirak/prestissimo --no-plugins --no-scripts

# set working directory
WORKDIR /app