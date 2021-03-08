from rest_app import user
from db_connector import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# backend testing, get info from sql to flask web as json.

res = requests.post('http://127.0.0.1:5000/users/1', json={"user_name": "itay"})

res = requests.get('http://127.0.0.1:5000/users/1')

select()

driver = webdriver.Chrome(executable_path=)
driver.get("http://127.0.0.1:5001/users/2")

