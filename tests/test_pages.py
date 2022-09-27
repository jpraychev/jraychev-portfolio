import sys
import time
import requests
from pathlib import Path
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


file_path = Path(__file__).resolve().parent

if sys.platform == 'win32':
    driver_name = 'geckodriver-win64.exe'
if sys.platform == 'linux':
    driver_name = 'geckodriver'

drivers_path = file_path.joinpath(f'drivers/{driver_name}')

url = 'http://127.0.0.1:5050/'

def test_homepage():
    r = requests.get(url + 'home')
    print(r.text)
    assert r.status_code == 200

def test_services():
    r = requests.get(url + 'services')
    assert r.status_code == 200

def test_experience():
    r = requests.get(url + 'experience')
    assert r.status_code == 200

def test_projects():
    r = requests.get(url + 'projects')
    assert r.status_code == 200

def test_blog():
    r = requests.get(url + 'blog')
    assert r.status_code == 200

def test_contact():
    r = requests.get(url + 'contact')
    assert r.status_code == 200

def test_contact_failure_post():
    data = {}
    data['name'] = 'admin'
    data['email'] = 'admin@admin.com'
    data['subject'] = 'pytest'
    data['message'] = 'pytest'

    r = requests.post(url + 'contact', params=data)
    assert r.status_code in (400, 500)

def test_contact_success_post():
    service = Service(executable_path=drivers_path, log_path=None)
    options = Options()
    options.headless = True # or options.add_argument('-headless')
        
    driver = Firefox(service=service, options=options)
    driver.get(url + 'contact')

    name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_name')))
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_email')))
    subject_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_subject')))
    message_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'id_message')))
    submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'form-btn')))
    
    name_field.send_keys('admin')
    email_field.send_keys('admin@admin.com')
    subject_field.send_keys('pytest')
    message_field.send_keys('pytest')
    submit_button.click()
    
    # TO DO
    # Always close the driver - if we get an exception from the assert the driver process will hand
    time.sleep(1)
    success_fail_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div')))
    assert 'Your message has been sent successfully!' in success_fail_field.text

    driver.close()