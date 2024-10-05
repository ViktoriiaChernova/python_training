# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_year():
    year = random.randint(1000, 3000)
    return str(year)

def random_day():
    day = random.randint(1, 31)
    return str(day)

def random_month():
    months = [
        "-", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return random.choice(months)

def random_phone(maxlen):
    symbols = string.digits + " " + "(" + ")" + "+"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="",
                       mobile_phone="", work_phone="", fax="", email="", email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-",
                       amonth="-", ayear="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                lastname=random_string("lastname", 10), nickname=random_string("lastname", 10),
                    title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 10),
                        home_phone=random_phone(15), mobile_phone=random_phone(15), work_phone=random_phone(15), fax=random_phone(15), email=random_string("email", 10),
                            email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homepage", 10),
                               bday=random_day(), bmonth=random_month(), byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year())
    for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_new_contact_form()
    app.contact.create(contact)
    app.contact.return_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)