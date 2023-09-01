import requests

def wiki_response(search_keyword):
    request_session = requests.Session()

    api_url = "https://en.wikipedia.org/w/api.php"

    parameters = {
        "action": "query",
        "generator": "prefixsearch",
        "gpssearch": search_keyword,
        "prop": "extracts",
        "namespace": "0",
        "exintro": "1",
        "explaintext": "1",
        "redirects": "1",
        "format": "json"
    }

    response = request_session.get(url=api_url, params=parameters).json()

    response_data = response['query']['pages']

    page_ids = response_data.keys()

    for page_id in page_ids:
        if response_data[page_id]['index'] == 1:
            result = response_data[page_id]['extract']
            break

    return result