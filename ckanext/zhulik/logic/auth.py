import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def zhulik_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "zhulik_get_sum": zhulik_get_sum,
    }
