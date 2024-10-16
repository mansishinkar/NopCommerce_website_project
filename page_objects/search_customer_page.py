from selenium.webdriver.common.by import By


class SearchCustomer:
    email_id = "SearchEmail"
    first_name_id = "SearchFirstName"
    last_name_id = "SearchLastName"
    search_button_id = "search-customers"

    # table xpath
    search_result_table_xpath = '//table[@id="customers-grid"]'
    table_xpath = '//table[@id="customers-grid"]'
    table_row_xpath = '//table[@id="customers-grid"]//tbody/tr'
    table_column_xpath = '//table[@id="customers-grid"]//tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def set_first_name(self, f_name):
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(l_name)

    def search_button(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def get_number_of_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def get_number_of_columns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1, self.get_number_of_rows() + 1):
            r = 1
            email_id = self.driver.find_element(By.XPATH,
                                                '//table[@id="customers-grid"]//tbody/tr[1]/td[2]'.format(r)).text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, name):
        flag = False
        for r in range(1, self.get_number_of_rows() + 1):
            name_id = self.driver.find_element(By.XPATH,
                                               '//table[@id="customers-grid"]//tbody/tr[{}]/td[3]'.format(r)).text
            if name_id == name:
                flag = True
                break
        return flag

    def search_customer_by_company_name(self, company_name):
        pass

    def search_customer_by_email_and_company_name(self, email, company_name):
        pass
