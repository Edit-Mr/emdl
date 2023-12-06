# worship-download

複製歌單後執行即可自動下載 Google Doc 歌譜 PDF，以及 YouTube 音檔

樂譜將按照原始順序合併為一個 PDF 檔案，音檔將按順序下載為 MP3 檔案，其他雲端硬碟檔案將直接下載。

## 支援的短網址服務

以下是目前經過測試可處理的服務商，如有需要，可自行新增或提出問題。

- [x] [bit.ly](https://bitly.com/)
- [x] [tinyurl](https://tinyurl.com/)
- [x] [piee.tw](https://piee.tw)
- [x] [pse.is](https://pse.is/)
- [x] [reurl.cc](https://reurl.cc/)
<!-- - [ ] [](https://) -->

## 使用方式

複製歌單後執行即可

### Windows

從 [release 頁面](https://github.com/Edit-Mr/worship-download/releases/tag/v1.0) 下載 `worship.exe`，雙擊執行即可，無須安裝。

### 手動編譯

#### 安裝 Python

首先，安裝 Python 3.8 以上版本，確保已添加至環境變數。

#### 安裝相依套件

```bash
pip install -r requirements.txt
```
或

```bash
pip install pyperclip requests beautifulsoup4 yt_dlp PyPDF2
```
#### 使用

```bash
python main.py
```
或雙擊 執行.bat 檔案。
