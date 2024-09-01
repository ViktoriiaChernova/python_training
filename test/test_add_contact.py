# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_new_contact_form()
    app.contact.create(Contact(firstname="ghgfhg", middlename="jhjhjhj", lastname="jhjjgjhg", nickname="jghjjhggh", title="jghgjjhjgh", company="jjhghjjh", address="jghgjhgjhgjh",
                               home_phone="676767", mobile_phone="676767", work_phone="766767", fax="6776767", email="fggfgff", email2="gfgfgffg", email3="gffgffg", homepage="gfgffggfgf",
                               bday="29", bmonth="September", byear="1989", aday="19", amonth="February", ayear="1989"))
    app.contact.return_homepage()
    app.session.logout()
