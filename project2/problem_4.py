class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
child2 = Group("child2")
sub_child2 = Group("subchild2")

parent.add_user("newuser")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child2_user = "sub_child2_user"
sub_child.add_user(sub_child2_user)
sub_child.add_user("sss")

child.add_group(sub_child)
parent.add_group(child2)
parent.add_group(child)


def is_user_in_group(user, group, found):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if found:
        return True
    print(group.name, group.get_users())
    for _user in group.get_users():
        print(user, "--- ", _user)
        if(user == _user):
            found = True

    for _group in group.get_groups():
        found = is_user_in_group(user, _group, found)

    return found


print(is_user_in_group("sss", parent, False))
