import os

from selene import browser, have, be, command

from qa_guru_python_12_homework_9.model.user import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.text-center').should(have.text('Practice Form'))

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_gender(user.gender.value)
        self.fill_mobile(user.mobile)
        self.fill_date_of_birth(user.year, user.month, user.day)
        self.fill_subjects(user.subjects.value)
        self.fill_hobbies(user.hobbies.value)
        self.fill_picture(user.picture)
        self.fill_current_address(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)

    def should_have_registered(self, user: User):
        self.should_registered_user_with(
            user.first_name,
            user.last_name,
            user.email,
            user.gender.value,
            user.mobile,
            f'{user.day} {user.month},{user.year}',
            user.subjects.value,
            user.hobbies.value,
            user.picture,
            user.current_address,
            user.state,
            user.city
        )

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).set_value(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).set_value(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).set_value(value)

    def fill_gender(self, value):
        browser.all('[name="gender"]').element_by(have.value(value)).element('..').click()

    def fill_mobile(self, value):
        browser.element('#userNumber').set_value(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.all('.react-datepicker__month-select>option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{day.zfill(3)}').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').set_value(value).press_enter()

    def fill_hobbies(self, value):
        browser.all('#hobbiesWrapper label').element_by(have.exact_text(value)).element('..').perform(command.js.scroll_into_view).click()

    def fill_picture(self, file):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'resources/{file}'))

    def fill_current_address(self, value):
        browser.element('#currentAddress').set_value(value)

    def fill_state(self, value):
        browser.element('#react-select-3-input').set_value(value).press_enter()

    def fill_city(self, value):
        browser.element('#react-select-4-input').set_value(value).press_enter()

    def submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_registered_user_with(self, first_name, last_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture, current_address, state, city):
        browser.element('table>tbody>tr:nth-child(1)>td:nth-child(2)').should(have.text(f'{first_name} {last_name}'))
        browser.element('table>tbody>tr:nth-child(2)>td:nth-child(2)').should(have.text(email))
        browser.element('table>tbody>tr:nth-child(3)>td:nth-child(2)').should(have.text(gender))
        browser.element('table>tbody>tr:nth-child(4)>td:nth-child(2)').should(have.text(mobile))
        browser.element('table>tbody>tr:nth-child(5)>td:nth-child(2)').should(have.text(date_of_birth))
        browser.element('table>tbody>tr:nth-child(6)>td:nth-child(2)').should(have.text(subjects))
        browser.element('table>tbody>tr:nth-child(7)>td:nth-child(2)').should(have.text(hobbies))
        browser.element('table>tbody>tr:nth-child(8)>td:nth-child(2)').should(have.text(picture))
        browser.element('table>tbody>tr:nth-child(9)>td:nth-child(2)').should(have.text(current_address))
        browser.element('table>tbody>tr:nth-child(10)>td:nth-child(2)').should(have.text(f'{state} {city}'))
