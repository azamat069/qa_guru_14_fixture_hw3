from selene import browser, be, have

def test_positive_search_google(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search_google(open_browser):
    text = 'jkbdsfkjsbd jksbdfkjsbd. jksbdfjkbsdfkjbsdf'
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('[class="card-section"]').should(have.text(f'По запросу {text} ничего не найдено.'))


