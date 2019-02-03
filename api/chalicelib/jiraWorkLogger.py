import base64
import json
import logging
import math
import os

import requests

logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

JIRA_URL = "https://jira.move.com"
JIRA_MAX_ALLOWED_HOURS_PER_ENTRY = 99

url = f"{JIRA_URL}/rest/tempo-timesheets/3/worklogs/"
user = os.getenv('jira_username')
password = os.getenv('jira_password')


def _get_headers(user, password):
    authorization_hash = base64.b64encode(bytes(f"{user}:{password}", 'utf-8')).decode("utf-8")
    return {
        "Authorization": f"Basic {authorization_hash}",
        "Content-Type": "application/json"
    }


def check_credentials(username, password):
    return True


def process_employee(jira_ticket, as_of, employee, days_in_period, hours_per_day, default_overhead):
    days_off = employee.pop('days_off')
    overhead = employee.pop('overhead') if 'overhead' in employee else default_overhead

    hours = math.floor(hours_per_day * (1 - overhead) * (days_in_period - days_off))

    while hours > JIRA_MAX_ALLOWED_HOURS_PER_ENTRY:
        _log_work(jira_ticket, as_of, employee['name'], JIRA_MAX_ALLOWED_HOURS_PER_ENTRY)
        hours -= JIRA_MAX_ALLOWED_HOURS_PER_ENTRY

    _log_work(jira_ticket, as_of, employee, hours)


def _log_work(jira_ticket, as_of, jira_username, hours):
    if hours <= 0:
        logger.info(f'attempted logging {hours} for {jira_username}')
        return

    logger.info(f'logging {hours} for {jira_username}')
    data = {
        "issue": {
            "key": jira_ticket,
        },
        "comment": f'Working on issue {jira_ticket}',
        "dateStarted": as_of,

        "timeSpentSeconds": 60 * 60 * hours,
        "author": {"name": jira_username},
    }

    r = requests.post(url, headers=_get_headers(user, password), data=json.dumps(data))

    if r.status_code == 200:
        logger.info(r.status_code)
    else:
        raise Exception(logger.debug(r.content.decode("utf-8")))
