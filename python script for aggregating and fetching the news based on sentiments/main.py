import tkinter as tk
import aylien_news_api
from tkinter import *
from aylien_news_api.rest import ApiException


def CreateWidgets():

    searchLabel = Label(root, text="SEARCH FOR : ", bg="turquoise4", font=('Helvetica', 10))
    searchLabel.grid(row=0, column=0, padx=5, pady=5)

    searchText = Entry(root, width=50, textvariable=searchNews)
    searchText.grid(row=0, column=2, pady=5)

    searchButton = Button(root, text="SEARCH", width=20, command=SearchNews)
    searchButton.grid(row=0, column=3, padx=5, pady=5)

    allRadioBtn = Radiobutton(text="All", variable=s, value='neutral', bg="turquoise4", font=('Helvetica',10))
    allRadioBtn.grid(row=1, column=1, padx=5, pady=5)

    goodRadioBtn = Radiobutton(text="GOOD NEWS", variable=s, value='positive', bg="turquoise4", font=('Helvetica', 10))
    goodRadioBtn.grid(row=1, column=2, padx=5, pady=5)

    badRadioBtn = Radiobutton(text="BAD NEWS", variable=s, value='negative', bg="turquoise4", font=('Helvetica', 10))
    badRadioBtn.grid(row=1, column=3, padx=5, pady=5)

    s.set('neutral')

    root.newsResults = Text(root, width=70, height=30)
    root.newsResults.grid(row=2, column=1, columnspan=3, padx=5, pady=5)


def SearchNews():

    searchFor = searchNews.get()
    newsType = s.get()

    aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = "b2adff8a"
    aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = "6034baed6a768a178e3013128ce47838"

    api_instance = aylien_news_api.DefaultApi()

    otps = {
        'title' : searchFor,
        'language' : ['en'],
        'sentiment_title_polarity' : newsType,
        'published_at_start' : 'NOW-7DAYS',
        'published_at_end' : 'NOW',
    }

    try:

        count = 1
        api_response = api_instance.list_stories(**otps)

        for news in api_response.stories:
            storyTitle = news.title
            storySource = news.source.name
            storyBody = news.body
            storyDate = news.published_at

            displayNews = "\n\n"+str(count)+". "+storyTitle+"\n\nSOURCE : "+storySource+\
                          "| PUBLISHED ON : "+str(storyDate)+"\n\n"+storyBody

            root.newsResults.insert('1.0', displayNews)

            count = count + 1


    except ApiException as e:

        print("Exception when calling DefaultApi->list_stories: $sn" % e)


root = tk.Tk()

root.title("PyNewsAggregator")
root.resizable(False, False)
root.config(bg = "turquoise4")
root.geometry("700x575")

searchNews = StringVar()
s = StringVar()

CreateWidgets()

root.mainloop()