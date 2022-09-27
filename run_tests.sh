#! /bin/bash
gunicorn -c /opt/portfolio/deployment/gunicorn-conf.py app:app --daemon
cd /opt/portfolio/tests/
pytest -s
cat /opt/portfolio/src/logs/debug.log