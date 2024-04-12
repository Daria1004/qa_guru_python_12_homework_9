from qa_guru_python_12_homework_9.model.user import test_user
from qa_guru_python_12_homework_9.model.registration_page import RegistrationPage


def test_complete_todo(browser_management):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.register(test_user)

    registration_page.submit()

    registration_page.should_have_registered(test_user)
