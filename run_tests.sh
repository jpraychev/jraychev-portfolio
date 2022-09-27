#! /bin/bash
gunicorn -c deployment/gunicorn-conf.py app:app --daemon
pytest