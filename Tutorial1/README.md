# Tutorial 1

## Starting a basic flask application

Flask application can be run in following ways:

* `flask run` command will look for `app.py` file in the current directory and use it to run the flask app

* If you want to run flask but you don't want to name the file as `app.py`, you need to set and environment variable `FLASK_APP` to specify the file name to run flask app.

        export FLASK_APP=app_two.py
        flask run

    You can set `FLASK_APP` variable per command basis instead of setting it in environment

        FLASK_APP=app_two.py flask run

* In order to run the flask application using python you can user the command below

        python app_three.py




