from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from tkinter import filedialog
import os, cv2, json, requests, urllib.request, tkinter as tk

root = tk.Tk()

root.geometry("530x530")
root.title("Instagram Post Download")
root.config(background="deepskyblue4")

def CreateWidgets():
    download_path_label = Label(root, text="Save To : ", background="deepskyblue4")
    download_path_label.grid(row=0, column=0, padx=5, pady=5)

    root.download_path = Entry(root, width=30, textvariable=dwl_path)
    root.download_path.grid(row=0, column=1, columnspan=2, pady=5)

    path_label_button = Button(root, text="Browse", command=Browse)
    path_label_button.grid(row=0, column=3, padx=5, pady=5)

    urlLabel = Label(root, text="Instagram Url : ", background="deepskyblue4")
    urlLabel.grid(row=1, column=0, padx=5, pady=5)

    root.urlEntry = Entry(root, width=30, textvariable=instaURL)
    root.urlEntry.grid(row=1, column=1, columnspan=2, pady=5)

    dwlBtn = Button(root, text="Download", command=postDownload, highlightbackground = "green")
    dwlBtn.grid(row=1, column=3, padx=5, pady=5)

    root.resultLabel = Label(root, text="Results : ", background="deepskyblue4")
    root.resultLabel.grid(row=2, column=0, padx=5, pady=5)

    root.dwlLabel = Label(root, textvariable=dwlText, background="deepskyblue4")
    root.dwlLabel.grid(row=3, column=0, padx=5, pady=5)

    root.previewLabel = Label(root, text='Preview', background="deepskyblue4")
    root.previewLabel.grid(row=4, column=0, padx=5, pady=5)

def Browse():
    path_text = filedialog.askdirectory()
    root.download_path.insert('0', path_text)

