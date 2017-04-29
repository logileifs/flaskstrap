# flaskstrap
flaskstrap sets up a new skeleton flask project and helps you get up and running live just with a few commands

## Install
`pip install flaskstrap`

## Example
`$ mkvirtualenv new_project`

`$ pip install flaskstrap`

`$ flaskstrap init new_project`

`$ tree new_project`
```
new_project/
├── makefile
├── requirements.txt
├── src
│   ├── __main__.py
│   └── new_project.py
└── tests
    └── unit-tests.py
```

## Usage

### flaskstrap init <project_name>
Create a new flask project called project_name

### flaskstrap setup
Sets up a new server fully configured with nginx+uwsgi+upstart to run your application
