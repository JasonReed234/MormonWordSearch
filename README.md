# DjangoMormonWordSearch4

#My 4th attempt at this.

#Mormonwordsearch is an app designed to prevent misinformation in the mormon community. The user can type a word into the search bar and see where it has been used throughout the church's history.


## Deploy to Heroku
1. Requirements
    1. Git
    1. Heroku CLI

1. Create Heroku app and add git remote
    ```bash
    $ heroku create <app-name: optional value or let heroku autocreate app name>
    $ heroku git:remote -a <app-name>
    ```

1. Ensure database has been provisioned
    ```bash
    $ heroku addons
        * If no database *
    $ heroku addons:create heroku-postgresql:hobby-dev
    ```

1. Set Environment Variables
    ```bash
    $ heroku config:set SECRET_KEY=<your_secret_key_here>
    ```

1. Deploy to Heroku - also use to redeploy updates
    ```bash
    $ git push heroku master
    ```

1. Deploy from **non-master** branch
    ```bash
    $ git push heroku <current-branch>:master
    ```

1. Create a superuser
    ```bash
    $ heroku run python manage.py createsuperuser
    ```