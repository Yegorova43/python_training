from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact (Contact(firstname="", middlename="", lastname="",
                                   nickname="",
                                   title="", company="", address="New address", home="",
                                   mobile="", work="", fax="", email="", email2="", email3="", homepage="", address2="",
                                   phone2="", notes="", byear="", ayear="", Bday="", Bmonth="", Aday="", Amonth=""))
    app.session.logout()