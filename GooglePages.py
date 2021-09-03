from BaseApp import BasePage
from selenium.webdriver.common.by import By

class GoogleSearchLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.NAME, "q")
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.NAME, "btnK")
    LOCATOR_GOOGLE_NAVIGATION_BAR = (By.XPATH, "//div[@class='g']//a[not(@class)]")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_BUTTON,time=600).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(GoogleSearchLocators.LOCATOR_GOOGLE_NAVIGATION_BAR,time=600)
        #searchText_google_suggestion = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//form[@action='/search' and @role='search']//ul[@role='listbox']//li//span")))
        ref_list = []
        for item in all_list:
            ref_list.add(item.get_attribute("href"))
        return ref_list