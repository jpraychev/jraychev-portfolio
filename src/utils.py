import re
import subprocess as ps

def get_last_commit_and_upstream_url(origin:str, main_branch:str) -> str:
    
    get_commit_cmd = f'git rev-parse --short {origin}/{main_branch}'
    get_upstream_cmd = f'git config --get remote.{origin}.url'

    try:
        commit = ps.run(get_commit_cmd, check=True, shell=True, capture_output=True, text=True).stdout.strip()
        upstream_url = ps.run(get_upstream_cmd, check=True, shell=True, capture_output=True, text=True).stdout.strip().split('.git')[0]
        return (commit, upstream_url)
    except ps.CalledProcessError:
        print(f'Either git is not initialized or there is no upstream repository available.')
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