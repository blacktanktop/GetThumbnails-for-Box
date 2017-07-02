# -*- coding: utf-8 -*-

# ------------------------------------
# python modules
# ------------------------------------

import os
import subprocess
import time
import argparse as ap
import pandas as pd
from boxsdk import OAuth2
from boxsdk import Client

# ------------------------------------
# own python modules
# ------------------------------------

from constants import *

# ------------------------------------
# Main function
# ------------------------------------

def main(args):
    print(args)
    # id and token
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret
    ACCESS_TOKEN = args.ACCESS_TOKEN
    # parent folder_id
    parent_folder_id = args.folder_id
    # out_dir
    out_dir = args.out_dir
    # thumbnails minmal size
    size = int(args.size)
    # Authorization with oauth2
    oauth2 = OAuth2(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN)
    client = Client(oauth2)
    child_folder = client.folder(folder_id = parent_folder_id).get()
    child_folder_id = pd.DataFrame.from_dict(child_folder.item_collection['entries'])
    #To get thumbnails in child_folders
    for i, j in enumerate(child_folder_id["id"]):
        folder = client.folder(folder_id = j).get()
        # print folder name to get thumbnail images
        print('folder name: ' + folder['name'])
        folder_name = folder['name']
        # get all file information as dataframe
        img = pd.DataFrame.from_dict(folder.item_collection['entries'])
        # remove " "(space) and "&" and "'"from img["name"]
        img["name"] = img['name'].str.replace(' ', '')
        img["name"] = img['name'].str.replace('&', '')
        img["name"] = img['name'].str.replace('\'', '')
        img["name"] = img['name'].str.replace('(', '')
        img["name"] = img['name'].str.replace(')', '')
        img["name"] = img['name'].str.replace('（', '')
        img["name"] = img['name'].str.replace('）', '')
        # make thumbnail dir, 
        SAVE_DIR = out_dir + "/" + "/thumbnail/" + folder_name
        if not os.path.isdir(SAVE_DIR):
            os.makedirs(SAVE_DIR)
        # get all thumbnails in folder_id you set
        for i, (id, name) in enumerate(zip(img["id"], img["name"])):
            img_save_path = SAVE_DIR + "/" + img["name"][i].rstrip('.psd') + "_thumnail.jpg"
            file_id = img["id"][i]
            cmd = 'curl \"https://api.box.com/2.0/files/{0}/thumbnail.jpg?min_height={1}&min_width={2}\" -H \"Authorization: Bearer {3}\" > {4}'.format(file_id, size, size, ACCESS_TOKEN, img_save_path)
            print(cmd)
            print(i + 1, "/", len(img["id"]))
            subprocess.call(cmd, shell = True)
            time.sleep(5.0) #sleep(秒指定)
            #subprocess.call(cmd.strip().split(" "))

