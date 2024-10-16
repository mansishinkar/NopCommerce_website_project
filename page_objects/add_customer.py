import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:
    customers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    customers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    add_new_button_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"

    email_input_xpath = "//input[@id='Email']"
    password_input_xpath = "//input[@id='Password']"
    first_name_xpath = "//input[@id='FirstName']"
    last_name_xpath = "//input[@id='LastName']"
    male_gender_id = "Gender_Male"
    female_gender_id = "Gender_Female"
    date_of_birth_xpath = "//input[@id='DateOfBirth']"
    company_name_xpath = "//input[@id='Company']"
    customer_roles_xpath = "//li[contains(text(),'Vendors')]"
    role_guests_xpath = "//li[contains(text(),'Guests')]"
    role_administrators_xpath = "//li[contains(text(),'Administrators')]"
    role_registered_xpath = "//li[contains(text(),'Registered')]"
    manager_of_vendor_xpath = "//*[@id='VendorId']"
    admin_comment_xpath = "//textarea[@id='AdminComment']"
    txt_customer_Roles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    save_button_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customer_menu(self):
        self.driver.find_element(By.XPATH, self.customers_menu_xpath).click()

    def click_customer_menu_item(self):
        self.driver.find_element(By.XPATH, self.customers_menuitem_xpath).click()

    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.add_new_button_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password)

    def set_first_name(self, fname):
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(lname)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.male_gender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.female_gender_id).click()
        else:
            self.driver.find_element(By.ID, self.male_gender_id).click()

    def set_date_of_birth(self, date_of_birth):
        self.driver.find_element(By.XPATH, self.date_of_birth_xpath).send_keys(date_of_birth)

    def set_company_name(self, company_name):
        self.driver.find_element(By.XPATH, self.company_name_xpath).send_keys(company_name)

    def set_admin_comment(self, admin_comment):
        self.driver.find_element(By.XPATH, self.admin_comment_xpath).send_keys(admin_comment)

    def set_manager_of_vendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.manager_of_vendor_xpath))
        drp.select_by_visible_text(value)

    def set_customer_roles(self, role):
        self.driver.find_element(By.XPATH, self.txt_customer_Roles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.list_item = self.driver.find_element(By.XPATH, self.role_registered_xpath)
        elif role == 'Administrators':
            self.list_item = self.driver.find_element(By.XPATH, self.role_administrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.list_item = self.driver.find_element(By.XPATH, self.role_guests_xpath)
        elif role == 'Registered':
            self.list_item = self.driver.find_element(By.XPATH, self.role_registered_xpath)
        elif role == 'Vendors':
            self.list_item = self.driver.find_element(By.XPATH, self.customer_roles_xpath)
        else:
            self.list_item = self.driver.find_element(By.XPATH, self.role_guests_xpath)
        time.sleep(3)
        # self.list_item.click()
        self.driver.execute_script("arguments[0].click();", self.list_item)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
