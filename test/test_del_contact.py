from model.contact import Contact
def test_delete_contact(app):
    app.contact.delete()
    app.contact.return_homepage()