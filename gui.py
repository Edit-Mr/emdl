import pyperclip
import re
import requests
from bs4 import BeautifulSoup
import os
import yt_dlp
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import ttk
import threading

# Download as PDF or original

def download(redirected_urls):
    print(combinePdf)
    pdfs = []
    btn.destroy()
    blank.destroy()
    if haveYouTube:
        ytFormatBox.destroy()
    if haveGoogleDoc > 0:
        fileFormatBox.destroy()
        if haveGoogleDoc > 1:
            combineBox.destroy()
    i = 0
    bar = ttk.Progressbar(group, mode='determinate',
                          maximum=len(redirected_urls))
    bar.pack(fill='x')
    for url in redirected_urls:
        a.set("正在下載 " + url)
        root.update()
        if "https://docs.google.com/document/" in url:
            pdf_url = f"{url.split('/edit')[0]}/export?format={fileValue.get()}"
            response = requests.get(pdf_url)
            if response.status_code == 200:
                filename = os.path.basename(pdf_url)
                index = redirected_urls.index(url)
                filename = f"index{index}.pdf"
                with open(filename, 'wb') as file:
                    file.write(response.content)
                a.set("成功下載歌譜" + filename)
                pdfs.append(filename)
            else:
                a.set(f"Error downloading {url}")
        elif "https://drive.google.com/file/" in url:
            file_id = url.split("drive.google.com/file/d/")[1].split("/")[0]
            url = f"https://drive.google.com/uc?id={file_id}"
            response = requests.get(url)
            if response.status_code == 200:
                filename = response.headers['Content-Disposition'].split(
                    "filename=")[1].split(";")[0].replace('"', '')
                with open(filename, "wb") as file:
                    file.write(response.content)
                a.set(f"成功下載檔案 {filename}")
            else:
                a.set(f"檔案下載失敗 {url}")
        elif "you" in url:
            if ytValue.get() == "mp3":
                ydl_opts = {'extract_flat': 'discard_in_playlist',
                            'final_ext': 'mp3',
                            'format': 'bestaudio/best',
                            'fragment_retries': 10,
                            'ignoreerrors': 'only_download',
                            'outtmpl': {'default': '%(title)s.%(ext)s', 'pl_thumbnail': ''},
                            'postprocessors': [{'key': 'FFmpegExtractAudio',
                                                'nopostoverwrites': False,
                                                'preferredcodec': 'mp3',
                                                'preferredquality': '5'},
                                               {'add_chapters': True,
                                                'add_infojson': 'if_exists',
                                                'add_metadata': True,
                                                'key': 'FFmpegMetadata'},
                                               {'already_have_thumbnail': False,
                                                'key': 'EmbedThumbnail'},
                                               {'key': 'FFmpegConcat',
                                                'only_multi_video': True,
                                                'when': 'playlist'}],
                            'retries': 5,
                            'writethumbnail': True}
            elif ytValue.get() == "mp4 (較慢)":
                ydl_opts = {'extract_flat': 'discard_in_playlist',
                            'format': 'bestvideo+bestaudio/best',
                            'fragment_retries': 10,
                            'ignoreerrors': 'only_download',
                            'outtmpl': {'default': '%(title)s.%(ext)s', 'pl_thumbnail': ''},
                            'postprocessors': [{'key': 'FFmpegVideoConvertor',
                                                'preferedformat': 'mp4'},
                                               {'add_chapters': True,
                                                'add_infojson': 'if_exists',
                                                'add_metadata': True,
                                                'key': 'FFmpegMetadata'},
                                               {'already_have_thumbnail': False,
                                                'key': 'EmbedThumbnail'},
                                               {'key': 'FFmpegConcat',
                                                'only_multi_video': True,
                                                'when': 'playlist'}],
                            'retries': 5,
                            'writethumbnail': True}
            else:
                ydl_opts = {'extract_flat': 'discard_in_playlist',
                            'format': 'bestvideo+bestaudio/best',
                            'fragment_retries': 10,
                            'ignoreerrors': 'only_download',
                            'outtmpl': {'default': '%(title)s.%(ext)s', 'pl_thumbnail': ''},
                            'postprocessors': [{'add_chapters': True,
                                                'add_infojson': 'if_exists',
                                                'add_metadata': True,
                                                'key': 'FFmpegMetadata'},
                                               {'already_have_thumbnail': False,
                                                'key': 'EmbedThumbnail'},
                                               {'key': 'FFmpegConcat',
                                                'only_multi_video': True,
                                                'when': 'playlist'}],
                            'retries': 5,
                            'writethumbnail': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                if ydl._download_retcode == 0:
                    a.set("成功下載 YouTube 影片")
        else:
            a.set(f"YouTube 下載失敗 {url}")
        i += 1
        bar['value'] = i
        root.update()
    if pdfs and combinePdf:
        pdf_files = [file for file in os.listdir() if file in pdfs]
        # Merge PDF files
        merger = PdfMerger()
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        # Save merged PDF as "merged.pdf"
        merger.write("合併.pdf")
        merger.close()
        # Delete original PDF files
        for pdf_file in pdf_files:
            os.remove(pdf_file)
        a.set("已合併 PDF")
    tk.Label(group).pack()
    tk.Button(group,
              text='關閉',
              command=root.destroy
              ).pack()


root = tk.Tk()
root.title('EMDL - 萬能下載器')

b64_data = requests.get("url").text
image = PhotoImage(data=b64_data)
root.tk.call('wm', 'iconphoto', root._w, image)
x = (root.winfo_screenwidth()/2) - 250
y = (root.winfo_screenheight()/2) - 250
root.geometry('500x400+%d+%d' % (x, y))
container = tk.LabelFrame(root, padx=15, pady=15, bd=0)
container.pack(fill='both', expand='yes')
containerA = tk.LabelFrame(container, padx=20, pady=10, text="毛哥EM製作")
containerA.pack(fill='both', expand='yes')
group = tk.LabelFrame(containerA, bd=0)
group.pack(fill='x', expand=True, side=tk.LEFT)
a = tk.StringVar()
tk.Label(group, text='EMDL - 萬能下載器', font=('Arial', 20)).pack()
status = tk.Label(group, textvariable=a, font=('Arial', 13))  # 狀態
a.set("正在找出剪貼簿連結\n並找出短網址真實位置")
status.pack()

# 列表
frame = tk.Frame(root)
scrollbar = tk.Scrollbar(frame)
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=6)
scrollbar.config(command=listbox.yview)


