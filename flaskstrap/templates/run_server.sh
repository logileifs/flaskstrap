#!/usr/bin/env bash
uwsgi --http-socket :8000 -p 2 --import ~/.uwsgi/bootstrap.py --module {{project_name}}:app -H ~/.virtualenvs/{{project_name}}/