from model.group import Group
import random

#def test_edit_group(app):
    #if app.group.count() == 0:
       # app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(name="edited", header="edited", footer="edited"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    id = random.choice(old_groups).id
    group = Group(name="edited")
    group.id = id
    app.group.edit_group_by_id(group, id)
    new_groups = db.get_group_list()
    for i, g in enumerate(old_groups):
        if g.id == id:
            old_groups[i] = group
            break
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_group_header(app):
   # if app.group.count() == 0:
       # app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header="edited"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)