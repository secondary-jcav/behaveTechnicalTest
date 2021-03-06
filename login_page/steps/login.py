from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Steps defined in login.feature are implemented here
START_URL = "URL goes here"
START_URL_TITLE = "Page title"


@given("login page can be reached")
def open_login_page(context):
    driver = context.browser
    driver.get(START_URL)
    try:
        WebDriverWait(driver, 10).until(EC.title_is(START_URL_TITLE))
    except TimeoutException:
        raise AssertionError(f"Page title is {driver.title}")


@given("user inputs name & password")
def enter_credentials(context):
    driver = context.browser
    try:
        username_input = driver.find_element_by_name("username")
        password_input = driver.find_element_by_name("password")
    except NoSuchElementException as e:
        raise AssertionError(e)
    username_input.send_keys("ihifhfw@gmail.com")
    password_input.send_keys("eoittnif")


@when("user clicks login")
def click_login_button(context):
    driver = context.browser
    try:
        # login_button = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[2]/form/button')
        login_button = driver.find_element_by_xpath('//*[@data-id="submit-login"]')
        login_button.click()
    except NoSuchElementException as e:
        print("login button can't be found")
        raise e


@then("user remains in the same page")
def failed_login(context):
    driver = context.browser
    assert driver.current_url == "Page Titl", f"User has navigated to {driver.current_url}"


@then(u'page goes to reset password')
def check_reset_page(context):
    driver = context.browser
    try:
        WebDriverWait(driver, 10).until(EC.url_contains("forgotPassword"))
    except TimeoutException:
        raise AssertionError(f"Page title is {driver.title}")


@when(u'user clicks on forgot password')
def click_on_forgot_password(context):
    driver = context.browser
    try:
        forgot_password_button = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[2]/form/div[3]/a')
        forgot_password_button.click()
    except NoSuchElementException as e:
        raise AssertionError(e)


@when(u'user inputs email')
def user_email_input(context):
    driver = context.browser
    try:
        user_input = driver.find_element_by_name("username")
        user_input.send_keys("example_email@gmail.com")
    except NoSuchElementException as e:
        raise AssertionError(e)


@when(u'user inputs password')
def user_password_input(context):
    driver = context.browser
    try:
        password_input = driver.find_element_by_name("password")
        password_input.send_keys("eoittnif")
    except NoSuchElementException as e:
        raise AssertionError(e)


@when(u'user clicks on reset request button')
def click_on_reset(context):
    driver = context.browser
    reset_button = driver.find_element_by_css_selector('.simple-btn--login')
    reset_button.click()


@then(u'page displays email sent message')
def check_feedback_page(context):
    driver = context.browser
    feedback_template = "Please check your inbox and follow the instructions to reset your password"
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login__feedback-message")))
        feedback_message = driver.find_element_by_css_selector('.login__feedback-message')
        assert feedback_template in feedback_message.text, f"{feedback_message.text}"
    except NoSuchElementException as e:
        raise AssertionError(e)


@when(u'user clicks on free trial link')
def click_free_trial_link(context):
    driver = context.browser
    try:
        free_trial_link = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div[3]/a')
        free_trial_link.click()
    except NoSuchElementException as e:
        raise AssertionError(e)


@then(u'page navigates to free trial section')
def check_free_trial_section(context):
    driver = context.browser
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Start Free"))
    except TimeoutException:
        raise AssertionError(f"Page title is {driver.title}")



