#! /bin/bash
gunicorn -c /opt/portfolio/deployment/gunicorn-conf.py app:app --daemon
cd /opt/portfolio/tests/
chmod +x /opt/portfolio/tests/drivers/geckodriver
pytest -s
ls -la /opt/portfolio/tests
ls -la /opt/portfolio/tests/drivers
whoami