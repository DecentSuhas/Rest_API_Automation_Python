from Referral import validation_text
from Referral.referral_api_calls import get_prefetch_content


def validate_header_text():
    """
    This methods verifies the header text of referral main
    :return:
    """
    expected_text_header = validation_text.HEADER_TEXT
    # expected_text_header_dashboard_top = validation_text.CTA_DASHBOARD_TOP_TEXT_HEADER
    # expected_text_header_dashboard_bottom = validation_text.CTA_DASHBOARD_BOTTOM_TEXT_HEADER
    # expected_text_header_explore = validation_text.CTA_EXPLORE_TEXT_HEADER
    # expected_text_header_profile = validation_text.CTA_PROFILE_TEXT_HEADER
    # expected_text_header_treatment = validation_text.CTA_TREATMENT_REPORT_BANNER_HEADER_TEXT
    prefetch_content = {}
    prefetch_content.update(get_prefetch_content())
    head_text = prefetch_content['data']['mainView']['header']  # It is a string
    assert head_text == expected_text_header, f"Incorrect header found = {head_text}"
    print(f"Success: Header text : {head_text}")


validate_header_text()