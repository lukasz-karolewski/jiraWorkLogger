from datetime import datetime

from chalice import Chalice
from chalicelib import jiraWorkLogger

app = Chalice(app_name='jiraWorkLogger')
app.debug = True


@app.route('/save-config', methods=['POST'], cors=True)
def save_config():
    config = app.current_request.json_body
    return {'received_config': config}


@app.route('/get-config', cors=True)
def get_config_view():
    return {'hello': 'world'}


@app.route('/check-credentials', methods=['POST'], cors=True)
def check_credentials_view():
    req = app.current_request.json_body
    return {"status": jiraWorkLogger.check_credentials(req['username'], req['password'])}

#
# @app.route('/process-employee', methods=['POST'], cors=True)
# def process_employee_view():
#     config = app.current_request.json_body
#
#     jira_ticket = config['jira_ticket']
#     default_overhead = config['default_overhead']
#     hours_per_day = config['hours_per_day']
#     days_in_period = args.days
#     employees = config['employees']
#     as_of = config.get('as_of', datetime.now().replace(microsecond=0).isoformat())
#
#     return jiraWorkLogger.process_employee(jira_ticket, as_of, employee, days_in_period, hours_per_day,
#                                            default_overhead)
