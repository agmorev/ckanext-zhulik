import ckan.plugins.toolkit as tk
import ckanext.zhulik.logic.schema as schema


@tk.side_effect_free
def zhulik_get_sum(context, data_dict):
    tk.check_access(
        "zhulik_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.zhulik_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'zhulik_get_sum': zhulik_get_sum,
    }
