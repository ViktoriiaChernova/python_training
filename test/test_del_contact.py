from model.contact import Contact
def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.contact.return_homepage()
    app.session.logout()