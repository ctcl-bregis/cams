# CAMS - CTCL 2017-2023
# Date: July 5, 2023 - July 6, 2023
# Purpose: Django views for the integrated documentation feature

# {{ dict|get_item:key }}
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
