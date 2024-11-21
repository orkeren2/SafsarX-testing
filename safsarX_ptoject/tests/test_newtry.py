import time
from utils.tetingphone import get_latest_sms
from Pages.Login_page import LoginPage as LP
from data import TestData as TD


def test_login(driver):
    lp = LP(driver)
    driver.get(lp.loginPage_baseUrl)
    loginbutton = lp.find_element(LP.loginbutton_locator)
    loginbutton.click()
    input_phone = lp.find_element(lp.input_phone_locator)
    input_phone.send_keys(TD.test_case_1_phone_number)
    enter_button = lp.find_element(lp.enter_button_locator)
    enter_button.click()
    time.sleep(3)

    # --- Integrate SMS code retrieval and entry ---
    sms_code = get_latest_sms()
    print(sms_code)
    if sms_code:
        print(f"Extracted SMS code: {sms_code}")
        input_sms_code = lp.find_element(lp.input_sms_locator)
        input_sms_code.send_keys(sms_code)  # Use send_keys to enter the code
        time.sleep(2)

        confirmbtn =lp.find_element(lp.confirmbtn_locator)
        confirmbtn.click()
        time.sleep(15)

    else:
        print("Failed to fetch the latest SMS.")
    # ---------------------------------------------

if __name__ == '__main__':
    test_login()