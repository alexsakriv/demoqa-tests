import os
from selene.support.shared import browser
from selene import command, have
import web_tests
from demoqa_tests.model import app


def test_submit(open_browser):
    # GIVEN
    app.automation_practice_form.given_opened()

    # WHEN
    app.automation_practice_form.input_info(
        firstName='Aleksandra',
        lastName='Krivoruchenko',
        userEmail='test@test.com',
        userNumber='8922121245',
        address='Tyumen, Moskovskaya Street 42'
    )

    app.radiobutton.select(type='gender', value='Female')

    app.datepicker.select(
        date_type='dateOfBirthInput',
        month='December',
        year='1997',
        day='11'
    )

    app.dropdown.select(input_data='computer', select_data='Computer Science')

    app.checkbox.select(type='hobbies', value='Sports')
    app.checkbox.select(type='hobbies', value='Reading')
    app.checkbox.select(type='hobbies', value='Music')

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(web_tests.__file__), 'resources/foto.jpeg')
        )
    )

    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Noida')).perform(command.js.click)

    browser.element('#submit').press_enter()

    # THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Aleksandra Krivoruchenko',
            'test@test.com',
            'Female',
            '8922121245',
            '11 December,1997',
            'Computer Science',
            'Sports, Reading, Music',
            'foto.jpeg',
            'Tyumen, Moskovskaya Street 42',
            'NCR Noida',
        )
    )