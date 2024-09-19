from model.contact import Contact
def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.open_new_contact_form()
        app.contact.create(Contact(firstname="ghgfhg", middlename="jhjhjhj", lastname="jhjjgjhg", nickname="jghjjhggh",
                                   title="jghgjjhjgh", company="jjhghjjh", address="jghgjhgjhgjh",
                                   home_phone="676767", mobile_phone="676767", work_phone="766767", fax="6776767",
                                   email="fggfgff", email2="gfgfgffg", email3="gffgffg", homepage="gfgffggfgf",
                                   bday="29", bmonth="September", byear="1989", aday="19", amonth="February",
                                   ayear="1989"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="edited", middlename="edited", lastname="edited", nickname="edited", title="edited", company="edited", address="edited",
                               home_phone="edited", mobile_phone="edited", work_phone="edited", fax="edited", email="edited", email2="edited", email3="edited", homepage="edited",
                               bday="29", bmonth="September", byear="1989", aday="19", amonth="February", ayear="1989")
    contact.id = old_contacts[0].id
    app.contact.edit(contact)
    app.contact.return_homepage()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=lambda contact: contact.id_or_max()) == sorted(new_contacts, key=lambda contact: contact.id_or_max())