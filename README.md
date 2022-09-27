# [Porfolio](https://www.jraychev.com) &middot; [![Tests](https://github.com/jpraychev/jraychev-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/jpraychev/jraychev-portfolio/actions/workflows/tests.yml) [![Deploy](https://github.com/jpraychev/jraychev-portfolio/actions/workflows/deploy.yml/badge.svg)](https://github.com/jpraychev/jraychev-portfolio/actions/workflows/deploy.yml) 

# Introduction
The current project is a personal portfolio of mine, powered by the Flask framework. It is heavily used for learning purposes and its not guaranteed to work all the time. Included into the project are the following ideas:
- Dynamic build of the last github commit shown to users
- Google recaptcha provided by its own library located at https://github.com/jpraychev/google-recaptcha
- Telegram bot notification triggered by contact events
- Tests running inside an ubuntu docker container
- Deployment strategy ran if tests are successfyl

# Usage
The project could be cloned and ran as follows:

## 1. Prerequisites (pip, google recaptcha tokenes for v3/v2, telegram bot token)
```
pip install -r requirements.txt
export RECAPTCHA_SITE_KEY=<TOKEN GOES HERE>
export RECAPTCHA_SECRET_KEY=<TOKEN GOES HERE>
export TELEGRAM_BOT_TOKEN=<TOKEN GOES HERE>
```

## 2. Dev mode (without gunicorn)
```
python .\src\app.py

 * Serving Flask app 'app'
 * Debug mode: on WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5050
   Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 902-470-930
```

## 3. Prod mode (with gunicorn running in daemon mode - check configuration file to see IP address and port (default 127.0.0.1:5050))
```
gunicorn -c deployment/gunicorn-conf.py app:app --daemon
```

## 4. Run tests locally
```
cd tests
pytest
==================================================================================================================== test session starts ==================================================================================================================== 
platform win32 -- Python 3.10.5, pytest-7.1.3, pluggy-1.0.0
rootdir: D:\Personal Projects\portfolio\tests
collected 7 items                                                                                                                                                                                                                                             

test_pages.py .......                                                                                                                                                                                                                                  [100%] 

===================================================================================================================== 7 passed in 2.14s ===================================================================================================================== 
```