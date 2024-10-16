import time
import pytest
from page_objects.login_page import LoginPage
from utility.read_properties import ReadConfig


class TestLoginPage:
    base_url = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    # @pytest.mark.order("first")
    def test_page_title(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(2)

        page_title = self.driver.title
        time.sleep(1)

        if page_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("screenshots\\" + "test_page_title.png")
            self.driver.close()
            assert False

    @pytest.mark.login
    def test_login(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(2)
        self.login_pg_obj = LoginPage(self.driver)
        self.login_pg_obj.set_user_name(self.username)
        self.login_pg_obj.set_password(self.password)
        self.login_pg_obj.click_login_button()
        time.sleep(2)

        page_title = self.driver.title

        if page_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("screenshots\\" + "test_login_page_title.png")
            self.driver.close()
            assert False

    @pytest.mark.login
    def test_login_with_invalid_credentials(self, set_up):
        pass
