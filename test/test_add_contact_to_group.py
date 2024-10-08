from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

def test_add_contact_to_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_contact_list()) == 0:
        app.contact.open_new_contact_form()
        app.contact.create(Contact(firstname="ghgfhg", middlename="jhjhjhj", lastname="jhjjgjhg", nickname="jghjjhggh", title="jghgjjhjgh", company="jjhghjjh", address="jghgjhgjhgjh",
                               home_phone="676767", mobile_phone="676767", work_phone="766767", fax="6776767", email="fggfgff", email2="gfgfgffg", email3="gffgffg", homepage="gfgffggfgf",
                               bday="29", bmonth="September", byear="1989", aday="19", amonth="February", ayear="1989"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = random.choice(db.get_contact_list())
    c_id = contact.id
    g_id = random.choice(db.get_group_list()).id
    contacts_in_group_before_adding = db.get_contacts_in_group(Group(id=g_id))
    app.contact.add_contact_to_group_by_id(c_id, g_id)
    contacts_in_group_after_adding = db.get_contacts_in_group(Group(id=g_id))
    contacts_in_group_before_adding.append(contact)
    assert sorted(contacts_in_group_before_adding, key=Contact.id_or_max) == sorted(contacts_in_group_after_adding, key=Contact.id_or_max)