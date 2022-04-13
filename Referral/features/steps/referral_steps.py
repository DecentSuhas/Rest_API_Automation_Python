""" Includes referral steps"""
from behave import step # pylint: disable=no-name-in-module

from Referral.utilities.apiCalls import getPrefetchContent, \
    prefetchContent  # pylint: disable=no-name-in-module
from Referral.data import text # pylint: disable=no-name-in-module


@step("I verify the title text of referral full screen")
def validate_head_text(context):
    """
    This methods verifies the header text of referral main
    :return:
    """
    expected_text_header = text.HEADER_TEXT
    prefetchContent.update(getPrefetchContent(context))
    head_text = prefetchContent['data']['mainView']['header']  # It is a string
    assert head_text == expected_text_header, f"Incorrect header found = {head_text}"
    print(f"Success: Header text : {head_text}")


@step("I verify title text in banners and referral screen")
def validate_header_text_on_referral_buttons(context):
    """
    This method verifies the header text of referral entry points
    :return:
    """
    dashboard_top_head_text = prefetchContent['data']['calls_to_action'][0]['ctaButtonText']
    dashboard_bottom_head_text = prefetchContent['data']['calls_to_action'][1]['headerText']
    dashboard_explore_head_text = prefetchContent['data']['calls_to_action'][2]['headerText']
    dashboard_profile_head_text = prefetchContent['data']['calls_to_action'][3]['headerText']
    validate_resp("Dashboard button", dashboard_top_head_text, text.DASHBRD_TOP_HEADER)
    validate_resp("Dashboard banner", dashboard_bottom_head_text, text.DASHBRD_BOTTOM_HEADER)
    validate_resp("Explore", dashboard_explore_head_text, text.EXPLORE_TEXT_HEADER)
    validate_resp("Profile", dashboard_profile_head_text, text.PROFILE_TEXT_HEADER)


@step("I verify the description text in referral banner entry points")
def validate_desc_ref_banner(context):
    """
        This method verifies the description text of referral banners in all entry points
        :return:
    """
    dashboard_banner_desc = prefetchContent['data']['calls_to_action'][1]['paragraph']
    explore_banner_desc = prefetchContent['data']['calls_to_action'][2]['paragraph']
    profile_banner_desc = prefetchContent['data']['calls_to_action'][3]['paragraph']
    treatment_report_banner_desc = prefetchContent['data']['calls_to_action'][4]['paragraph']
    validate_resp("Banner description-Dashboard", dashboard_banner_desc,
                  text.DASHBRD_BTM_BTN_DESC)
    validate_resp("Banner description-Explore", explore_banner_desc,
                  text.EXPLORE_BTN_DESC)
    validate_resp("Banner description-Profile", profile_banner_desc,
                  text.PROFILE_BTN_DESC)
    validate_resp("Banner description-TreatmentReport", treatment_report_banner_desc,
                  text.TREATMENT_BTN_DESC)

@step("I verify the campaign text")
def validate_campaign_text(context):
    """
    This method verifies the campaign text in referral screen.
    :return:
    """
    prefetchContent.update(getPrefetchContent(context))
    campaign_desc = prefetchContent['data']['mainView']['paragraph']
    validate_resp("Campaign description", campaign_desc,
                  text.PARAGRAPH_VALUE)


def validate_resp(referral_entrypoint, actual_text, expected_text):
    """
        This method verifies the text.

    :param referral_entrypoint:
    :param actual_text:
    :param expected_text:
    :return:
    """
    assert actual_text == expected_text, \
        f"Incorrect text found in {referral_entrypoint} is \'{actual_text}\'"
    print(f"Success: Text found in {referral_entrypoint} is \'{actual_text}\'")
