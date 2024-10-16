import time
from utility.read_properties import ReadConfig
from page_objects.login_page import LoginPage
from utility import xl_utils


class TestDdtLoginPage:
    base_url = ReadConfig.get_base_url()
    file_path = ".//test_data/login_data.xlsx"

    def test_ddt_login_page(self, set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login_page = LoginPage(self.driver)

        # login page
        rows = xl_utils.get_row_count(file_name=self.file_path, sheet_name='Sheet1')
        print("number of rows ::", rows)

        status_list = []
        for r in range(2, rows + 1):
            self.username = xl_utils.read_data(file_name=self.file_path, sheet_name='Sheet1', row_num=r, col_num=1)
            self.password = xl_utils.read_data(file_name=self.file_path, sheet_name='Sheet1', row_num=r, col_num=2)
            self.expected_op = xl_utils.read_data(file_name=self.file_path, sheet_name='Sheet1', row_num=r, col_num=3)

            self.login_page.set_user_name(self.username)
            self.login_page.set_password(self.password)
            self.login_page.click_login_button()
            time.sleep(3)

            expected_page_title = "Dashboard / nopCommerce administration"
            actual_page_title = self.driver.title

            if actual_page_title == expected_page_title:
                if self.expected_op == 'pass':
                    self.login_page.click_logout_button()
                    status_list.append('pass')

                elif self.expected_op == 'fail':
                    self.login_page.click_logout_button()
                    status_list.append('fail')

            elif actual_page_title != expected_page_title:
                if self.expected_op == 'fail':
                    status_list.append('pass')

                elif self.expected_op == 'pass':
                    status_list.append('fail')

        print("\n\n...................status_list......................\n\n")
        print(status_list)
        print("\n\n...................status_list......................\n\n")

        if 'fail' not in status_list:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
