#! /bin/bash
gunicorn -c /opt/portfolio/deployment/gunicorn-conf.py app:app --daemon
pytest