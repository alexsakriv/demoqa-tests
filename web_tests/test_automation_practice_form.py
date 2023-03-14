from selene.support.shared import browser
from selene import have
from demoqa_tests import app


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

    app.radiobutton.select(
        type='gender',
        value='Female'
    )

    app.datepicker.select(
        date_type='dateOfBirthInput',
        month='December',
        year='1997',
        day='11'
    )

    app.dropdown.select(
        input_data='computer',
        select_data='Computer Science'
    )

    app.checkbox.select(
        type='hobbies',
        value='Sports'
    )
    app.checkbox.select(
        type='hobbies',
        value='Reading'
    )
    app.checkbox.select(
        type='hobbies',
        value='Music'
    )

    app.uploadPicture.select(
        name='foto.jpeg'
    )

    app.automation_practice_form.select_state_and_city(
        state='NCR',
        city='Noida'
    )

    app.automation_practice_form.press_submit()

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