ARG DOCKER_PHP_VERSION='7'
ARG TZ='Asia/Yekaterinburg'

FROM php:${DOCKER_PHP_VERSION}-fpm

# Set timezone to UTC
RUN echo "${TZ}" && rm /etc/localtime \
    && ln -s /usr/share/zoneinfo/$TZ /etc/localtime \
    && date

RUN apt-get update && apt-get install -y \
    bash \
    mc \
    curl \
    wget \
    git \
    nodejs \
    npm 

RUN apt-get update && apt-get install -y \
    libzip-dev \
    zip \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng-dev \
    libbz2-dev \
    libcurl4-gnutls-dev \
    libxml2-dev \
    libssl-dev \
    libc-client-dev \
    libkrb5-dev \
    zlib1g-dev \
    libicu-dev \
    g++ \
    libsqlite3-dev \
    libpspell-dev \
    libreadline-dev \
    libedit-dev \
    librecode-dev \
    libtidy-dev \
    libxslt1.1 \
    libxslt1-dev \
    ssmtp \
    snmp \
    libgmp-dev \
    libldb-dev \
    libldap2-dev \
    libsodium-dev \
    gnupg2

#  Install php extensions
RUN php -m \
  && docker-php-ext-configure bcmath --enable-bcmath \
  && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
  && docker-php-ext-install imap \
  && docker-php-ext-enable imap \
  && docker-php-ext-configure gettext \
  && docker-php-ext-configure intl \
  && docker-php-ext-install intl \
  # && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  # && docker-php-ext-configure gd \
  # && docker-php-ext-install gd \
  && docker-php-ext-install \
    bcmath \
    bz2 \
    calendar \
    ctype \
    curl \
    dba \
    # dom \
    exif \
    # fileinfo \
    # ftp \
    gettext \
    gmp \
    # hash \
    # iconv \
    # mbstring \
    # sodium \
    mysqli \
    opcache \
    pcntl \
    pdo \
    pdo_mysql \
    pdo_sqlite \
    phar \
    posix \
    pspell \
    ## readline \
    ## recode \
    session \
    shmop \
    # simplexml \
    ## snmp 
    soap \
    sockets \
    sysvmsg \
    sysvsem \
    sysvshm \
    tidy \
    # tokenizer \
    ## wddx \
    # xml \
    ## xmlrpc \
    # xmlwriter \
    ## xsl \
    zip

# # set up sendmail config
# RUN echo "hostname=localhost.localdomain" > /etc/ssmtp/ssmtp.conf
# RUN echo "root=vincent@vfac.fr" >> /etc/ssmtp/ssmtp.conf
# RUN echo "mailhub=maildev" >> /etc/ssmtp/ssmtp.conf
# # The above 'maildev' is the name you used for the link command
# # in your docker-compose file or docker link command.
# # Docker automatically adds that name in the hosts file
# # of the container you're linking MailDev to.
#
# # Set up php sendmail config
# RUN echo "sendmail_path=sendmail -i -t" >> /usr/local/etc/php/conf.d/php-sendmail.ini
#
# # Fully qualified domain name configuration for sendmail on localhost.
# # Without this sendmail will not work.
# # This must match the value for 'hostname' field that you set in ssmtp.conf.
# RUN echo "localhost localhost.localdomain" >> /etc/hosts

# composer
# COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
USER root
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
USER www-data:www-data

# Clean up
USER root
RUN apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
USER www-data:www-data

WORKDIR /var/www
