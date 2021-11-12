## Пример создания Веб Приложения

С использованием технологий:

- Docker 
- Compose 
- Flask 
- Gunicorn 
- PostgreSQL 
- pgamin
- nginx (reverse proxy) 

Для запуска:

```
# Билд
sudo docker-compose -f docker-compose.dev.yml build
# Запуск
sudo docker-compose -f docker-compose.dev.yml up
# Запуск в фоне
sudo docker-compose -f docker-compose.dev.yml up -d
# Остановка
sudo docker-compose -f docker-compose.dev.yml stop
```

## Внешние тома

База и приложение пробрасываются на хост! На деве - это норм, на проде - нужно спрятать внутрь!



## Полезные ссылки

https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/