import requests
import customtkinter

def mainProgram():
    customtkinter.set_appearance_mode('system')
    customtkinter.set_default_color_theme('green')
    global root
    root =  customtkinter.CTk()
    root.geometry("315x450")
    root.title('Currency Converter')
    root.resizable(False,False)
    root.iconbitmap("money.ico")
    appName = customtkinter.CTkLabel(master=root,text="Currency Converter",font=('Helvetica',16))
    appName.pack()
    apiInfo = customtkinter.CTkLabel(master=root,text="exchange rates can be little outdated",font=('Helvetica',13))
    apiInfo.pack()
    EuroUsd = customtkinter.CTkButton(master=root,text="Euro to USD",width=135,height=25,corner_radius=13,command=EuroUSD)
    EuroUsd.pack(pady=5)
    UsdEuro = customtkinter.CTkButton(master=root,text="USD to Euro",width=135,height=25,corner_radius=13,command=USDEuro)
    UsdEuro.pack(pady=5)
    root.mainloop()
def EuroUSD():
    global Euro
    Euro = customtkinter.CTkEntry(master=root,width=155,height=35,corner_radius=15,placeholder_text="Euro")
    Euro.pack(pady=7)
    convertButton = customtkinter.CTkButton(master=root,height=25,width=135,corner_radius=13,text="Convert",command=convert_euro_to_usd)
    convertButton.pack(pady=7)
def USDEuro():
    global USD
    USD = customtkinter.CTkEntry(master=root,width=155,height=35,corner_radius=15,placeholder_text="USD")
    USD.pack(pady=7)
    convertButton = customtkinter.CTkButton(master=root,height=25,width=135,corner_radius=13,text="Convert",command=convert_usd_to_eur)
    convertButton.pack(pady=7)
def convert_euro_to_usd():
    url = "https://rest.coinapi.io/v1/exchangerate/EUR/USD"
    headers = {
        "X-CoinAPI-Key": "Insert-Your-API-Key-Here"
    }
    value = Euro.get()
    response = requests.get(url,headers=headers)
    info = response.json()
    rateValue = info['rate']
    buyingValue = float(value) * float(rateValue)
    formated_rate = "{:.2f}".format(buyingValue)
    conversion_value = customtkinter.CTkLabel(master=root,text="For " + str(value) + "€ " + "You can buy :" + formated_rate + "$",font=('Helvetica',16))
    conversion_value.pack(pady=6)
    conversion_value.after(6500,conversion_value.destroy)
def convert_usd_to_eur():
    url = "https://rest.coinapi.io/v1/exchangerate/USD/EUR"
    headers = {
        "X-CoinAPI-Key": "Insert-Your-API-Key-Here"
    }
    value = USD.get()
    response = requests.get(url,headers=headers)
    info = response.json()
    rateValue = info['rate']
    buyingValue = float(value) * float(rateValue)
    formated_rate = "{:.2f}".format(buyingValue)
    conversion_value = customtkinter.CTkLabel(master=root,text="For " + str(value) + " $ " + "You can buy :" + formated_rate + " €",font=('Helvetica',16))
    conversion_value.pack(pady=6)
    conversion_value.after(6500,conversion_value.destroy)
mainProgram()