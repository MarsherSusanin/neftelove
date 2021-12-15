#!/usr/bin/env bash
#
#   Запуск нужного состояния контейнера
#   laravel app | queue | scheduler
#
set -e

role=${CONTAINER_ROLE:-app}
env=${APP_ENV:-production}

# if [ "$env" != "local" ]; then
#     echo "Caching configuration..."
#     # cd /var/www/html_nakanune.ru/adm02
#     # (cd /var/www/html_nakanune.ru/adm02 && php artisan config:cache && php artisan route:cache && php artisan view:cache)
#     ## php artisan config:clear && php artisan route:clear && php artisan view:clear && php artisan cache:clear
# fi

if [ "$role" = "app" ]; then
    exec php-fpm

elif [ "$role" = "supervisor" ]; then
    echo "Running the supervisor..."
    /usr/bin/supervisord -n -c /etc/supervisord.conf

elif [ "$role" = "queue" ]; then
    echo "Running the queue..."
    cd /var/www/html
    php /var/www/html/artisan queue:work --verbose --sleep=1 --tries=1 --timeout=900
    php /var/www/html/artisan queue:listen --verbose --sleep=1 --tries=1 --timeout=900
    ## В сдучае появления неудачных заданий
    ## php artisan queue:retry all
    ## php artisan queue:work --stop-when-empty
    ## php artisan queue:restart

elif [ "$role" = "scheduler" ]; then
    cd /var/www/html
    while [ true ]
    do
      php /var/www/html/artisan schedule:run --verbose --no-interaction &
      sleep 60
    done

else
    echo "Could not match the container role \"$role\""
    exit 1
fi

####
# Команды для перезапуска
#
# php artisan config:clear && php artisan route:clear && php artisan view:clear && php artisan cache:clear && php artisan queue:restart
#
