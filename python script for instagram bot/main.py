from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
    
    def login(self, username, password):
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_box(self):
        return LoginPage(self.browser)

home_page = HomePage(browser)
login_page = home_page.go_to_login_box()
login_page.login("sek_davara_codes", 'Sek_d_251298')

browser.close()
