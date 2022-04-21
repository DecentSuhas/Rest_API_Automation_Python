""" Includes referral steps"""
from behave import step  # pylint: disable=no-name-in-module


from Referral.utilities.apiCalls import getPrefetchContent, \
    prefetchContent  # pylint: disable=no-name-in-module
from Referral.utilities.config import localization_dict
from Referral.utilities.excel_operations import locale_text_list


@step("I verify the title text of referral full screen")
def validate_head_text(context):
    """
    This methods verifies the header text of referral main
    :return: None
    """
    expected_text_header = localization_dict["HEADER_TEXT"]
    prefetchContent.update(getPrefetchContent(context))
    head_text = prefetchContent['data']['mainView']['header']  # It is a string
    assert head_text == expected_text_header, f"Incorrect header found = {head_text}"
    print(f"Success: Header text : {head_text}")


@step("I verify title text in banners and referral screen")
def validate_header_text_on_referral_buttons(context):
    """
    This method verifies the header text of referral entry points
    :return: None
    """
    dashboard_top_head_text = prefetchContent['data']['calls_to_action'][0]['ctaButtonText']
    dashboard_bottom_head_text = prefetchContent['data']['calls_to_action'][1]['headerText']
    dashboard_explore_head_text = prefetchContent['data']['calls_to_action'][2]['headerText']
    dashboard_profile_head_text = prefetchContent['data']['calls_to_action'][3]['headerText']
    validate_resp("Dashboard button", dashboard_top_head_text)
    validate_resp("Dashboard banner", dashboard_bottom_head_text)
    validate_resp("Explore", dashboard_explore_head_text)
    validate_resp("Profile", dashboard_profile_head_text)


@step("I verify the description text in referral banner entry points")
def validate_desc_ref_banner(context):
    """
    This method verifies the description text of referral banners in all entry points
    :return: None
    """
    dashboard_banner_desc = prefetchContent['data']['calls_to_action'][1]['paragraph']
    explore_banner_desc = prefetchContent['data']['calls_to_action'][2]['paragraph']
    profile_banner_desc = prefetchContent['data']['calls_to_action'][3]['paragraph']
    treatment_report_banner_desc = prefetchContent['data']['calls_to_action'][4]['paragraph']
    validate_resp("Banner description-Dashboard", dashboard_banner_desc,
                  localization_dict["DASHBRD_BTM_BTN_DESC"])
    validate_resp("Banner description-Explore", explore_banner_desc,
                  localization_dict["EXPLORE_BTN_DESC"])
    validate_resp("Banner description-Profile", profile_banner_desc,
                  localization_dict["PROFILE_BTN_DESC"])
    validate_resp("Banner description-TreatmentReport", treatment_report_banner_desc,
                  localization_dict["TREATMENT_BTN_DESC"])


@step("I verify the campaign text")
def validate_campaign_text(context):
    """
    This method verifies the campaign text in referral screen.
    :return: None
    """
    prefetchContent.update(getPrefetchContent(context))
    campaign_desc = prefetchContent['data']['mainView']['paragraph']
    validate_resp("Campaign description", campaign_desc,
                  localization_dict["PARAGRAPH_VALUE"])


@step("I verify the how it works title and description")
def validate_how_it_works(context):
    """
    This method validates the how it works link text and the description
    :param context:
    :return:
    """
    HIT_title = prefetchContent['data']['howItWorks']['headerText']
    HIT_desc = prefetchContent['data']['howItWorks']['paragraph']
    # validate_resp("How it works title", HIT_title,
    #               text.HOW_IT_WORKS_TEXT)
    validate_resp("How it works description", HIT_desc,
                  localization_dict["HOW_IT_WORKS_DESC"])


def validate_resp(referral_entrypoint, actual_text, *argvs):
    """
        This method verifies the text.

    :param referral_entrypoint:
    :param actual_text:
    :param expected_text:
    :return: None
    """
    check = "False"
    for item in range(0, len(locale_text_list)):
        expected_text = locale_text_list[item]
        if actual_text == expected_text:
            check = "True"
    assert check == "True", \
        f"Incorrect text found in {referral_entrypoint} : \'{actual_text}\' : Expected text = {expected_text}"
    print(f"Success: Text found in {referral_entrypoint} is \'{actual_text}\'")
