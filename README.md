# EMDL

你敢複製，我就敢下載  
絕對是你人生中用過最好用的下載器。
音樂和影片都會是全網最高畫質，MP3不但會有專輯縮圖還會嵌入作者資訊和發佈專櫃及年份。

## 簡介

你只需要複製一個歌單文字，比如說:

> 2/9 歌單來囉，久等了！
> 1.被造的意義 - G / 150bpm  
> 連結：https://reurl.cc/L6LxjL  
> 歌譜：https://reurl.cc/L6Lx1L  
> 2.不能被搖動-B  
> 連結：https://youtu.be/eABWf8MvqKk?si=z9jF2rfTEfsiBz2j  
> 歌譜：https://tinyurl.com/ylalc8j6  
> 3.愛降下-E  
> 連結：https://youtu.be/6KYqygcT2Uk?si=2vBOO1Kt9wnKYEJX  
> 歌譜：https://tinyurl.com/yvkwadk3  
> 4.All Hail King Jesus 稱頌主耶穌 - A / 75bpm  
> 連結：https://reurl.cc/o5ndzg  
> 中文：https://reurl.cc/z6v8m6  
> 歌譜：https://reurl.cc/edexjx  
> 奉獻：3  
> 回應：4  
> 咱們週六見，一起敬拜愛我們的天父：）

你連整理連結都不用，直接整段複製。執行即可自動下載 Google Doc 歌譜 PDF，以及 YouTube 音檔。樂譜將按照原始順序合併為一個 PDF 檔案，音檔將按順序下載為 MP3 檔案，其他雲端硬碟檔案將直接下載。

如果你想要自訂下載格格式，或是不要合併PDF，請使用 GUI 版本。


## 支援的服務

以下是目前經過測試可處理的服務商，如有需要，可自行新增或提出 issue。

### 檔案

- [x] [Google Drive](https://drive.google.com/)
- [X] [Google Doc](https://docs.google.com/)
- [X] [YouTube](https://www.youtube.com/)
- [X] [所有 youtube-dl 支援的 1225 個網站](https://ytdl-org.github.io/youtube-dl/supportedsites.html)
    - 我不會說酸鹼值網站也能下載

### 短網址

- [x] [bit.ly](https://bitly.com/)
- [x] [tinyurl](https://tinyurl.com/)
- [x] [piee.tw](https://piee.tw)
- [x] [pse.is](https://pse.is/)
- [x] [reurl.cc](https://reurl.cc/)
<!-- - [ ] [](https://) -->

## 使用方式

請先複製一段包含一個或多個連結的文字再執行程式即可。

如果有使用影片轉檔功能，請確保已安裝 [FFmpeg](https://ffmpeg.org/) 並已添加至環境變數。

### 簡易版

#### Windows

從 [release 頁面](https://github.com/Edit-Mr/worship-download/releases/tag/v1.0) 下載 `worship.exe`，雙擊執行即可，無須安裝。


### GUI 版本

#### Windows

從 [release 頁面](https://github.com/Edit-Mr/worship-download/releases/tag/v1.0) 下載 `emdl.exe`，雙擊執行即可，無須安裝。

#### 手動編譯

##### 安裝 Python

首先，安裝 Python 3.8 以上版本，確保已添加至環境變數。

##### 安裝相依套件

```bash
pip install -r requirements.txt
```
或

```bash
pip install pyperclip requests beautifulsoup4 yt_dlp PyPDF2 tk
```
##### 使用

```bash
python main.py
# 或
python gui.py
# 或雙擊 emdl.bat 檔案
```