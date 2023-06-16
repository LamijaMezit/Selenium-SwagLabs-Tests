from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()
    
    def login(self, username, password):

        username_field_locator = (By.ID, "user-name")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()
    
    
    def verification_products_title(self):
        products_title_locator=(By.XPATH, "//span[@class='title' and text()='Products']")
        wait_products_title_field= self.wait.until(EC.presence_of_element_located(products_title_locator))

        products_title_locator = wait_products_title_field.text
        assert products_title_locator == "Products"
        #print("TEST PASSED : LOGIN SUCCESSFUL")
    
    def adding_two_products_to_cart(self):
        product_1= self.selenium_driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        product_2=self.selenium_driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")

        shopping_cart= self.selenium_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")

        product_1.click()
        product_2.click()
        shopping_cart.click()
    
    def verification_your_cart_title(self):
        your_cart_locator=(By.XPATH, "//span[@class='title' and text()='Your Cart']")
        wait_your_cart_field= self.wait.until(EC.presence_of_element_located(your_cart_locator))

        your_cart_locator = wait_your_cart_field.text
        assert your_cart_locator == "Your Cart"
    
    def verification_products_in_the_chart(self):
      name_of_product_1= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']")
      name_of_product_2= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div[@class='inventory_item_name']")
  
      assert name_of_product_1.text=="Sauce Labs Backpack"
      assert name_of_product_2.text=="Sauce Labs Bike Light"


    def click_on_the_checkout(self):
        click_checkout=self.selenium_driver.find_element(By.ID, "checkout")
        click_checkout.click()
    
    def verification_your_information_title(self):
        your_infomation_locator=(By.XPATH, "//span[@class='title' and contains(text(),'Checkout: Your Information']")
        wait_your_information_field= self.wait.until(EC.presence_of_element_located(your_infomation_locator))

        your_infomation_locator= wait_your_information_field.text
        assert your_infomation_locator == "Checkout: Your Information"
    
    def filling_the_fields(self,first_name,last_name, zip_code):
        first_name_field_locator = (By.ID, "first-name")
        wait_first_name_field = self.wait.until(EC.element_to_be_clickable(first_name_field_locator))
        wait_first_name_field.click()
        wait_first_name_field.clear()
        wait_first_name_field.send_keys(first_name)

        last_name_field_locator = (By.ID, "last-name")
        wait_last_name_field = self.wait.until(EC.element_to_be_clickable(last_name_field_locator))
        wait_last_name_field.click()
        wait_last_name_field.clear()
        wait_last_name_field.send_keys(last_name)

        zip_code_field_locator = (By.ID, "postal-code")
        wait_zip_code_field = self.wait.until(EC.element_to_be_clickable(zip_code_field_locator))
        wait_zip_code_field.click()
        wait_zip_code_field.clear()
        wait_zip_code_field.send_keys(zip_code)

        continue_button=self.selenium_driver.find_element(By.ID, "continue")
        continue_button.click()
    
    def verification_checkout_overview_title(self):
        checkout_overview_locator=(By.XPATH, "//span[@class='title']")
        wait_checkout_overview_field= self.wait.until(EC.presence_of_element_located(checkout_overview_locator))

        checkout_overview_locator= wait_checkout_overview_field.text
        assert checkout_overview_locator== "Checkout: Overview"
    

    def verification_products_in_checkout_overview(self):
        product_1_name=self.selenium_driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div[@class='inventory_item_name']")
        product_2_name= self.selenium_driver.find_element(By.XPATH, "//a[@id='item_0_title_link']/div[@class='inventory_item_name']")

        assert product_1_name.text=="Sauce Labs Backpack"
        assert product_2_name.text=="Sauce Labs Bike Light"


    def click_to_finish_button(self):
        finish_button_locator= self.selenium_driver.find_element(By.ID, "finish")
        finish_button_locator.click()

    
    def verification_checkout_complete_title(self):
        checkout_complete_locator = (By.XPATH, "//span[@class='title' and text()='Checkout: Complete!']")
        wait_checkout_complete_field = self.wait.until(EC.presence_of_element_located(checkout_complete_locator))

        checkout_complete_text = wait_checkout_complete_field.text
        expected_title = "Checkout: Complete!"
        assert checkout_complete_text == expected_title

    
    def click_on_the_menu_button(self):
        menu_button_locator= (By.ID, "react-burger-menu-btn")
        wait_menu_button_locator=self.wait.until(EC.element_to_be_clickable(menu_button_locator))

        wait_menu_button_locator.click()

    
    def click_on_the_logout_button(self):
        logout_locator=(By.ID, "logout_sidebar_link")
        wait_logout_locator=self.wait.until(EC.element_to_be_clickable(logout_locator))

        wait_logout_locator.click()

    
    def verification_of_login_page(self):
        expected_title = "Swag Labs"
        actual_title = self.selenium_driver.title
        assert actual_title == expected_title
        








    





        
        

    