def start():
    global haveYouTube
    haveYouTube = False
    global haveGoogleDoc
    haveGoogleDoc = 0
    # 找連結
    urls = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', pyperclip.paste())
    redirected_urls = []
    for url in urls:
        response = requests.get(url)
        if "reurl.cc" in url:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            input_element = soup.find('input', {'id': 'url'})
            if input_element:
                value = input_element.get('value')
                redirected_urls.append(value)
                listbox.insert(tk.END, value)
        elif "piee.pw" in url:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            a_element = soup.find('p').find('a')
            if a_element:
                href = a_element.get('href')
                redirected_urls.append(href)
                listbox.insert(tk.END, href)
        else:
            redirected_urls.append(response.url)
            listbox.insert(tk.END, response.url)
        if "you" in response.url:
            haveYouTube = True
        elif "https://docs.google.com/document/" in response.url:
            haveGoogleDoc += 1
        a.set("已找到"+str(listbox.size())+"個有效連結\n並找出短網址真實位置")
    if redirected_urls:
        combine = tk.BooleanVar()
        listbox.pack()
        scrollbar.pack(side='right', fill='y')
        listbox.pack(side='left', fill='both', expand=True)
        frame.pack(fill='x')
        if haveYouTube or haveGoogleDoc > 0:
            a.set("已找到"+str(listbox.size())+"個有效連結\n請選擇下載格式")
            if haveYouTube:
                global ytFormatBox
                ytFormatBox = tk.LabelFrame(group, bd=0)
                ytFormatBox.pack()
                tk.Label(ytFormatBox, text="YouTube").pack(side='left')
                ytOptionList = ['mp3',"原始影片 (最快)", "mp4 (較慢)"]   # 選項
                global ytValue
                ytValue = tk.StringVar()
                ytValue.set('mp4')
                ytFormat = tk.OptionMenu(ytFormatBox, ytValue, *ytOptionList)
                ytFormat.pack(side='left')

            if haveGoogleDoc > 0:
                global fileFormatBox
                fileFormatBox = tk.LabelFrame(group, bd=0)
                fileFormatBox.pack()
                tk.Label(fileFormatBox, text="Google Doc").pack(side='left')
                fileOptionList = ['pdf', "docx", "odt",
                                  "rtf", "txt", "html", "epud"]   # 選項
                global fileValue
                fileValue = tk.StringVar()
                fileValue.set('pdf')
                fileFormat = tk.OptionMenu(
                    fileFormatBox, fileValue, *fileOptionList)
                fileFormat.pack(side='left')
                if haveGoogleDoc > 1:
                    global combineBox
                    combineBox = tk.LabelFrame(group, bd=0)
                    combineBox.pack()
                    check_btn1 = tk.Checkbutton(
                        combineBox, text='合併 PDF', variable=combine, command=lambda: print(combine.get()))
                    check_btn1.pack(side='left')
        else:
            a.set("已找到"+str(listbox.size())+"個有效連結\n會以原始格式下載")
        global blank
        blank = tk.Label(group)
        blank.pack(fill='x')
        global btn
        global combinePdf
        def combinePdf(): return combine.get()
        btn = tk.Button(group,
                        text='開始下載',
                        command=threading.Thread(
                            target=download, args=(redirected_urls,)).start,
                        pady=5,
                        padx=5
                        )
    else:
        a.set("沒有找到網址\n請先複製一段包含一個或多個連結的文字再執行程式")
        tk.Label(group).pack()
        btn = tk.Button(group,
                        text='關閉',
                        command=root.destroy
                        )
    btn.pack()


root.after(100, start)
root.mainloop()
