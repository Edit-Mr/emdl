# worship-download

複製歌單後執行即可自動下載 Google Doc 歌譜 PDF，以及 YouTube 音檔

歌譜會以原順序合併成一個 PDF 檔案，音檔會依序下載成 MP3 檔案，其他雲端硬碟檔案會直接下載。

## 可處理的短網址服務

以下為目前實測可處裡的服務商，若有需要可自行新增，或是提出 issue。

- [x] [bit.ly](https://bitly.com/)
- [x] [tinyurl](https://tinyurl.com/)
- [x] [piee.tw](https://piee.tw)
- [x] [pse.is](https://pse.is/)
- [x] [reurl.cc](https://reurl.cc/)
<!-- - [ ] [](https://) -->

## 安裝

### 安裝 Python

請先安裝 Python 3.6 以上版本，並確認已經加入環境變數。

### 安裝套件

```bash
pip install -r requirements.txt
```

或是

```bash
pip install pyperclip requests beautifulsoup4 yt_dlp PyPDF2
```

## 使用

### 執行

```bash
python main.py
```

或是雙擊 `執行.bat` 檔案
