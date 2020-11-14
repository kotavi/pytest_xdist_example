import time

import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        assert "Selenium Easy" in self.driver.title

    def test_content_text(self):
        print("Verify content on the page")
        center_text = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == center_text

    def test_bootstrap_bar(self):
        print("Lets try with another example")
        yes_no_form = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "at-cv-lightbox-header")))
        if yes_no_form:
            no_btn = self.driver.find_element_by_xpath("//div/a[contains(text(), 'No, thanks!')]")
            no_btn.click()

        main_menu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Progress Bars')]")
        main_menu.click()

        sub_menu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Bootstrap Progress bar')]")
        sub_menu.click()

        btn_download = self.driver.find_element_by_xpath("//button[contains(text(), 'Download')]")
        # btn_download = self.driver.find_element_by_id("cricle-btn")
        print(btn_download.text)
        btn_download.click()  # TODO: doesn't click
        time.sleep(5)
        slice_class = self.driver.find_element_by_class_name("slice")
        style_attr = slice_class.get_attribute("style")
        assert "none" not in style_attr, "{}".format(style_attr)

        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element_value((By.ID, 'cricleinput'), "105"))

        elem_value = self.driver.find_element_by_id("cricleinput")
        # <input type="hidden" id="cricleinput" value="105">
        elem_attribute_value = elem_value.get_attribute('value')
        assert elem_attribute_value == "105"

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert len(x) == 5

    def test_three(self):
        x = "welcome"
        assert "one" not in x
