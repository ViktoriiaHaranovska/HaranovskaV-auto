import pytest 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from modules.ui.page_objects.sign_in_page_chess import ChessDotComAutomation

@pytest.mark.ui_chess
def test_check_correct_username_page_object():
    sign_in_page = ChessDotComAutomation()
    sign_in_page.go_to()
    sign_in_page.try_login("victoriagbon@gmail.com","12345678Test")
    assert sign_in_page.check_nickname("testforstudy")
    sign_in_page.close()