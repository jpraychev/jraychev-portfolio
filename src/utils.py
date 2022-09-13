import re
import subprocess as ps

def get_upstream_branch() -> str:
    
    cmd = 'git config --get remote.origin.url'
    try:
        upstream_url = ps.run(cmd, check=True, shell=True, capture_output=True, text=True)
        return upstream_url.stdout.strip().split('.git')[0]
    except ps.CalledProcessError:
        print('No upstream branch found')
        return False

def get_branch_last_commit_hash(main_branch:str) -> str:
    
    cmd = f'git rev-parse --short origin/{main_branch}'
    try:
        result = ps.run(cmd, check=True, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except ps.CalledProcessError:
        print(f'Branch {main_branch} not found!')
        return False

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