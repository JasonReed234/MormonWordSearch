#MormonWordSearch

Mormonwordsearch is an app designed to prevent misinformation in the Mormon community. This app finds every instance of any given word in the Mormon corpus* and contextually renders it to the user with sources cited. The intended audience includes current and former members of the LDS church or anybody interested in historical accuracy as it pertains to the LDS church.

*Mormon corpus includes general conference talks, scriptures, handbooks, newsletters, books written by general authorities of the church, etc.

Next steps:
1) Upload large Mormon corpus file to a PaaS (it is currently on my PC, program will not run until this step is complete)
2) Provide formatting to enable an aesthetically pleasing output
3) Complete the Mormon corpus file (currently contains all general conference talks from 1897-2011)
4) Include "usage over time" charts for any word searched
5) Implement ideas sourced from the community


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
