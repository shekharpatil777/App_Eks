def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            raise PermissionError("Admin privileges required")
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def delete_user(user, username):
    print(f"{username} deleted by {user['name']}")

user = {"name": "Alice", "role": "admin"}
delete_user(user, "Bob")
