import os
import json
import shutil
import datetime as dt
from pathlib import Path


bookmarks_file =  os.path.abspath('/mnt/c/Users/User/AppData/Local/Google/Chrome/User Data/Default/Bookmarks')
folder_name = "ulubione jbzd"


with open(bookmarks_file, "r") as f:
    data = json.load(f)
links = []
timestamps = []
dates = []

for item in data['roots']['bookmark_bar']['children']:
    if item['type'] == 'folder':
        # print(item['name'])
        for sub_item in item['children']:
            if sub_item['type'] == 'folder' and sub_item['name'] == 'ulubione jbzdy':
                for sub_sub_item in sub_item['children']:
                    if sub_sub_item['type'] == 'url':
                        links.append(sub_sub_item['url'])
                        timestamps.append(sub_sub_item['date_added'])
                        # print(sub_sub_item['url'], sub_sub_item['date_added'])
                        # print(sub_sub_item['date_added'])
                    # if items_inside['name'] == 'ulubione jbzdy':
                    #     for items_inside2 in items_inside['children']:
                    #         print(items_inside2['url'])
       
# for link in links:
#     print(link)

for timestamp in timestamps:
    date = float(timestamp)

    # Konwersja timestampa na datę i czas
    win32_epoch = dt.datetime(year=1601, month=1, day=1)
    
    date_from_win = win32_epoch + dt.timedelta(seconds=date/1e6)

    # Formatowanie daty do postaci "dd-mm-yy"
    date_str = date_from_win.strftime('%d-%m-%y')

    # Wyświetlenie daty
    dates.append(date_str)
# children = []
slownik = {}
for key, value in zip(date_str, links):
    slownik.setdefault(key, []).append(value)

print(slownik)
# for item in data['roots']['bookmark_bar']['children']:
#     # if obj.get('name') == 'ulubione jbzdy':
#     if item['type'] == 'folder' and item['name'] == 'inne':
#         print(f'Folder: {item["url"]}')

#         # children = obj['children']
#         # children.append(obj)
#         # print(obj)

# print(children)

# # pobranie id folderu z zakładkami
# for folder in data["roots"]["bookmark_bar"]["children"]:
#     if folder.get("name") == folder_name:
#         folder_id = folder["id"]
#         break

# # pobranie zakładek z wybranego folderu
# bookmarks = []
# def extract_bookmarks(folder):
#     for item in folder["children"]:
#         if "children" in item:
#             extract_bookmarks(item)
#         elif item["type"] == "url":
#             item["date_added"] = int(item["date_added"])
#             bookmarks.append(item)
            
# extract_bookmarks(data["roots"]["bookmark_bar"]["children"][0])

# # grupowanie zakładek po dacie utworzenia
# for bookmark in bookmarks:
#     url = bookmark["url"]
#     title = bookmark["name"]
#     date_added = bookmark["date_added"] // 1000000  # przeliczenie czasu z mikrosekund na sekundy
#     date = datetime.datetime.fromtimestamp(date_added).strftime('%d-%m-%y') #formatowanie daty do postaci dd-mm-rr
    
#     #tworzenie folderu z datą, jeśli jeszcze nie istnieje
#     if not os.path.exists(date):
#         os.makedirs(date)
    
#     # przeniesienie zakładki do odpowiedniego folderu z datą
#     destination = os.path.join(date, title + ".url")
#     with open(destination, "w") as f:
#         f.write("[InternetShortcut]\nURL=" + url + "\n")
        
# print("Zakładki zostały pogrupowane.") 

# # utworzenie folderu na pulpicie i przeniesienie do niego wszystkich folderów z zakładkami
# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
# folder_path = os.path.join(desktop_path, "Grupowane Zakładki")
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
# for folder in os.listdir():
#     if os.path.isdir(folder) and folder not in ["__pycache__", "venv", "Grupowane Zakładki"]:
#         shutil.move(folder, folder_path)
# print("Foldery z zakładkami zostały przeniesione do folderu 'Grupowane Zakładki' na pulpicie.")
