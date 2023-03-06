import os
from selene.support.shared import browser
from selene import have, command, be

browser.config.hold_browser_open = True
browser.config.click_by_js = True


def test_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Bob')
    browser.element('#lastName').should(be.blank).type('By')
    browser.element('#userEmail').should(be.blank).type('email@email.email')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="2"]').should(have.text('March')).click()
    browser.element('.react-datepicker__year-select option[value="2023"]').should(have.text('2023')).click()
    browser.element('.react-datepicker__day--020').should(have.text('20')).click()
    browser.element('#subjectsInput').should(be.blank).type('physics').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/picture/VYqbjvKLSlU.jpg')
    browser.element('#currentAddress').should(be.blank).type('address')
    browser.element('#react-select-3-input').should(be.blank).type('Haryana').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Karnal').press_enter()
    browser.element('#submit').perform(command.js.click)

    # Проверяем введенные данные
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tr').element_by_its('td', have.text('Student Name')).all('td')[1].should(have.text('Bob By'))
    browser.all('tr').element_by_its('td', have.text('Student Email')).all('td')[1].should(have.text(
        'email@email.email'))
    browser.all('tr').element_by_its('td', have.text('Gender')).all('td')[1].should(have.text('Male'))
    browser.all('tr').element_by_its('td', have.text('Mobile')).all('td')[1].should(have.text('1234567890'))
    browser.all('tr').element_by_its('td', have.text('Date of Birth')).all('td')[1].should(have.text('20 March,2023'))
    browser.all('tr').element_by_its('td', have.text('Subjects')).all('td')[1].should(have.text('Physics'))
    browser.all('tr').element_by_its('td', have.text('Hobbies')).all('td')[1].should(have.text('Reading'))
    browser.all('tr').element_by_its('td', have.text('picture')).all('td')[1].should(have.text('VYqbjvKLSlU.jpg'))
    browser.all('tr').element_by_its('td', have.text('Address')).all('td')[1].should(have.text('address'))
    browser.all('tr').element_by_its('td', have.text('State and City')).all('td')[1].should(have.text('Haryana Karnal'))
    browser.element('#closeLargeModal').click()
