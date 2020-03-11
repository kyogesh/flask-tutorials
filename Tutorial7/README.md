# Tutorial 8
## Interacting with Jinja templates

Running flask app with gunicorn

        gunicorn --bind 0.0.0.0:8000 "manage:create_app()"