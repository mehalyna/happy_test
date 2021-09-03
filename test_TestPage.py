from GooglePages import SearchHelper

def test_google_search(browser):
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word("Python")
    google_main_page.click_on_the_search_button()
    google_main_page.check_navigation_bar()
    
    assert True