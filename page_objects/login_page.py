from selenium.webdriver.common.by import By


class LoginPage:
    username_id = "Email"
    password_id = "Password"
    login_button_xpath = '//button[@class="button-1 login-button"]'
    logout_link_text = '//a[@href="/logout"]'

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_link_text).click()
