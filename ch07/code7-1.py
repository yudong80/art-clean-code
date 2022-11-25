import urllib.request


def url_to_html(url):
  html = urllib.request.urlopen(url).read()
  return html
