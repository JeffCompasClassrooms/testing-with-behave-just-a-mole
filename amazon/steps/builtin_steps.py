from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@given("I open the Amazon home page")
def step_open_amazon(context):
    context.behave_driver.get("https://www.amazon.com/")

@then("I expect the Amazon logo to be visible")
def step_verify_logo(context):
    wait = WebDriverWait(context.behave_driver, 10)
    logo = wait.until(EC.visibility_of_element_located((By.ID, "nav-logo-sprites")))
    assert logo.is_displayed()

@when('I search for "video games"')
def step_search_item(context):
    wait = WebDriverWait(context.behave_driver, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("video games")
    search_box.send_keys(Keys.RETURN)

@then('I expect the results text to contain "Popular Shopping Ideas"')
def step_verify_results_text(context):
    wait = WebDriverWait(context.behave_driver, 10)
    xpath = f"//*[contains(text(), 'Popular Shopping Ideas')]"
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    assert element.is_displayed()

@when('I search for "HDMI Cable"')
def step_search_item(context):
    wait = WebDriverWait(context.behave_driver, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("HDMI Cable")
    search_box.send_keys(Keys.RETURN)

@when("I select the first result")
def step_select_first_result(context):
    wait = WebDriverWait(context.behave_driver, 10)
    first_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".s-main-slot .s-result-item .s-image")))
    first_item.click()

@when("I click the add to cart button")
def step_add_to_cart(context):
    wait = WebDriverWait(context.behave_driver, 10)
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    add_btn.click()

@then('I expect the cart count to be "1"')
def step_verify_cart_count_one(context):
    wait = WebDriverWait(context.behave_driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, "nav-cart-count"), "1"))
    cart_count_element = context.behave_driver.find_element(By.ID, "nav-cart-count")
    assert cart_count_element.text == "1"

@when("I click the cart button")
def step_click_cart(context):
    wait = WebDriverWait(context.behave_driver, 10)
    cart_icon = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
    cart_icon.click()

@then("I expect to see the subtotal")
def step_verify_subtotal(context):
    wait = WebDriverWait(context.behave_driver, 10)
    subtotal_label = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Subtotal')]")))
    assert subtotal_label.is_displayed()

@when("I click the language settings")
def step_click_lang_settings(context):
    wait = WebDriverWait(context.behave_driver, 10)
    lang_menu = wait.until(EC.element_to_be_clickable((By.ID, "icp-nav-flyout")))
    lang_menu.click()

@when("I select Spanish")
def step_select_spanish(context):
    wait = WebDriverWait(context.behave_driver, 10)
    spanish_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'español')]")))
    spanish_option.click()

@when("I save the language changes")
def step_save_lang(context):
    wait = WebDriverWait(context.behave_driver, 10)
    save_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#icp-save-button .a-button-input")))
    save_btn.click()

@then("I expect the navigation to be in Spanish")
def step_verify_spanish(context):
    wait = WebDriverWait(context.behave_driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Hola')]")))

@when("I select English as the language")
def step_select_english(context):
    wait = WebDriverWait(context.behave_driver, 10)
    english_opt = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'English')]")))
    english_opt.click()

@then("I expect the navigation to be in English")
def step_verify_english(context):
    wait = WebDriverWait(context.behave_driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Hello')]")))

@when('I search for "Toy"')
def step_search_hdmi(context):
    wait = WebDriverWait(context.behave_driver, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("Toy")
    search_box.send_keys(Keys.RETURN)

@when("I click the delete button")
def step_click_delete(context):
    wait = WebDriverWait(context.behave_driver, 10)
    delete_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Delete']")))
    delete_btn.click()

@then("I expect the cart to have 1 item")
def step_verify_empty(context):
    wait = WebDriverWait(context.behave_driver, 10)
    cart_count = context.behave_driver.find_element(By.ID, "nav-cart-count").text
    assert cart_count == "1"

@when('I search for "Coffee Mug"')
def step_search_coffee(context):
    wait = WebDriverWait(context.behave_driver, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("Coffee Mug")
    search_box.send_keys(Keys.RETURN)

@then("I expect to see the product title")
def step_verify_title(context):
    wait = WebDriverWait(context.behave_driver, 10)
    title = wait.until(EC.visibility_of_element_located((By.ID, "productTitle")))
    assert title.is_displayed()

@when("I scroll to the bottom of the page")
def step_scroll_bottom(context):
    context.behave_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@when("I click the Careers link")
def step_click_careers(context):
    wait = WebDriverWait(context.behave_driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Careers")))
    link.click()

@then("I expect to see the Careers page")
def step_verify_careers(context):
    wait = WebDriverWait(context.behave_driver, 10)
    assert "jobs" in context.behave_driver.title.lower() or "careers" in context.behave_driver.title.lower()

@when("I click the sign in button")
def step_click_signin(context):
    wait = WebDriverWait(context.behave_driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.ID, "nav-link-accountList")))
    link.click()

@when("I click Continue without entering email")
def step_click_continue_empty(context):
    wait = WebDriverWait(context.behave_driver, 10)
    cont_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    cont_btn.click()

@then("I expect to see the missing email error")
def step_verify_email_error(context):
    wait = WebDriverWait(context.behave_driver, 10)
    error = wait.until(EC.visibility_of_element_located((By.ID, "empty-claim-alert")))
    assert error.is_displayed()

@when('I search for "fjkdsjkfdsajkfdsakjfdsjk"')
def step_search_gibberish(context):
    wait = WebDriverWait(context.behave_driver, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("fjkdsjkfdsajkfdsakjfdsjk")
    search_box.send_keys(Keys.RETURN)

@then("I expect to see the no results message")
def step_verify_no_results(context):
    wait = WebDriverWait(context.behave_driver, 10)
    msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Need help?')]")))
    assert msg.is_displayed()

@when('I search for "AA Batteries"')
def step_search_batteries(context):
    wait = WebDriverWait(context.behave_driver, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("AA Batteries")
    search_box.send_keys(Keys.RETURN)

@then("I expect the item to be In Stock")
def step_verify_instock(context):
    wait = WebDriverWait(context.behave_driver, 10)
    availability = wait.until(EC.visibility_of_element_located((By.ID, "availability")))
    assert "In Stock" in availability.text

@when("I click the Registry link")
def step_click_registry(context):
    wait = WebDriverWait(context.behave_driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Registry")))
    link.click()

@then("I expect to see the Registry header")
def step_verify_registry(context):
    wait = WebDriverWait(context.behave_driver, 10)
    assert "Registry" in context.behave_driver.title

@when("I click the Gift Cards link")
def step_click_giftcards(context):
    wait = WebDriverWait(context.behave_driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Gift Cards")))
    link.click()

@then("I expect to see the Gift Cards header")
def step_verify_giftcards(context):
    wait = WebDriverWait(context.behave_driver, 10)
    header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src*='Manage_GiftCard_Tiles_Desktop-Redeem']")))
    assert header.is_displayed()

@when("I click the Best Sellers link")
def step_click_bestsellers(context):
    wait = WebDriverWait(context.behave_driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Best Sellers")))
    link.click()

@then("I expect to see the Best Sellers header")
def step_verify_bestsellers(context):
    wait = WebDriverWait(context.behave_driver, 10)
    header = wait.until(EC.visibility_of_element_located((By.ID, "zg_banner_text")))
    assert "Best Sellers" in header.text