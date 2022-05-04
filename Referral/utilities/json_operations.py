"""
This file contains all the method to operate on json file
"""
import json
import os

from Referral.utilities.config import path


def update_json(filename, valuetoupdate, region):
    """
    This method updates the existing json file with value passed as parameter
    :param filename:
    :param valuetoupdate:
    :param argvs:
    :return:
    """
    jsonPath = path + "\\data\\" + filename + ".json"
    with open(jsonPath, 'r') as jp:
        payload = json.load(jp)
    payload.update({
        "event_name": "advocate_mobile_experience",
        "data": {
            "first_name": "Lumea_automation",
            "email": "Lumea_automation@yopmail.com",
            "partner_user_id": "1220000",
            "labels": valuetoupdate,
            "locale": region
        }
    })
    with open(jsonPath, 'w') as jp:
        json.dump(payload, jp, indent=2)
