def get_downloadAddr(url):
    import urllib.request as ur
    import re
    import gzip
#    url = 'http://www.piaohua.com/html/aiqing/2016/0527/30958.html'
    try:
        webPage = ur.urlopen(url)
    except:
        return None
    doc = webPage.read()
    try:
        data = gzip.decompress(doc).decode("utf-8")
    except:
        data = doc.decode("utf-8")
    url_list1 = []
    url_list2 = []
    url_list3 = []
    url_list4 = []
    url_list1 = re.findall(r"(?<=href=\")ftp.*?(?=\")",data)
    url_list2 = re.findall(r"(?<=href=\")thunder.*?(?=\")", data)
    url_list3 = re.findall(r"http.*?rmvb", data)
    url_list4 = re.findall(r"(?<=href=\")ed2k.*?(?=\")", data)
    url_list = url_list1 + url_list2 + url_list3 +url_list4
    #getUrl = re.search(r"(ftp|thunder).*?(rmvb|mp4|mkv|avi)",data)
    if url_list:
        url_list = list(set(url_list))
        url_list.sort()
        return url_list
