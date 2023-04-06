# demoqa-tests

UI тест написан на проверку формы заполнения регистрационных данных: https://demoqa.com/automation-practice-form

Тест включает заполнение данных и последующую проверку данных на соответствие ранее введеным

## <img width="30px" title="Jenkins" src="https://user-images.githubusercontent.com/118905261/230335250-74a96dcc-6029-423c-9faf-f4551b7a9448.png"> Запуск проекта в Jenkins

[Ссылка на сборку](https://jenkins.autotests.cloud/job/alexsakriv_qa_guru_python_3_10/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 40 54" src="https://user-images.githubusercontent.com/118905261/230338674-724129f4-3e2e-4faa-bdb5-bd7156b0ac06.png">

##### После сборки тестов формируется Allure отчет. Открыть его можно нажав на иконку  <img width="10px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png">

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 41 10" src="https://user-images.githubusercontent.com/118905261/230338695-2eeb419c-fd23-4f21-ac39-71261fe612f4.png">

## <img width="30px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png"> Allure отчет

Вкладка "Overview" включает себя отчет по тесту, дату прохождения теста и затраченное время на прохождение теста

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 27" src="https://user-images.githubusercontent.com/118905261/230340031-95d63f15-8c50-460e-92dd-671ea37af2fa.png">

На вкладке "Suites" можно найти подробную ифнормацию о тесте: предусловия, шаги теста и вложения (скриншот, видео и логи)

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 45" src="https://user-images.githubusercontent.com/118905261/230340065-bd50f0b7-cc5e-4005-a0c2-4569a4caae51.png">
