from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New_firstname"))


def test_modify_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test"))
    app.contact.modify_first_contact(Contact(middlename="New_middlename"))
