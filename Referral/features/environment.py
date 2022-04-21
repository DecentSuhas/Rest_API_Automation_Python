from Referral.utilities import config
from Referral.utilities.excel_operations import get_ref_text_from_excel
from Referral.utilities.json_operations import update_json


def before_feature(context, feature):
    if config.locale == "Czech":
        get_ref_text_from_excel("Czech")
        update_json("referalBody", "refer-a-friend-lumea-czech-republic", "cz-CZ")
    elif config.locale == "Romania":
        get_ref_text_from_excel("Romania")
        update_json("referalBody", "refer-a-friend-lumea-romania", "ro-RO")
    elif config.locale == "Netherlands":
        get_ref_text_from_excel("Netherlands")
        update_json("referalBody", "lumea-mobile-app-staging", "nl-NL")
    elif config.locale == "English":
        get_ref_text_from_excel("English")
        update_json("referalBody", "lumea-mobile-app-staging-try-and-buy", "nl-NL")
