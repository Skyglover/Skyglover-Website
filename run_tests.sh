#!/usr/bin/env bash
# Change /home/m/.virtualenvs/env/bin/python with the location of your python environment
/home/m/.virtualenvs/env/bin/python manage.py test
for test_file in ./functional_tests/*/*.py; do /home/m/.virtualenvs/env/bin/python "$test_file"; done
git co db.sqlite3
