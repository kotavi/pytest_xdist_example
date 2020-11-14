import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExampleTwo:

    def test_input_form(self):
        print("Another example")
        yes_no_form = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "at-cv-lightbox-header")))
        if yes_no_form:
            no_btn = self.driver.find_element_by_xpath("//div/a[contains(text(), 'No, thanks!')]")
            no_btn.click()
        main_menu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Input Forms')]")
        main_menu.click()

        sub_menu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Simple Form Demo')]")
        sub_menu.click()

        # Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        elem_user_message = self.driver.find_element_by_id("user-message")

        elem_user_message.clear()
        elem_user_message.send_keys("Test Python")

        # Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        elem_show_msg_btn = self.driver.find_element_by_css_selector('#get-input > .btn')
        elem_show_msg_btn.click()

        # Checking whether the input text and output text are same using assertion.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'display')))
        elem_your_msg = self.driver.find_element_by_id("display")
        assert "Test Python" in elem_your_msg.text

    def test_func_fast(self):
        time.sleep(0.1)

    def test_func_slow1(self):
        time.sleep(0.2)

    def test_func_slow2(self):
        time.sleep(0.3)
