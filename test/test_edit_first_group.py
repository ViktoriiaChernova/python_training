from model.group import Group

def test_edit_group(app):
    app.group.edit_first_group(Group(name="edited", header="edited", footer="edited"))

def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="edited"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="edited"))