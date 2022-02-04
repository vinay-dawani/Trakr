def only_admin(message, next):
    user = message.get('user')
    if user == "U":
        next()
