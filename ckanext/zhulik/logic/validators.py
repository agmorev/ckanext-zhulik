import ckan.plugins.toolkit as tk


def zhulik_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "zhulik_required": zhulik_required,
    }
