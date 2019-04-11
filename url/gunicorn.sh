#!/bin/bash
cd /opt/url
source venv/bin/activate
cd /opt/url/url
gunicorn url.wsgi -t 600 -b 127.0.0.1:8005 -w 6 --user=servidor --group=servidor --log-file=/opt/url/url.log 2>>/opt/url/url.log

