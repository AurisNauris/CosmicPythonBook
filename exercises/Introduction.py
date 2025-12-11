
def snippet_01():
    import json
    import ssl
    from urllib.request import urlopen
    from urllib.parse import urlencode

    # Create a context that ignores security/certificate errors
    ## Note that this is a short fix
    ## for longer time, need to upgrade certificates for my python for macos
    ssl_context = ssl._create_unverified_context()

    params = dict(q='Sausages', format='json')

    # Pass the context to the urlopen
    handle = urlopen('http://api.duckduckgo.com' + '?' + urlencode(params),
                     context=ssl_context)
    raw_text = handle.read().decode('utf8')
    parsed = json.loads(raw_text)

    results = parsed['RelatedTopics']
    for r in results:
        if 'Text' in r:
            print(r['FirstURL'] + ' - ' + r['Text'])

def snippet_02():
    import requests

    params = dict(q="Sausages", format="json")
    parsed = requests.get("http://api.duckduckgo.com/", params=params).json()

    results = parsed['RelatedTopics']
    for r in results:
        if 'Text' in r:
            print(r['FirstURL'] + ' - ' + r['Text'])

# def snippet_03():
#       This will not work anymore because outdated package
#     import duckduckpy
#     for r in duckduckpy.query('Sausages').related_topics:
#         print(r.first_url, ' - ', r.text)

## Very explicit
#snippet_01()
## Less explicit, more abstraction
#snippet_02()
## Very much abstracted, note that package is outdated
#snippet_03()