import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

# list of currencies
currencyList = ['AED', 'AUD', 'BHD', 'BRL', 'CAD', 'CNY', 'EUR', 'HKD', 'INR', 'USD']


# gui for widget
def CreateWidjets():

    inputAMTL = Label(root, text='ENTER THE AMOUNT : ', bg='SpringGreen4')
    inputAMTL.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

    inputAMTText = Entry(root, width=20, textvariable=getAMT)
    inputAMTText.grid(row=1, column=3, columnspan=2, pady=10)

    fromLabel = Label(root, text='FROM : ', bg='SpringGreen4')
    fromLabel.grid(row=2, column=1)

    root.fromCombo = ttk.Combobox(root, values=currencyList)
    root.fromCombo.grid(row=2, column=2)

    toLabel = Label(root, text='TO : ', bg='SpringGreen4')
    toLabel.grid(row=2, column=3)

    root.toCombo = ttk.Combobox(root, values=currencyList)
    root.toCombo.grid(row=2, column=4)

    convertButton = Button(root, text='CONVERT', width=52, command=Convert)
    convertButton.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

    outputAMTL = Label(root, text='CONVERTED AMOUNT : ', font=('Helvetica',10), bg='SpringGreen4')
    outputAMTL.grid(row=4, column=2, columnspan=2, pady=50)

    root.outputAMTAns = Label(root, font=('Helvetica',20), bg='SpringGreen4')
    root.outputAMTAns.grid(row=4, column=3, columnspan=2, pady=50)


# define convert function
def Convert():

    # fetch the user input value
    inputAmt = float(getAMT.get())
    fromCur = root.fromCombo.get()
    toCur = root.toCombo.get()

    # api key of online converter
    apiKey = "9MUQEX9RHBLGOPH3"

    # storing the base url
    baseURL = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    # storing the complete URL
    inputURL = baseURL + "&from_currency=" + fromCur\
               + "&to_currency=" + toCur + "&apikey=" + apiKey

    # return the response to user by get method
    requestObj = requests.get(inputURL)

    # convert json data to python dictionary
    result = requestObj.json()

    # getting the exchange rate
    exchangeRate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])

    # calculating the converted amount and rounding the decimal
    calculateAmt = round(inputAmt * exchangeRate, 2)

    print(exchangeRate)

    # display the result
    root.outputAMTAns.config(text=str(calculateAmt))


# create object of tk class
root = tk.Tk()

root.geometry("400x250")
root.resizable(False, False)
root.title("PuCurrency Converter")
root.config(bg='SpringGreen4')

getAMT = StringVar()

CreateWidjets()

root.mainloop()