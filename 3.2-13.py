import unittest
from selenium import webdriver
import time

def reg(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(".form-control.first:required").send_keys("Мasha")
        browser.find_element_by_css_selector(".form-control.second:required").send_keys("Мedvedeva")
        browser.find_element_by_css_selector(".form-control.third:required").send_keys("Мmm")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        return welcome_text_elt.text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
welcome_text = "Congratulations! You have successfully registered!"

class TestsForPages(unittest.TestCase):
    def test_page1(self):
        self.assertEqual(reg(link1), welcome_text)

    def test_page2(self):
        self.assertEqual(reg(link2), welcome_text)


if __name__ == "__main__":
    unittest.main()