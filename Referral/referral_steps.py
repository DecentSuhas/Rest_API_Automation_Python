from Referral import validation_text
from Referral.referral_api_calls import get_prefetch_content


def validate_header_text():
    """
    This methods verifies the header text of referral main
    :return:
    """
    expected_text_header = validation_text.HEADER_TEXT
    prefetch_content = {}
    prefetch_content.update(get_prefetch_content())
    head_text = prefetch_content['data']['mainView']['header']  # It is a string
    assert head_text == expected_text_header, f"Incorrect header found = {head_text}"
    print(f"Success: Header text : {head_text}")


def validate_header_text_on_referral_buttons():
    """
    This method verifies the header text of referral entry points
    :return:
    """
    prefetch_content = {}
    prefetch_content.update(get_prefetch_content())
    dashboard_top_head_text = prefetch_content['data']['calls_to_action'][0]['ctaButtonText']
    dashboard_bottom_head_text = prefetch_content['data']['calls_to_action'][1]['headerText']
    dashboard_explore_head_text = prefetch_content['data']['calls_to_action'][2]['headerText']
    dashboard_profile_head_text = prefetch_content['data']['calls_to_action'][3]['headerText']
    validate_response("Dashboard button", dashboard_top_head_text, validation_text.CTA_DASHBOARD_TOP_TEXT_HEADER)
    validate_response("Dashboard banner", dashboard_bottom_head_text, validation_text.CTA_DASHBOARD_BOTTOM_TEXT_HEADER)
    validate_response("Explore", dashboard_explore_head_text, validation_text.CTA_EXPLORE_TEXT_HEADER)
    validate_response("Profile", dashboard_profile_head_text, validation_text.CTA_PROFILE_TEXT_HEADER)


def validate_referral_button_description():
    """
        This method verifies the description text of referral banners in all entry points
        :return:
    """
    prefetch_content = {}
    prefetch_content.update(get_prefetch_content())
    dashboard_banner_desc = prefetch_content['data']['calls_to_action'][1]['paragraph']
    explore_banner_desc = prefetch_content['data']['calls_to_action'][2]['paragraph']
    profile_banner_desc = prefetch_content['data']['calls_to_action'][3]['paragraph']
    treatment_report_banner_desc = prefetch_content['data']['calls_to_action'][4]['paragraph']
    validate_response("Banner description-Dashboard", dashboard_banner_desc,
                      validation_text.CTA_DASHBOARD_BOTTOM_BTN_DESC)
    validate_response("Banner description-Explore", explore_banner_desc,
                      validation_text.CTA_EXPLORE_BTN_DESC)
    validate_response("Banner description-Profile", profile_banner_desc,
                      validation_text.CTA_PROFILE_BTN_DESC)
    validate_response("Banner description-TreatmentReport", treatment_report_banner_desc,
                      validation_text.CTA_TREATMENT_BTN_DESC)

def validate_campaign_text():
    """
    This method verifies the campaign text in referral screen.
    :return:
    """
    prefetch_content = {}
    prefetch_content.update(get_prefetch_content())
    campaign_desc = prefetch_content['data']['mainView']['paragraph']
    validate_response("Campaign descrition", campaign_desc,
                      validation_text.PARAGRAPH_VALUE)

def validate_response(referral_entrypoint, actual_text, expected_text):
    """
        This method verifies the text.

    :param referral_entrypoint:
    :param actual_text:
    :param expected_text:
    :return:
    """
    assert actual_text == expected_text, f"Incorrect text found in {referral_entrypoint} = {actual_text}"
    print(f"Success: Text found in {referral_entrypoint} = {actual_text}")


validate_campaign_text()
