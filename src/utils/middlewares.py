#  middleware used to only allow admin to access certain commands
def only_admin(message, next):
    user = message.get("user")
    if user == "U":
        next()


# ? middlewares for different level of access control
