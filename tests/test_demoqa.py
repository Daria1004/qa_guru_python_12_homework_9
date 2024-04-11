from qa_guru_python_12_homework_9.model.registration_page import RegistrationPage


def test_complete_todo(browser_management):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Ivan')

    registration_page.fill_last_name('Durian')

    registration_page.fill_email('ID@gmail.com')

    registration_page.fill_gender('Other')

    registration_page.fill_mobile('1234512345')

    registration_page.fill_date_of_birth('1900', 'May', '10')

    registration_page.fill_subjects('Computer Science')

    registration_page.fill_hobbies('Music')

    registration_page.fill_picture('clover.jpg')

    registration_page.fill_current_address('Thailand, Phuket')

    registration_page.fill_state('Haryana')

    registration_page.fill_city('Panipat')

    registration_page.submit()

    registration_page.should_registered_user_with(
        'Ivan',
        'Durian',
        'ID@gmail.com',
        'Other',
        '1234512345',
        '10 May,1900',
        'Computer Science',
        'Music',
        'clover.jpg',
        'Thailand, Phuket',
        'Haryana',
        'Panipat'
    )
