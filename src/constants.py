from pathlib import Path
from dotenv import load_dotenv

# This can be edited if other names are used
ABOUT_FILE = 'db/about.json'
CONTACT_FILE = 'db/contact.json'
EXPERIENCE_FILE = 'db/experience.json'
PROJECTS_FILE = 'db/projects.json'
SERVICES_FILE = 'db/services.json'


# Do no edit anything below
current_file_path = Path(__file__).parent

load_dotenv(dotenv_path=f'{current_file_path}/../venv/.env')

ABOUT_PATH = current_file_path.joinpath(f'{current_file_path}/{ABOUT_FILE}')
CONTACT_PATH = current_file_path.joinpath(f'{current_file_path}/{CONTACT_FILE}')
EXPERIENCE_PATH = current_file_path.joinpath(f'{current_file_path}/{EXPERIENCE_FILE}')
PROJECT_PATH = current_file_path.joinpath(f'{current_file_path}/{PROJECTS_FILE}')
SERVICES_PATH = current_file_path.joinpath(f'{current_file_path}/{SERVICES_FILE}')