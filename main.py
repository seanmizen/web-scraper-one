import urllib.request
from bs4 import BeautifulSoup
import json

# Go to the Website:
# https://find-and-update.company-information.service.gov.uk/search
# Search for “Barclays”
# https://find-and-update.company-information.service.gov.uk/search?q=Barclays
# Click on the first result:
# https://find-and-update.company-information.service.gov.uk/company/00048839
# Parse the HTML


def get_entity_details(entity_name):
    host = "https://find-and-update.company-information.service.gov.uk"
    details = {
        "company_name": None,
        "registered_address": None,
        "company_status": None,
        "company_type": None,
        "incorporated_on": None}

    bs_obj = run_search(host, entity_name)
    # todo handle zero results
    # todo handle http error
    first_link = host + bs_obj.find(id="results").find("a").get("href")

    first_result_page = BeautifulSoup(
        urllib.request.urlopen(first_link).read(), "html.parser")

    try:
        details["company_name"] = first_result_page.find(
            "p", class_="heading-xlarge").text.strip()
    except:
        pass
    details["registered_address"] = extract_dd_element(
        first_result_page, "Registered office address")
    details["company_status"] = extract_dd_element(
        first_result_page, "Company status")
    details["company_type"] = extract_dd_element(
        first_result_page, "Company Type")
    details["incorporated_on"] = extract_dd_element(
        first_result_page, "Incorporated on")

    return details


def extract_dd_element(result_page, dt_name):
    try:
        return_val = result_page.find(
            "dt", text="dt_name").next_sibling.next_sibling.text.strip()
    except:
        return_val = ""
    return return_val


# function that searches the entity using query in the URL
def run_search(host, entity_name):
    # todo, sanitise host into URL format
    search_url = host + "/search?q=" + entity_name
    with urllib.request.urlopen(search_url) as search_url_page:
        #
        bs_obj = BeautifulSoup(search_url_page.read(), "html.parser")
        return bs_obj

    # We're looking for the first element of type=company in the list id=results


if __name__ == "__main__":
    print(json.dumps(get_entity_details("Barclays")))
    print(json.dumps(get_entity_details("seanmizen.com")))
