from model.contact import Contact
import re

def test_info_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
    db_contacts_dict = {contact.id: contact for contact in contact_from_db}
    for home_contact in contact_from_home_page:
        db_contact = db_contacts_dict.get(home_contact.id)
        assert home_contact.all_phones_from_home_page == merge_phones_like_on_home_page(db_contact)
        assert home_contact.all_emails_from_home_page == merge_emails_like_on_home_page(db_contact)
        assert home_contact.firstname == db_contact.firstname
        assert home_contact.lastname == db_contact.lastname
        assert home_contact.address == db_contact.address

def clear(s):
    return re.sub("[() -]", "", s)
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="" and x is not None,
                            [contact.email, contact.email2, contact.email3]))


