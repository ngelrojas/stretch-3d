TRAVIS CI [![Build Status](https://travis-ci.org/ngelrojas/stretch-3d.svg?branch=master)](https://travis-ci.org/ngelrojas/stretch-3d)

# STRETCH 3D

stretch-3d is just to begin a project using Django, Django Rest Framework and Docker.

this configuration is based in multi-stage build, you can see the final image size is lighter.

it's integrated with swagger to documentation API's

is based in 12 factor to good developing

### Configuration env files and description

- remove prefix ".example" in all .env files
- `.env` file is develop environment
- `.env_prod` is production environment
- `.env.prod.db` is database production environment
- `.env.prod.pgadmin` is pg-admin panel production

in all .env put your data, to connection postgresql

### Run mode Development

- when run develop environment, use a settings folder and development.py, and config your own settings configuration, that environment.

#### run basic develop environment

- up your environment

```python
    docker-compose up -d --build
```

- run migrate environment

```python
    docker-compose exec api python manage.py migrate
```

- run createsuperuser

```python
    docker-compose exec api python manage.py createsuperuser
```

- create project

```python
    docker-compose exec api python startapp your_name_app
```

- this script run test and flake8 in all tests modules

```python
    docker-compose run api sh -c "python manage.py test && flake8"
```

or use, but just run a test

```python
    docker-compose exec api python manage.py test
```

- down docker

```python
    docker-compose down -v
```

### run mode production

- when run production environment, use a settings folder and production.py, and config your own settings configuration, that environment.

#### run basic production environment

- up your environment

```python
    docker-compose -f docker-compose.prod.yml up -d --build
```

- run migrate production

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py migrate
```

- run createsuperuser

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py createsuperuser
```

- run create app

```python
    docker-compose -f docker-compose.prod.yml exec api python startapp your_name_app
```

- this script run a test and flake8 in all test modules

```python
    docker-compose -f docker-compose.prod.yml run api sh -c "python manage.py test && flake8"
```

or use, this script but jus a run test in all modules

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py test
```

#### troubleshooting

- if the panel admin not working try this:

- don't stop current container

- edit docker-compose.prod.yml and add '/api/' in volumes like this:

```python
    -static_volume: /home/app/api/api/staticfiles
```

- run the script

```python
    docker-compose -f docker-compose.prod.yml run sh -c "python manage.py collectstatic --no-input --clear"
```
