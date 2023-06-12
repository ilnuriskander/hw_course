# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    browser.get(sbis_site)
    contacts = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1.mh-8')
    contacts.click()
    tensor_button = browser.find_element(By.CSS_SELECTOR, '.pt-32.pb-16 .sbisru-Contacts__logo-tensor.mb-8')
    tensor_button.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    block_sila = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert block_sila.is_displayed(), 'Блок "Сила в людях" не отображается'
    podrobnee = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    podrobnee.location_once_scrolled_into_view
    podrobnee.click()
    assert browser.current_url == 'https://tensor.ru/about'

finally:
    browser.quit()



