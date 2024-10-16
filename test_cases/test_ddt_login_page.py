import time
import pytest
from utility.read_properties import ReadConfig
from page_objects.login_page import LoginPage
from utility import xl_utils


class TestDdtLoginPage:
    base_url = ReadConfig.get_base_url()

    file_name = "C:\\Users\\mansi\\PycharmProjects\\NopCommerce_website_project\\test_data\\proj_ddt.xlsx"

    @pytest.mark.parametrize("username, password, excel_result_column, row_n", ([
                                                                                    xl_utils.read_data(row_num=2,
                                                                                                       col_num=1),
                                                                                    xl_utils.read_data(row_num=2,
                                                                                                       col_num=2),
                                                                                    xl_utils.read_data(row_num=2,
                                                                                                       col_num=3),
                                                                                    2
                                                                                ],
                                                                                [
                                                                                    xl_utils.read_data(row_num=3,
                                                                                                       col_num=1),
                                                                                    xl_utils.read_data(row_num=3,
                                                                                                       col_num=2),
                                                                                    xl_utils.read_data(row_num=3,
                                                                                                       col_num=3),
                                                                                    3
                                                                                ],
                                                                                [
                                                                                    xl_utils.read_data(row_num=4,
                                                                                                       col_num=1),
                                                                                    xl_utils.read_data(row_num=4,
                                                                                                       col_num=2),
                                                                                    xl_utils.read_data(row_num=4,
                                                                                                       col_num=3),
                                                                                    4
                                                                                ]
    ))
    def test_ddt_login_page(self, set_up, username, password, excel_result_column, row_n):
        self.driver = set_up
        self.driver.get(self.base_url)

        # Login page
        self.login_page = LoginPage(self.driver)
        self.login_page.set_user_name(username)
        self.login_page.set_password(password)

        self.login_page.click_login_button()
        time.sleep(3)

        pg_title = self.driver.title

        # read "result" from excel page
        result = ""

        print("\n\nexcel_result_column ::", excel_result_column)
        print("page_title ::", pg_title)

        if pg_title == excel_result_column:
            xl_utils.write_data(row_num=row_n, col_num=4, data="Pass")
            self.driver.close()
            assert True

        else:
            xl_utils.write_data(row_num=row_n, col_num=4, data="Fail")
            self.driver.close()
            assert False
