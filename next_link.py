#first_link为网站根目录，url为要打开的网页网址，done_url为已爬过的网页网址,content为搜索内容
def next_links(first_link,url,content):
    import urllib.request as ur
    import re
    import gzip

    next_link_list1 = []
    try:
        webPage = ur.urlopen(url)
    except:
        next_link_list1.insert(0, 'second')  # 主要是防止访问的页面没有时抓不到链接next_link_list3为空，导致main.py里面的list1[0]出现越界访问
        return next_link_list1
    doc = webPage.read()
    try:
        data = gzip.decompress(doc).decode("utf-8")
    except:
        data = doc.decode("utf-8")
    # allUrl = webPage.geturl()
    # print(allUrl)

    link_list = re.findall(r"(?<=a href=\").+?(?=\")|(?<=a href=\').+?(?=\')" ,data)  #斜杠\" 表示转移字符"
    # for next_url in link_list:
    #     print(next_url)
    # print("==============================================================================")
    link_list = list(set(link_list))
    # try:
    #     next_link_list = [link for link in link_list if link not in done_url ]
    # except:
    #     print("not found ")
    # for next_url in next_link_list:
    #     print(next_url)
    next_link_list1 = [first_link+link if link[0]=='/' else link for link in link_list]
    next_link_list2 = []
    for link in next_link_list1:
        if link[0:4] == 'list':
            replace_link = url.split("/")[-1]
            link = re.sub(replace_link, link, url)
            next_link_list2.append(link)
        else:
            next_link_list2.append(link)
    next_link_list3 = next_link_list2
    # next_link_list3 = []
    # try:
    #     next_link_list3 = [link for link in next_link_list2 if link not in done_url]
    # except:
    #     print("not found ")

    #清除无用的，外站的链接
    next_link_list3 = [link for link in next_link_list3 if link[0:len(first_link)] == first_link]
    unuse_link = 'http://www.piaohua.com/webPlay'
    next_link_list3 = [link for link in next_link_list3 if link[0:len(unuse_link)] != unuse_link]
    # str1 = '(?<=href=\"' + ')' + '.*?' + content  #通过这种字符串组合的方式来为正则表达式输入变量
    # str2 = re.search(str1, data)
    # print(str2.group())
    # if str2:
    #     str3 = re.search(r'(?<=href=\").*(href=\")',str2.group())
    #     str4 = str3.group()
    #     str5 = '(?<=' + str4 +')' + '.*?' + '(?=\")'
    #     result = re.search(str5,str2.group())

    str1 = '(href=\"' + ')' + '.*?' + content
    str2 = re.search(str1, data)
    if str2:
        str3 = re.split('href=', str2.group())
        result = re.search(r'(?<=\").*?(?=\")',str3[-1])
        if result:
            a_link = result.group()
            a_link = first_link+a_link
            next_link_list3[0] = 'first'
            next_link_list3.insert(1, a_link)
        # else:
        #     next_link_list3.insert(0, 'second')  # 主要是防止访问的页面没有时抓不到链接next_link_list3为空，导致main.py里面的list1[0]出现越界访问
    else:
        next_link_list3.insert(0, 'second')
    return next_link_list3

# first_link = 'http://www.piaohua.com'
# content = '真相禁区'
# url = 'http://www.piaohua.com'
# done_url = []
# list = next_links(first_link, url, done_url, content)
# print(list)