def postDownload():
    download_path = dwl_path.get() + '\\'
    
    insta_posts = requests.get(instaURL.get())
    soup = BeautifulSoup(insta_posts.text, parser="html.parser")
    script = soup.find('script', text=re.compile('window._sharedData'))
    parse_json = script.text.split(' = ',1)[1].rstrip(';')
    
    data = json.loads(parse_json)
    base_data = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    
    typename = base_data['__typename']

    if typename == 'GraphImage':
        display_url = base_data['display_url']
        file_name = base_data['taken_at_timestamp']
        downloadPath = download_path + str(file_name) + ".jpg"
        
        if not os.path.exists(downloadPath):
            urllib.request.urlretrieve(display_url, downloadPath)
            image = Image.open(downloadPath)
            image = image.resize((90, 90), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)

            imagelabel = Label(root)
            imagelabel.grid(row=4, column=0, padx=5, pady=5)
            imagelabel.config(image=image)
            imagelabel.photo = image

            imagetext = Label(root, text=str(file_name)+'.jpg', background="deepskyblue4")
            imagetext.grid(row=5, column=0, padx=5, pady=5)

            prev_t = dwlText.get()
            new_t = prev_t + "\n" + str(file_name) + ".jpg Downloaded"
            root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
            dwlText.set(new_t)
        
        else:
            prev_t = dwlText.get()
            new_t = prev_t + "\n" + str(file_name) + ".jpg Exists"
            root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
            dwlText.set(new_t)
    
    elif typename == 'GraphVideo':
        video_url = base_data['video_url']
        file_name = base_data['taken_at_timestamp']
        downloadPath = download_path + str(file_name) + ".mp4"

        if not os.path.exists(downloadPath):
            urllib.request.urlretrieve(video_url, downloadPath)
            vid = cv2.VideoCapture(downloadPath)
            ret, frame = vid.read()

            if not os.path.exists(download_path + "/VideoIcons/"):
                os.mkdir(download_path + "/VideoIcons/")

            video_icon = download_path + "/VideoIcons/" + str(file_name) + ".jpg"
            cv2.imwrite(video_icon, frame)
            
            icon = Image.open(video_icon)
            icon = icon.resize((90, 90), Image.ANTIALIAS)
            icon = ImageTk.PhotoImage(icon)

            imagelabel = Label(root)
            imagelabel.grid(row=4, column=0, padx=5, pady=5)
            imagelabel.config(image=icon)
            imagelabel.photo = icon

            imagetext = Label(root, text=str(file_name)+'.mp4', background="deepskyblue4")
            imagetext.grid(row=5, column=0, padx=5, pady=5)

            prev_t = dwlText.get()
            new_t = prev_t + "\n" + str(file_name) + ".mp4 Downloaded"
            root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
            dwlText.set(new_t)
        
        else:
            prev_t = dwlText.get()
            new_t = prev_t + "\n" + str(file_name) + ".mp4 Exists"
            root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
            dwlText.set(new_t)
            root.dwlLabel.config(text=str(file_name) + ".mp4 has been already downloaded")
    
    elif typename == 'GraphSidecar':
        shortcode = base_data['shortcode']
        response = requests.get(f"https://www.instagram.com/p/" + shortcode + "/?__a=1").json()
        post_n = 1; i = 0

        for edge in response['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
            file_name = response['graphql']['shortcode_media']['taken_at_timestamp']
            downloadPath = download_path + str(file_name) + "-" + str(post_n)
            is_video = edge['node']['is_video']

            if not is_video:
                display_url = edge['node']['display_url']
                downloadPath += ".jpg"

                if not os.path.exists(downloadPath):
                    urllib.request.urlretrieve(display_url, downloadPath)
                    image = Image.open(downloadPath)
                    image = image.resize((90, 90), Image.ANTIALIAS)
                    image = ImageTk.PhotoImage(image)

                    imagelabel = Label(root)
                    imagelabel.grid(row=4, column=i, padx=5, pady=5)
                    imagelabel.config(image=image)
                    imagelabel.photo = image

                    imagetext = Label(root, text=str(file_name)+'.jpg', background="deepskyblue4")
                    imagetext.grid(row=5, column=i, padx=5, pady=5)
                    

                    prev_t = dwlText.get()
                    new_t = prev_t + "\n" + str(file_name) + "-" + str(post_n) + ".jpg Downloaded"
                    root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
                    dwlText.set(new_t)
                    i += 1
                
                else:
                    prev_t = dwlText.get()
                    new_t = prev_t + "\n" + str(file_name) + "-" + str(post_n) + ".jpg Exists"
                    root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
                    dwlText.set(new_t)
            
            else:
                video_url = edge['node']['video_url']
                downloadPath += '.mp4'

                if not os.path.exists(downloadPath):
                    urllib.request.urlretrieve(video_url, downloadPath)
                    vid = cv2.VideoCapture(downloadPath)
                    ret, frame = vid.read()

                    if not os.path.exists(download_path + "/VideoIcons/"):
                        os.mkdir(download_path + "/VideoIcons/")

                    video_icon = download_path + "/VideoIcons/" + str(file_name) + ".jpg"
                    cv2.imwrite(video_icon, frame)
                    
                    icon = Image.open(video_icon)
                    icon = icon.resize((90, 90), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(icon)

                    imagelabel = Label(root)
                    imagelabel.grid(row=4, column=i, padx=5, pady=5)
                    imagelabel.config(image=img)
                    imagelabel.photo = img

                    imagetext = Label(root, text=str(file_name)+'.mp4', background="deepskyblue4")
                    imagetext.grid(row=5, column=i, padx=5, pady=5)

                    prev_t = dwlText.get()
                    new_t = prev_t + "\n" + str(file_name) + "-" + str(post_n) + ".mp4 Downloaded"
                    root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
                    dwlText.set(new_t)
                    i += 1
                
                else:
                    prev_t = dwlText.get()
                    new_t = prev_t + "\n" + str(file_name) + "-" + str(post_n) + ".mp4 Exists"
                    root.dwlLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
                    dwlText.set(new_t)
            post_n += 1

dwl_path = StringVar()
instaURL = StringVar()
dwlText = StringVar()

CreateWidgets()

root.mainloop()