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
            result_page = wiki_page(response_data[page_id]['pageid'])
            break
    
    sentences_list = result.split('.')

    sentences_list = sentences_list[:10]

    result = '.'.join(sentences_list)

    result = result + '.'

    result = result + f'\n\n💬 Read more in official <a href="{result_page}">Wikipedia page</a> ...'

    return result

def wiki_page(search_keyword):
    result = f"https://en.wikipedia.org/w/index.php?curid={search_keyword}"

    return result