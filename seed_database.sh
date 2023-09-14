#!/bin/bash

rm db.sqlite3
rm -rf ./parallel_place_api/migrations
python3 manage.py migrate
python3 manage.py makemigrations parallel_place_api
python3 manage.py migrate parallel_place_api
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata teachers
python3 manage.py loaddata students
python3 manage.py loaddata vocab_words
python3 manage.py loaddata assignments
python3 manage.py loaddata assignment_submissions
python3 manage.py loaddata character_list 
python3 manage.py loaddata inspiration_list
python3 manage.py loaddata discussion_topics
python3 manage.py loaddata discussion_comments
python3 manage.py loaddata about_the_author

