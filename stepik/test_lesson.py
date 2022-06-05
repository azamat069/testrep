from selenium import webdriver
import time
import pytest


# import unittest

# class TestAbs(unittest.TestCase):

def test_abs1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
    last_name.send_keys('Ivanov')
    email = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    email.send_keys('ivan@mail.ru')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!", welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


def test_abs2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
    last_name.send_keys('Ivanov')
    email = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    email.send_keys('ivan@mail.ru')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!", welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


if __name__ == "__main__":
    pytest.main()
