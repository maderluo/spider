from tkinter import *
from tkinter import ttk
from main import main_process

def getAddr(*args):
    content = movieName.get()
    list = main_process(content)
    text = ''
    for link in list:
        text = text + link+'\n'
    downloadAddr.set(text)

main = Tk()
main.title('电影下载链接搜索')
mainframe = ttk.Frame(main, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

movieName = StringVar()
downloadAddr = StringVar()
movieName_entry = ttk.Entry(mainframe, textvariable=movieName)
movieName_entry.grid(column=1, row=2,columnspan=2, sticky=W)
ttk.Label(mainframe, textvariable=downloadAddr).grid(row=4, column=1, columnspan=4,sticky=W)
ttk.Button(mainframe, text="搜索",command=getAddr).grid(column=4,row=2,sticky=W)

movieName_entry.focus()
main.bind('<Return>',getAddr)

#图片显示
# photo = PhotoImage(file='hh.gif')
# label = Label(image=photo)
# label.image = photo
# label.grid(row=4,column=1,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


ttk.Label(mainframe,text="请输入电影名称:").grid(column=1, row=1, columnspan=2,sticky=W)
ttk.Label(mainframe, text="下载链接：").grid(row=3,columnspan=4,sticky=W)


main.mainloop()