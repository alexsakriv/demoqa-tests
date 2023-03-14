from selene.support.shared import browser


def given_opened():
    browser.open('https://demoqa.com/automation-practice-form')


def input_info(firstName, lastName, userEmail, userNumber, address):
    browser.element('#firstName').type(firstName)
    browser.element('#lastName').type(lastName)
    browser.element('#userEmail').type(userEmail)
    browser.element('#userNumber').type(userNumber)
    browser.element('#currentAddress').type(address)
