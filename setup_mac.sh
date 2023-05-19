#!/bin/bash

psql -c "DROP DATABASE IF EXISTS $LEARN_OPS_USER WITH (FORCE);"
psql -c "CREATE DATABASE $LEARN_OPS_USER;"
psql -c "CREATE USER $LEARN_OPS_USER WITH PASSWORD '$LEARN_OPS_PASSWORD';"
psql -c "ALTER ROLE $LEARN_OPS_USER SET client_encoding TO 'utf8';"
psql -c "ALTER ROLE $LEARN_OPS_USER SET default_transaction_isolation TO 'read committed';"
psql -c "ALTER ROLE $LEARN_OPS_USER SET timezone TO 'UTC';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE $LEARN_OPS_USER TO $LEARN_OPS_USER;"

echo '[
    {
       "model": "sites.site",
       "pk": 1,
       "fields": {
          "domain": "learningplatform.com",
          "name": "Learning Platform"
       }
    },
    {
        "model": "socialaccount.socialapp",
        "pk": 1,
        "fields": {
            "provider": "github",
            "name": "Github",
            "client_id": "'"$LEARN_OPS_CLIENT_ID"'",
            "secret": "'"$LEARN_OPS_SECRET_KEY"'",
            "key": "",
            "sites": [
                1
            ]
        }
    }
  ]
' > ./LearningAPI/fixtures/socialaccount.json


export DJANGO_SETTINGS_MODULE="LearningPlatform.settings"
PWD=$(python3 ./djangopass.py "$LEARN_OPS_SUPERUSER_PASSWORD" >&1)


echo '[
    {
        "model": "auth.user",
        "pk": null,
        "fields": {
            "password": "'"$PWD"'",
            "last_login": null,
            "is_superuser": true,
            "username": "'"$LEARN_OPS_SUPERUSER_NAME"'",
            "first_name": "Admina",
            "last_name": "Straytor",
            "email": "me@me.com",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2023-03-17T03:03:13.265Z",
            "groups": [
                2
            ],
            "user_permissions": []
        }
    }
]' > ./LearningAPI/fixtures/superuser.json

# Install project requirements
pipenv install

# Run existing migrations
python3 manage.py migrate

# Load data from backup
python3 manage.py loaddata socialaccount
python3 manage.py loaddata complete_backup
python3 manage.py loaddata superuser

rm ./LearningAPI/fixtures/superuser.json
rm ./LearningAPI/fixtures/socialaccount.json