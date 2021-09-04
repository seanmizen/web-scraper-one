from bs4 import BeautifulSoup

# Go to the Website:
# https://find-and-update.company-information.service.gov.uk/search
# Search for “Barclays”
# https://find-and-update.company-information.service.gov.uk/search?q=Barclays
# Click on the first result:
# https://find-and-update.company-information.service.gov.uk/company/00048839
# Parse the HTML


def get_entity_details(entity_name):
    host = 'https://find-and-update.company-information.service.gov.uk'
    details = {
        'company_name': None,
        'registered_address': None,
        'company_status': None,
        'company_type': None,
        'incorporated_on': None}
    # functions will run here
    # ...
    # ...
    return details


# function that searches the entity using php query in the URL
def run_search(host, entity_name):

    # todo, sanitise host into URL format
    search_url = host + "search?q=" + entity_name
    # with urllib.request.urlopen(search_url) as search_url_page:
    #    return search_url_page.read()

    # we're looking for the first element of type=company in the list id=results


# function to search inital details
    # identify the seach pane element
    # use a CSS selector for input['search'] to enter search
    # etc

# solution NOT using selenium:

# import module that can run REST requests
# send a rest request for URL https://find-and-update.company-information.service.gov.uk/search with search "entity name"
# return data in the format it returns in
# transform data into the dictionary given

if __name__ == "__main__":
    print("Hello!")
    pass
