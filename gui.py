import pyperclip
import re
import requests
from bs4 import BeautifulSoup
import os
import yt_dlp
from PyPDF2 import PdfMerger
import tkinter as tk

# Download as PDF or original
def download():
  for url in redirected_urls:
    if "https://docs.google.com/document/" in url:
      pdf_url = url.split("/edit")[0] + "/export?format=pdf"
      response = requests.get(pdf_url)
      if response.status_code == 200:
        filename = os.path.basename(pdf_url)
        index = redirected_urls.index(url)
        filename = f"index{index}.pdf"
        with open(filename, 'wb') as file:
          file.write(response.content)
        a.set("成功下載歌譜" + {filename})
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
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        if ydl._download_retcode == 0:
          a.set("成功下載 YouTube 音樂")
    else:
      a.set(f"YouTube 下載失敗 {url}")

  if pdfs:
    pdf_files = [file for file in os.listdir() if file in pdfs]

    # Merge PDF files
    merger = PdfMerger()
    for pdf_file in pdf_files:
      merger.append(pdf_file)

    # Save merged PDF as "merged.pdf"
    merger.write("歌譜.pdf")
    merger.close()

    # Delete original PDF files
    for pdf_file in pdf_files:
      os.remove(pdf_file)
    a.set("已合併歌譜")
  tk.Button(root,
          text='關閉',
          command=root.destroy
          ).pack()
root = tk.Tk()
root.title('EMDL')
root.geometry('400x300')

a = tk.StringVar()  # 設定 a 為文字變數

tk.Label(root, text='EMDL', font=('Arial', 20)).pack()
mylabel = tk.Label(root, textvariable=a, font=('Arial', 16))  # 狀態
mylabel.pack()

a.set("正在檢查剪貼簿...")
# Get text from clipboard
text = pyperclip.paste()
urls = re.findall(
  r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

redirected_urls = []
pdfs = []
for url in urls:
  response = requests.get(url)
  if "reurl.cc" in url:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    input_element = soup.find('input', {'id': 'url'})
    if input_element:
      value = input_element.get('value')
      redirected_urls.append(value)
      a.set("找到", value)
  elif "piee.pw" in url:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    a_element = soup.find('p').find('a')
    if a_element:
      href = a_element.get('href')
      redirected_urls.append(href)
      a.set("找到", href)
    else:
      redirected_urls.append(response.url)
      a.set("沒有找到" + response.url + "的真實網址")
  else:
    redirected_urls.append(response.url)
    a.set("找到 " + response.url)
if redirected_urls:
  a.set("請選擇 YouTube 下載格式")
  btn = tk.Button(root,
          text='聲音檔',
          command=download
          )
  btn.pack()
else:
  a.set("沒有找到網址")
  btn = tk.Button(root,
          text='好吧',
          command=root.destroy
          )
  btn.pack()

root.mainloop()