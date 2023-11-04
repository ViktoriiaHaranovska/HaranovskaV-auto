from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class SignInPage(BasePage):
    URL = 'https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/'

    def __init__(self) -> None:
        BasePage.__init__(self)

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        accept_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".osano-cm-accept-all")))
        accept_btn.click()

        login_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/span[2]/a")))
        login_link.click()

        login_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))
        login_elem.send_keys(username)

        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)

        login_btn = self.driver.find_element(By.ID, "login")
        login_btn.click()

    def check_nickname(self,expected_nickname):
        nickname_elem = self.driver.find_element(By.CLASS_NAME, "home-username-link")
        actual_nickname = nickname_elem.text
        return actual_nickname == expected_nickname

    def style_change(self, expected_theme):
        settings_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sb > div.nav-menu-area > a")))
        settings_btn.click()


        themes_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#vue-instance > div.v5-section.v5-overflow-hidden > a:nth-child(3)")))
        themes_btn.click()


        new_theme_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.base-layout > div.base-container > main > div.layout-column-two > div.v5-section > div > div.settings-themes-theme-preview.settings-themes-theme-hover.settings-themes-bubblegum")))
        new_theme_btn.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div.base-layout > div.base-container > main > div.layout-column-two > div.v5-section > div > div.settings-themes-theme-preview.settings-themes-default-theme")))

        theme_elem = self.driver.find_element(By.CSS_SELECTOR, "body > div.base-layout > div.base-container > main > div.layout-column-two > div.v5-section > div > div.settings-themes-theme-preview.settings-themes-default-theme")
        actual_theme = theme_elem.get_attribute('style')
        print(f"Actual theme: {actual_theme}")
        return actual_theme == expected_theme

    def start_a_new_game(self):
        new_game_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "v5-section-shadow-hover.play-quick-links-link")))
        new_game_btn.click()

        resign_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#board-layout-sidebar > div > div.tab-content-component > div.live-game-buttons-component > button.resign-button-component")))
        resign_btn.click()

        resign_approve_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#board-layout-sidebar > div > div.tab-content-component > div.live-game-buttons-component > button.resign-button-component > div > button.ui_v5-button-component.ui_v5-button-primary.ui_v5-button-small")))
        resign_approve_btn.click()


        

        