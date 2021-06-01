import blogsite.settings

if (blogsite.settings.DEBUG):
    raise ValueError("Set DEBUG to False")
