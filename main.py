from logging import log
from tkinter import *
import tkinter as tkinter
from tkinter import font
from typing import Optional
from tkinter import ttk
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

root=Tk()
root.title("CapCadeau")
root.geometry("950x960+180+50")

logo=Canvas(root,width=950,height=880,bg="#46B8E1")
logo.place(x=0,y=10)

log=Label(logo,text="CapCadeau :",font=('arial',19,'bold'))
log.place(x=20,y=10)

de_la_part_de=Label(logo,text="De la part de :",bg="#46B8E1",font=('arial',15,'bold'),fg="#FFF")
de_la_part_de.place(x=260,y=80)

de_la_part_de_Entry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
de_la_part_de_Entry.place(x=260,y=120)

""""""
prenom=Label(logo,text="Prénom :",bg="#46B8E1",font=('arial',15,'bold'),fg="#FFF")
prenom.place(x=260,y=160)

PrenomEntry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
PrenomEntry.place(x=260,y=200)

""""""
nom=Label(logo,text="Nom :",bg="#46B8E1",font=('arial',15,'bold'),fg="#FFF")
nom.place(x=260,y=240)

nomEntry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
nomEntry.place(x=260,y=280)

""""""

email=Label(logo,text="Email d'envoi :",bg="#46B8E1",font=('arial',15,'bold'),fg="#FFF")
email.place(x=260,y=320)

emailEntry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
emailEntry.place(x=260,y=360)

offre=Label(logo,text="Choisir l'offre :",bg="#46B8E1",font=('arial',15,'bold'),fg="#FFF")
offre.place(x=260,y=400)

offreEntry = ttk.Combobox(logo,width=45,font=('arial',12),
                            values=["Bon d'échange menu Roseau + Eau + Café",
                                    "Cheque Cadeaux",
                                    "Grand Lac 1h Annecy","Grand Lac 1h30 Annecy","Bons d'échange APERO BATO Aigue"],)
offreEntry.place(x=260,y=440)

tarrif_cheque=Label(logo,text="Valeur du chèque cadeaux :",bg="#46B8E1",font=('arial',15,'bold'),fg="#FFF")
tarrif_cheque.place(x=260,y=480)

tarrif_chequeEntry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
tarrif_chequeEntry.place(x=260,y=520)

nombre=Label(logo,text="Nombre de bon cadeaux :",bg="#46B8E1",font=('arial',15,'bold'),fg="#FFF")
nombre.place(x=260,y=560)

nombreEntry=Entry(logo,width=50,relief=FLAT,font=('arial',12))
nombreEntry.place(x=260,y=600)

