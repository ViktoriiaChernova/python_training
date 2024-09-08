from model.contact import Contact
def test_edit_contact(app):
    app.contact.edit(Contact(firstname="edited", middlename="edited", lastname="edited", nickname="edited", title="edited", company="edited", address="edited",
                               home_phone="edited", mobile_phone="edited", work_phone="edited", fax="edited", email="edited", email2="edited", email3="edited", homepage="edited",
                               bday="29", bmonth="September", byear="1989", aday="19", amonth="February", ayear="1989"))
    app.contact.return_homepage()