def check_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if permission in user.permissions:
                print(f"User '{user.name}' has permission '{permission}'. Access granted.")
                return func(user, *args, **kwargs)
            else:
                print(f"User '{user.name}' does not have permission '{permission}'. Access denied.")
                return None
        return wrapper
    return decorator

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

#This decorator can be used to check if a user has the required permissions to access a function.
@check_permission("admin")
def delete_user(user, user_to_delete):
    print(f"User '{user.name}' deleting user '{user_to_delete}'.")

admin_user = User("Alice", ["admin", "read"])
guest_user = User("Bob", ["read"])

delete_user(admin_user, "Charlie")
delete_user(guest_user, "Dave")
# Output:
# User 'Alice' has permission 'admin'. Access granted.
# User 'Alice' deleting user 'Charlie'.
# User 'Bob' does not have permission 'admin'. Access denied.
