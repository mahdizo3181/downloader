import urllib.request
import time
from os import system as terminal, name as os_name


def handle_progress(block_num, block_size, total_size):
    read_data = 0
    temp = block_num * block_size
    read_data = temp + read_data
    remaining_size = total_size - read_data
    if remaining_size <= 0:
        downloaded_percentage = 100
        remaining_size = 0
    else:
        downloaded_percentage = int(((total_size - remaining_size) / total_size) * 100)
    print("==", f"Read date : {read_data}", " : ", f"Remaining size : {remaining_size}", " : ", f"{downloaded_percentage}% ", " : ", f"Total size : {total_size}", "==")
    if downloaded_percentage == 100:
        terminal('clear') if os_name != "nt" else terminal('cls')


file_name = input("please enter txt file name : ")


def download_file():
    with open(f"{file_name}.txt", "r") as links:
        link = links.readlines()
    for i in range(0, len(link)):
        download_url = link[i]
        print("Downloaded data: Remaining size: Downloaded percentage: Total size")
        save_location = f"{i+1}"
        urllib.request.urlretrieve(download_url, save_location, handle_progress)
        print(f"======================================  Done  ======================================  file: {save_location}")
        print("###############  Wait a few seconds to download the next file  ###############")
        time.sleep(4)


download_file()

