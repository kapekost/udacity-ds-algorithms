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


def is_user_in_group(user, group, found=False):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == None or group == None:
        return False
    if user.strip() == "":
        return False

    if found:
        return True
    # print(group.name, group.get_users())
    for _user in group.get_users():
        # print(user, "--- ", _user)
        if(user == _user):
            found = True

    for _group in group.get_groups():
        found = is_user_in_group(user, _group, found)

    return found


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    child2 = Group("child2")
    sub_child2 = Group("subchild2")
    sub_sub_child = Group("sub_sub_child")

    parent.add_user("newuser")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    sub_child2_user = "sub_child2_user"
    sub_child.add_user(sub_child2_user)
    sub_child.add_user("Kostas")
    sub_sub_child.add_user("subsubchild")

    child.add_group(sub_child)
    child.add_group(sub_sub_child)
    parent.add_group(child2)
    parent.add_group(child)

    print("find name, 2 levels deep")
    assert is_user_in_group(
        "Kostas", parent) == True, f"find name, 2 levels deep"
    print("find false name, 2 levels deep")
    assert is_user_in_group(
        "not-user", parent) == False, f"find false name, 2 levels deep"
    print("find second name, 2 levels deep")
    assert is_user_in_group(
        "sub_child2_user", parent) == True, f"find second name, 2 levels deep"
    print("find second name, 1 level deep")
    assert is_user_in_group(
        "newuser", parent) == True, f"find second name, 1 level deep"
    print("find second name, 1 level deep")
    assert is_user_in_group(
        "sub_child_user", parent) == True, f"find second name, 1 level deep"
    print("find second name, 3 levels deep")
    assert is_user_in_group(
        "subsubchild", parent) == True, f"find second name, 3 levels deep"
    print("empty user string")
    assert is_user_in_group(
        "", parent) == False, f"empty user string"
    print("None user string")
    assert is_user_in_group(
        None, parent) == False, f"None user string"
    print("all passed")
