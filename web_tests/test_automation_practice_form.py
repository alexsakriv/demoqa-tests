from selene.support.shared import browser
from selene import have, command
from demoqa_tests import app
import allure
from allure import attachment_type


def test_submit(open_browser):
    # GIVEN
    with allure.step('Открываем главную страницу'):
        app.automation_practice_form.given_opened()
        app.automation_practice_form.remove_ads()

    # WHEN
    with allure.step('Заполняем данные пользователя'):
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

    with allure.step('Нажимаем кнопку "Submit"'):
        app.automation_practice_form.press_submit()


    # THEN
    with allure.step('Проверяем данные на соответствие введеным данным'):
        app.automation_practice_form.then(
            name='Aleksandra Krivoruchenko',
            email='test@test.com',
            gender='Female',
            number='8922121245',
            dateOfBirth='11 December,1997',
            subject='Computer Science',
            hobby='Sports, Reading, Music',
            picture='foto.jpeg',
            address='Tyumen, Moskovskaya Street 42',
            stateAndCity='NCR Noida'
        )
