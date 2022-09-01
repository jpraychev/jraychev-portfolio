import re

def validate_string(string:str) -> str:
    """ Validates if a given string is valid according to a regex.
    Allowed characters are: a-z, A-Z, 0-9, !, -, _, +, =, ,, .,

    Args:
        string (str): String to be checked

    Returns:
        str: The original string if it is valid, otherwise raise an exception
    """
    regex = r"^[a-zA-Z0-9\!\-\_\+\=\,\.\s]*$"
    result = re.search(regex, string)
    if not result:
        raise ValueError(f'Invalid string passed {string}')
    return string

def generate_recaptcha_code():
        """
        Returns the new ReCaptcha code
        :return:
        """
        return """
        <input name="g-recaptcha-response" id="recaptcha" hidden></input>
        <script src="https://www.google.com/recaptcha/api.js?render=6LcevbYhAAAAADgeMdbvfQtFpOBgklwcIS-fCUpS"></script>
        <script>
        // Handles Google ReCaptcha logic
        btn = document.getElementsByTagName("button")[0]
        form = btn.closest("form")
        console.log(btn)
        // formBtn = document.getElementById('form-btn')
        btn.addEventListener("click", function(e){ 
            e.preventDefault();
            grecaptcha.ready(function() {
                grecaptcha.execute("6LcevbYhAAAAADgeMdbvfQtFpOBgklwcIS-fCUpS", {action: "submit"}).then(function(token) {
                    document.getElementById("recaptcha").value = token
                    form.submit()
                });
            });
        });
        </script>
        """
        