# -*- coding: utf-8 -*-

import soundcloud
import os
import csv
import requests
import shutil

id = "YOUR_ID_HERE"
users_number = "130256332"

file_destination = "FINAL_LOCATION_OF_DL_FILES"

client = soundcloud.Client(client_id=id, redirect_uri='http://soundcloud.com/callback')

def save_favorites():

	"""Create CSV file with headers and then saves the users like to the CSV file."""

	with open("soundcloud_favs.csv", 'w', encoding='utf-8', newline='') as csv_file:
		
		vrai = True
		i = 0
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(['Track Title', 'Track URL'])
		
		while vrai:
			favs_list = client.get("/users/{}/favorites".format(users_number), client_id=id, offset=50*i)
			i += 1
			vrai = False
			for track in favs_list:
				vrai = True
				csv_writer.writerow([track.title, track.permalink_url])

def dl_missing():
	
	"""Downloads the missing favs, the list of already downloaded favs is in downloaded_favs.csv"""
	
	with open("downloaded_favs.csv", "r", encoding='utf-8', newline='') as dl_favs:
		with open("soundcloud_favs.csv", 'r', encoding='utf-8', newline='') as favs:

			dl_list = list(csv.reader(dl_favs, delimiter=','))
			
			fav_list = list(csv.reader(favs, delimiter=','))
			for ligne in fav_list:
				if ligne not in dl_list:
					os.system('soundscrape {}'.format(ligne[1]))
					
	shutil.move("soundcloud_favs.csv", "downloaded_favs.csv")
					
def move_files():
	
	files = os.listdir()
	
	for f in files:
		if '.mp3' in f:
			shutil.move(f, "D:\\Users\\Sofa\\Desktop\\musiques\\soundcloud\\")

save_favorites()
dl_missing()
move_files()
