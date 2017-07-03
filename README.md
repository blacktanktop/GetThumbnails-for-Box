# GetThumbnails-for-Box

To get thumbnails with using Box API

# Introduction

This scripts (get_thumbnail.py) can get thumbnails of many image files (psd files) in Box with [Box API](https://developer.box.com/v2.0/reference)


# Requirements

*  python3.x.x (recommend Python 3.5.2, or Anaconda3-4.2.0 (conda create for Python 3.5.2))
*  pandas
*  [box-python-sdk](https://github.com/box/box-python-sdk) 

# How to make enviroment
Recommend to make enviroment with [pyenv](https://github.com/pyenv/pyenv)

```
git clone https://github.com/takatsugukosugi/GetThumbnails-for-Box.git
cd GetThumbnails-for-Box
# Make anaconda3 enviroment
pyenv install anaconda3-4.2.0
pyenv local anaconda3-4.2.0
# Make different name anaconda3 enviroment to use Python 3.5.2
conda create -n "ILLUSTRATE" python=3.5.2 anaconda
# Set pyenv enviroment for the current directory
pyenv local anaconda3-4.2.0/envs/ILLUSTRATE
# Install boxsdk
pip install boxsdk
```
---
If you don't use anaconda, you need to install pandas

```
pip install pandas
```
---

If you finished making enviroment, type shown blow command

```
python get_thumbnail.py -h
```

and then return this

```
usage: get_thumbnail.py [-h] [--version] {oneFolder,manyFolders} ...

get_thumbnail.py -- Getting thumbnails with using BOX API

positional arguments:
  {oneFolder,manyFolders}
    oneFolder           Get thumbnails in one folder.
    manyFolders         Get thumbnails in many folders.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
```
---
Second, to get client id and client secret, create a developer account and application in [Box](https://developer.box.com/v2.0/docs/configuring-box-platform)
Third, generate and copy developer token in your application (as same as client id and client secret)
Finally, add your client id and your client secret in ./BOX/constants.py and use developer token as argument
```
# Paste the client id, client secret
client_id = " " #Paste your client_id
client_secret = " " #Paste your client_secret
```

# Usage

This scripts (get_thumbnail.py) can get thumbnails (output are jpg files) of many image files (psd files) in Box with Box API

You can get thumbnails of .psd files in one directroy and you should set folder_id, developer token, min size height or width, output directroy.

```
python get_thumbnail.py oneFolder -i [folder_id] -t [developer token] -s [size (for example:360)] --outdir [output dir]
```

You can get thumbnails of .psd files in some directroies and you should set parent_folder_id, developer token, min size height or width, output directroy.

```
python get_thumbnail.py manyFolders -i [parent_folder_id] -t [developer token] -s [size (for example:360)] --outdir [output dir]
```


# Caution

It is developing now, such as  Error handling and automatic Authorization with refresh token.
