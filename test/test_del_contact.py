import random
from model.contact import Contact

def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.open_new_contact_form()
        app.contact.create(Contact(firstname="ghgfhg", middlename="jhjhjhj", lastname="jhjjgjhg", nickname="jghjjhggh", title="jghgjjhjgh", company="jjhghjjh", address="jghgjhgjhgjh",
                               home_phone="676767", mobile_phone="676767", work_phone="766767", fax="6776767", email="fggfgff", email2="gfgfgffg", email3="gffgffg", homepage="gfgffggfgf",
                               bday="29", bmonth="September", byear="1989", aday="19", amonth="February", ayear="1989"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    app.contact.return_homepage()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)