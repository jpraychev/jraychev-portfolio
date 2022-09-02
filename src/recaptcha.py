from flask import request
from markupsafe import Markup
import requests
import os


class ReCaptcha:

    VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'

    def __init__(
        self,
        app: str,
        site_key: str = None,
        site_secret: str = None
    ):
        self.app = app
        self.app.context_processor(self.gorecaptcha)
        self.site_key = os.getenv('RECAPTCHA_SITE_KEY') if site_key is None else site_key
        self.site_secret = os.getenv('RECAPTCHA_SECRET_KEY') if site_secret is None else site_secret

    def verify(self):

        data = {
            'secret': self.site_secret,
            'response' : request.form['g-recaptcha-response']
        }

        r = requests.post(self.VERIFY_URL, data=data)

        if r.status_code != 200:
            raise Exception('Invalid request')
        if not r.json()['success']:
            return False
        return True

    def gorecaptcha(self):
        return dict(recaptcha_code = Markup(self.__generate_code()))
    
    def __generate_code(self):
            """
            Returns the new ReCaptcha code
            :return:
            """
            left_brace = "{"
            right_brace = "}"
            
            return f"""
            <input name='g-recaptcha-response' id='recaptcha' hidden></input>
            <script src='https://www.google.com/recaptcha/api.js?render={self.site_key}'></script>
            <script>
            // Handles Google ReCaptcha logic
            btn = document.getElementsByTagName('button')[0]
            form = btn.closest('form')
            btn.addEventListener('click', function(e) {left_brace}
                e.preventDefault();
                grecaptcha.ready(function() {left_brace}
                    grecaptcha.execute('{self.site_key}', {left_brace} action: 'submit' {right_brace}).then(function(token) {left_brace}
                        document.getElementById('recaptcha').value = token
                        form.submit()
                     {right_brace});
                 {right_brace});
             {right_brace});
            </script>
            """