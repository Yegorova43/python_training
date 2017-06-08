# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.form_fields import Form_fields


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Form_fields(firstname="Мария", middlename="Александровна", lastname="Егорова",
                                   nickname="Nick",
                                   title="Hello", company="Company", address="Address", home="54",
                                   mobile="89317856906",
                                   work="89216785434", fax="4908894", email="test@mail.ru",
                                   email2="test2@mail.ru",
                                   email3="test3@mail.ru", homepage="Home page", address2="Address2",
                                   phone2="89064452976",
                                   notes="Notes", byear="1988", ayear="2010",
                                   Bday="//div[@id='content']/form/select[1]//option[19]",
                                   Bmonth="//div[@id='content']/form/select[2]//option[4]",
                                   Aday="//div[@id='content']/form/select[3]//option[16]",
                                   Amonth="//div[@id='content']/form/select[4]//option[12]"))
    app.session.logout()