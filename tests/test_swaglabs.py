from pages.home_page import HomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")
    home_page.verification_products_title()
    home_page.adding_two_products_to_cart()
    home_page.verification_your_cart_title()
    home_page.verification_products_in_the_chart()
    home_page.click_on_the_checkout()
    home_page.filling_the_fields("Lamija", "Mezit", "88400")
    home_page.verification_checkout_overview_title()
    home_page.verification_products_in_checkout_overview()
    home_page.click_to_finish_button()
    home_page.verification_checkout_complete_title()
    home_page.click_on_the_menu_button()
    home_page.click_on_the_logout_button()
    home_page.verification_of_login_page()
