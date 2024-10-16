import time
import string
import random
from page_objects.login_page import LoginPage
from page_objects.add_customer import AddCustomer
from utility.read_properties import ReadConfig
from selenium.webdriver.common.by import By


class TestAddCustomers:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_add_customer(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)

        self.login_page = LoginPage(self.driver)
        self.login_page.set_user_name(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()
        time.sleep(2)

        # add customer page
        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_customer_menu()
        time.sleep(1)
        self.add_customer.click_customer_menu_item()
        time.sleep(2)

        self.add_customer.click_add_new()
        time.sleep(2)
        self.email = random_generator() + "@gmail.com"
        self.add_customer.set_email(self.email)
        self.add_customer.set_password("test123")
        # self.add_customer.set_customer_roles("Guests")
        # self.add_customer.set_manager_of_vendor("Vendor 2")
        self.add_customer.set_gender("Male")
        self.add_customer.set_first_name("Ravi")
        self.add_customer.set_last_name("Jadhav")
        self.add_customer.set_date_of_birth("12/12/1996")  # Format: DD/ MM / YYY
        self.add_customer.set_company_name("HSBC")
        self.add_customer.set_admin_comment("Company name is HSBC")
        self.add_customer.click_save()
        time.sleep(3)

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'successfully.' in self.msg:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            assert False

        self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