def recupdonnee():
    de_la_part_de = de_la_part_de_Entry.get()
    email = emailEntry.get()
    prenom = PrenomEntry.get()
    nom = nomEntry.get()
    offre = offreEntry.get()
    tarrif_cheque = tarrif_chequeEntry.get()
    nombre = int(nombreEntry.get())
    i = 0
    for i in range(0,nombre):
        if offre == "Bon d'échange menu Roseau + Eau + Café":
            browser  = webdriver.Chrome(ChromeDriverManager().install())
            browser.set_window_size(1280, 720)
            fb_name = ""
            fb_pass = ""
            browser.get('https://www.capcadeau.pro/espace-pro/login')
            browser.find_element_by_id("username").send_keys(fb_name)
            browser.find_element_by_id("password").send_keys(fb_pass)
            browser.find_element_by_xpath('/html/body/main/section/div/div/div[2]/div/div[1]/form/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/main/section[1]/div/div[2]/div[2]/a').click()
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[30]/h3/a').click()
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_offer").send_keys(de_la_part_de)
            browser.find_element_by_id('voucher_paymentAmount').clear()
            browser.find_element_by_id("voucher_paymentAmount").send_keys("0")
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/div/div/form/div[5]/div[3]/div/div[2]/div/div[4]/label').click()
            browser.find_element_by_id("voucher_customer_firstName").send_keys(prenom)
            browser.find_element_by_id("voucher_customer_lastName").send_keys(nom)
            browser.find_element_by_id("voucher_customer_email").send_keys(email)
            browser.find_element_by_id("voucher_submit").click()

        elif offre == "Grand Lac 1h Annecy" :
            browser  = webdriver.Chrome(ChromeDriverManager().install())
            browser.set_window_size(1280, 720)
            fb_name = "r.fourneuve@tourisme-participations.com"
            fb_pass = "Id19lu82&*"
            browser.get('https://www.capcadeau.pro/espace-pro/login')
            browser.find_element_by_id("username").send_keys(fb_name)
            browser.find_element_by_id("password").send_keys(fb_pass)
            browser.find_element_by_xpath('/html/body/main/section/div/div/div[2]/div/div[1]/form/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/main/section[1]/div/div[2]/div[2]/a').click()
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[5]/h3/a').click()
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_offer").send_keys(de_la_part_de)
            browser.find_element_by_id('voucher_paymentAmount').clear()
            browser.find_element_by_id("voucher_paymentAmount").send_keys("0")
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/div/div/form/div[6]/div[3]/div/div[2]/div/div[4]/label').click()
            browser.find_element_by_id("voucher_customer_firstName").send_keys(prenom)
            browser.find_element_by_id("voucher_customer_lastName").send_keys(nom)
            browser.find_element_by_id("voucher_customer_email").send_keys(email)
            browser.find_element_by_id("voucher_submit").click()
        
        elif offre == "Bons d'échange APERO BATO Aigue" :
            browser  = webdriver.Chrome(ChromeDriverManager().install())
            browser.set_window_size(1280, 720)
            fb_name = "r.fourneuve@tourisme-participations.com"
            fb_pass = "Id19lu82&*"
            browser.get('https://www.capcadeau.pro/espace-pro/login')
            browser.find_element_by_id("username").send_keys(fb_name)
            browser.find_element_by_id("password").send_keys(fb_pass)
            browser.find_element_by_xpath('/html/body/main/section/div/div/div[2]/div/div[1]/form/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/main/section[1]/div/div[2]/div[2]/a').click()
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[30]/h3/a').click()
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_offer").send_keys(de_la_part_de)
            browser.find_element_by_id('voucher_paymentAmount').clear()
            browser.find_element_by_id("voucher_paymentAmount").send_keys("0")
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/div/div/form/div[6]/div[3]/div/div[2]/div/div[4]/label').click()
            browser.find_element_by_id("voucher_customer_firstName").send_keys(prenom)
            browser.find_element_by_id("voucher_customer_lastName").send_keys(nom)
            browser.find_element_by_id("voucher_customer_email").send_keys(email)
            browser.find_element_by_id("voucher_submit").click()

        elif offre == "Grand Lac 1h30 Annecy" :
            browser  = webdriver.Chrome(ChromeDriverManager().install())
            browser.set_window_size(1280, 720)
            fb_name = "r.fourneuve@tourisme-participations.com"
            fb_pass = "Id19lu82&*"
            browser.get('https://www.capcadeau.pro/espace-pro/login')
            browser.find_element_by_id("username").send_keys(fb_name)
            browser.find_element_by_id("password").send_keys(fb_pass)
            browser.find_element_by_xpath('/html/body/main/section/div/div/div[2]/div/div[1]/form/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/main/section[1]/div/div[2]/div[2]/a').click()
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[6]/h3/a').click()
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_offer").send_keys(de_la_part_de)
            browser.find_element_by_id('voucher_paymentAmount').clear()
            browser.find_element_by_id("voucher_paymentAmount").send_keys("0")
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/div/div/form/div[6]/div[3]/div/div[2]/div/div[4]/label').click()
            browser.find_element_by_id("voucher_customer_firstName").send_keys(prenom)
            browser.find_element_by_id("voucher_customer_lastName").send_keys(nom)
            browser.find_element_by_id("voucher_customer_email").send_keys(email)
            browser.find_element_by_id("voucher_submit").click()

        elif offre == "Grand Lac 1h30 Annecy" :
            browser  = webdriver.Chrome(ChromeDriverManager().install())
            browser.set_window_size(1280, 720)
            fb_name = "r.fourneuve@tourisme-participations.com"
            fb_pass = "Id19lu82&*"
            browser.get('https://www.capcadeau.pro/espace-pro/login')
            browser.find_element_by_id("username").send_keys(fb_name)
            browser.find_element_by_id("password").send_keys(fb_pass)
            browser.find_element_by_xpath('/html/body/main/section/div/div/div[2]/div/div[1]/form/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/main/section[1]/div/div[2]/div[2]/a').click()
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[6]/h3/a').click()
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_offer").send_keys(de_la_part_de)
            browser.find_element_by_id('voucher_paymentAmount').clear()
            browser.find_element_by_id("voucher_paymentAmount").send_keys("0")
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/div/div/form/div[6]/div[3]/div/div[2]/div/div[4]/label').click()
            browser.find_element_by_id("voucher_customer_firstName").send_keys(prenom)
            browser.find_element_by_id("voucher_customer_lastName").send_keys(nom)
            browser.find_element_by_id("voucher_customer_email").send_keys(email)
            browser.find_element_by_id("voucher_submit").click()

        elif offre == "Cheque Cadeaux" :
            browser  = webdriver.Chrome(ChromeDriverManager().install())
            browser.set_window_size(1280, 720)
            fb_name = "r.fourneuve@tourisme-participations.com"
            fb_pass = "Id19lu82&*"
            browser.get('https://www.capcadeau.pro/espace-pro/login')
            browser.find_element_by_id("username").send_keys(fb_name)
            browser.find_element_by_id("password").send_keys(fb_pass)
            browser.find_element_by_xpath('/html/body/main/section/div/div/div[2]/div/div[1]/form/div[3]/button').click()
            browser.find_element_by_xpath('/html/body/main/section[1]/div/div[2]/div[2]/a').click()
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/h3/a').click()
            browser.find_element_by_id('voucher_voucherFreeAmount').clear()
            browser.find_element_by_id("voucher_voucherFreeAmount").send_keys(tarrif_cheque)
            browser.find_element_by_id("voucher_lastName").send_keys(" ")
            browser.find_element_by_id("voucher_offer").send_keys(de_la_part_de)
            browser.find_element_by_id('voucher_paymentAmount').clear()
            browser.find_element_by_id("voucher_paymentAmount").send_keys("0")
            browser.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/div/div/form/div[5]/div[3]/div/div[2]/div/div[4]/label').click()
            browser.find_element_by_id("voucher_customer_firstName").send_keys(prenom)
            browser.find_element_by_id("voucher_customer_lastName").send_keys(nom)
            browser.find_element_by_id("voucher_customer_email").send_keys(email)
            browser.find_element_by_id("voucher_submit").click()


executer=Button(logo,text="Executer",bg="green",fg="white",relief=FLAT,font=('arial',12),width=20,command=recupdonnee)
executer.place(x=400,y=630)



root.mainloop()

