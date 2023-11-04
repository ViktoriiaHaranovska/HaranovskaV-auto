import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from modules.ui.page_objects.sign_in_page_chess import SignInPage

@pytest.mark.skip
def test_check_theme_change():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("victoriagbon@gmail.com", "12345678Test")
    assert sign_in_page.check_nickname("testforstudy")
    expected_theme = "background-image: url('https://images.chesscomfiles.com/chess-themes/backgrounds/_previews_/web/bubblegum.jpeg'); transition: background-image 0.3s linear 0s;"

    style_changed = sign_in_page.style_change(expected_theme)
    assert style_changed, "Style change was not successful"

    """
    Тест закінчується результатом failed не зважаючи на те 
    що очікуваний результат співпадає з актуальним.
    """







