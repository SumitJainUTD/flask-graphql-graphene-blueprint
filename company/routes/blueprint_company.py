from flask import Blueprint
import json

company = Blueprint("company", __name__)


@company.route('/<company_id>')
def get_company(company_id):
    return json.dumps({
        "company_id": company_id
    })
