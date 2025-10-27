FROM php:8.2-apache

# Instala as extensões necessárias
RUN docker-php-ext-install pdo pdo_mysql mysqli

# (opcional) habilita rewrite se tiver rotas
RUN a2enmod rewrite

# Copia o código depois (melhor uso de cache)
COPY src/ /var/www/html/

EXPOSE 80