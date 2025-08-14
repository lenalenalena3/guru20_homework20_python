from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_check_title_pages():
    text_1_page = "The Free Encyclopedia\n…in over 300 languages"
    with step('Проверка главной страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text(text_1_page))

    text_2_page = "New ways to explore"
    with step(f'Проверка страницы {text_2_page}'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text(text_2_page))

    text_3_page = "Reading lists with sync"
    with step(f'Проверка страницы {text_3_page}'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text(text_3_page))

    text_4_page = "Data & Privacy"
    with step(f'Проверка страницы страницы {text_4_page}'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text(text_4_page))
