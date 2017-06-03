#!/usr/bin/env bash
killall -r gunicorn
gunicorn --daemon --workers 3 --bind unix:/root/thecovfefe/covfefe.sock thecovfefe.wsgi&
service nginx restart
