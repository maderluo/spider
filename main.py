def main_process(content):
    import dlAddr,next_link,re


    #获取下载链接函数：
    def getAdrr(next_url):
        downloadaddr_list = dlAddr.get_downloadAddr(next_url)
        # download_addr_list.append(download_addr)
        # flag用于表示是否找到所要的电影下载链接
        flag = 0
        if downloadaddr_list != None and downloadaddr_list != []:
            for download_addr in downloadaddr_list:
                # result = re.search(content, download_addr)
                # if result:
                print(download_addr)
                flag = 1
        if flag == 1:
            return downloadaddr_list
        else:
            return 0x111
    #种子节点及根目录：
    first_link = 'http://www.piaohua.com'
    next_link_list = []
    #next_link_list.insert(0,'http://www.piaohua.com/html/aiqing/2016/0607/30997.html')
    next_link_list.append(first_link)
    done_url = []
    done_url.append('/')
    done_url.append('#')

    #download_addr_list = []
    # content = input("Please Enter The Movie Name:\n")
    x = 0
    while True:
        next_url = next_link_list.pop(0)
        done_url.append(next_url)
        list1 = next_link.next_links(first_link,next_url,content)
        if list1[0] == 'first':
            list1.pop(0)
            target_link = list1[0]  #有可能直接链接到下载文件的网页,不能用pop(0)获取，万一targ_link里没有下载链接，它还得放进带抓取链接列表里
            result1 = getAdrr(target_link)
            result2 = getAdrr(next_url)
            if result1 != 0x111:
                result = result1
                break
            elif result2 !=0x111:
                result = result2
                break
            else:
                for link in list1:
                    if link not in next_link_list and link not in done_url:
                        next_link_list.append(link)
        else:
            list1.pop(0)
            for link in list1:
                if link not in next_link_list and link not in done_url:
                    next_link_list.append(link)
            # list1.pop(0)
            # next_link_list += list1
            # next_link_list = list(set(next_link_list))
            #next_link_list.sort()
        x = x+1
        if x%50 == 0:
            print("已搜索%d条网页"%x)
            print("已搜索的网页列表")
            print(done_url)
    # download_addr_list = list(set(download_addr_list))
    # for dl_addr in download_addr_list:
    #     print(dl_addr)
    print("search ok!")
    return result