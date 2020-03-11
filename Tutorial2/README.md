# Tutorial 2

## Customizing Flask Settings

Flas app has a config attribute which is a `dict` object and its used to set app configurations for flask.

To read more about configuration handling in flask, click [here](https://flask.palletsprojects.com/en/1.1.x/config/).


Flask config can be set via environment variable using `from_envvar` method. In this case we are using `FLASK_SETTINGS` environment variable

Flask can be run via inline env vars, for example:

        FLASK_SETTINGS=settings_module/dev.py flask run

There multiple ways of loading config. More details on it can be found [here](https://flask.palletsprojects.com/en/1.1.x/api/#configuration).
