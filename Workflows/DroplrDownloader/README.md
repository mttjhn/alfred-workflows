Droplr Downloader ([Download](https://raw.github.com/mttjhn/alfred-workflows/master/Workflows/DroplrDownloader/DroplrDownloader.alfredworkflow))
=====================

This is a quick workflow that I made to grab files from Droplr after uploading a screenshot or screencast. While one of Droplr's nicest features is the ability to grab a screenshot and simply paste a short URL into a chat window or email, there are times when I don't want to use the Droplr URL, but instead attach an image to my email, or use the image in a document. This workflow automates all the clicks you have to go through to get that image downloaded and renamed, ready for an email or document. By default, it will save the images/files to a specific folder (that you should change if you're going to use this). You will need to edit the `Download.py` file and adjust the `DOWNLOAD_PATH` variable to your specific needs. Also, you will need to edit the `PrepareDownload.py` file to adjust the `URL_CHECK` variable to the type of URL that Droplr generates for you (my account is set up with a custom domain).

## Requirements
1. [Alfred App 3](http://www.alfredapp.com/#download)
1. [Alfred Powerpack](https://buy.alfredapp.com/)

## Commands
- `dprdown`
    * Looks up the URL that's currently in the clipboard and provides an option to perform the download for that URL. If a valid URL is not found in the clipboard, an error message will be shown to the user.

## Contributors
- [@mttjhn](https://github.com/mttjhn)
