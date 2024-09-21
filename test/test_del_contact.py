from model.contact import Contact
from random import randrange
def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.open_new_contact_form()
        app.contact.create(Contact(firstname="ghgfhg", middlename="jhjhjhj", lastname="jhjjgjhg", nickname="jghjjhggh", title="jghgjjhjgh", company="jjhghjjh", address="jghgjhgjhgjh",
                               home_phone="676767", mobile_phone="676767", work_phone="766767", fax="6776767", email="fggfgff", email2="gfgfgffg", email3="gffgffg", homepage="gfgffggfgf",
                               bday="29", bmonth="September", byear="1989", aday="19", amonth="February", ayear="1989"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.contact.return_homepage()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts