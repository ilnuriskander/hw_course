# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
browser = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
try:
    browser.maximize_window()
    browser.get(sbis_site)
    time.sleep(2)
    user_login, user_password = 'autotest_cours_11', 'autotest_cours_11autotest_cours_11'
    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    time.sleep(2)
    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    time.sleep(7)
    contacts_1 = browser.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1')
    contacts_1.click()
    time.sleep(2)
    contacts_2 = browser.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default')
    contacts_2.click()
    time.sleep(2)
    new_message = browser.find_element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-default controls-icon icon-RoundPlus"]')
    new_message.click()
    time.sleep(6)
    find_employer = browser.find_element(By.CSS_SELECTOR, '[class="controls-StackTemplate-content"] [class="controls-Field js-controls-Field controls-InputBase__nativeField controls-Search__nativeField_caretEmpty controls-Search__nativeField_caretEmpty_theme_default   controls-InputBase__nativeField_hideCustomPlaceholder"]')
    find_employer.send_keys('Курс Автотест')
    time.sleep(2)
    employer_button = browser.find_element(By.CSS_SELECTOR, '.person-BaseInfo.ws-flexbox')
    employer_button.click()
    time.sleep(3)
    pole_massage = browser.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field.textEditor_slate_Container')
    massage_text = 'тестовое сообщение ' + time.strftime('%Y-%m-%d %H:%M:%S')
    pole_massage.send_keys(massage_text)
    send = browser.find_element(By.CSS_SELECTOR, '.controls-Button__icon.controls-BaseButton__icon.controls-icon_size-s.controls-icon_style-contrast.controls-icon.icon-BtArrow')
    send.click()
    time.sleep(3)
    massage = browser.find_element(By.CSS_SELECTOR, '.msg-entity-text.msg-entity_font_croppless.richEditor_richContentRender_fontSize-m_theme-default')
    assert massage.is_displayed(), 'Сообщение не получено'
    assert massage.text == massage_text, 'Текст сообщения не соответсвует отправленному'
    action_chains = ActionChains(browser)
    action_chains.move_to_element(massage)
    action_chains.context_click(massage)
    action_chains.perform()
    delete_message = browser.find_element(By.CSS_SELECTOR, '.controls-icon_size-m.controls-icon_style-danger.icon-Erase.controls-icon.controls-Menu__icon.controls-Menu__icon_m-left')
    delete_message.click()
    time.sleep(3)
    try:
        massage.is_displayed()
    except:
        pass
    else:
        raise Exception('Сообщение не удалено')
finally:
    browser.quit()
