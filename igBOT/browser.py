from re import T
from tkinter.font import BOLD
from selenium import webdriver
import time
import userData as ud
import tkinter as tk
from tkinter import *
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, JavascriptException

form = tk.Tk()
form.title("Instagram'da Takip Etmeyenleri Yakala!")
form.geometry("500x500")
form.configure(background="#2c2c2e")
form.iconbitmap(default="instagram.ico")

label1 = tk.Label(text="Kullanıcı Adı", font=("Helvetica", 9, BOLD), fg="white", bg="#4a494d")
label1.place(x=10, y=20)
label2 = tk.Label(text="Şifre", font=("Helvetica", 9, BOLD), fg="white", bg="#4a494d")
label2.place(x=10, y=50)

username1 = tk.Entry()
username1.place(x=100, y=20, width=100, height=20)
password1 = tk.Entry(show="*")
password1.place(x=100, y=50, width=100, height=20)

listbox = Listbox(form)
listbox.place(x=260, y=50, width=220, height=360)

def verial():
    ud.userName = username1.get()
    ud.password = password1.get()
    Browser("https://www.instagram.com")

def temizle():
    list1.clear()
    list2.clear()
    listbox.delete(0, END)

buton = tk.Button(form, text="Giriş", command=verial, fg="white", bg="grey", font=("Arial", 10))
buton.place(x=120, y=80, width=60, height=30)

buton2 = tk.Button(form, text="Temizle", command=temizle, fg="white", bg="grey", font=("Arial", 10))
buton2.place(x=260, y=415, width=60, height=30)

label3 = tk.Label(text="Takip Ettiğin Fakat", font=("Helvetica", 10, BOLD), fg="white", bg="#4a494d")
label3.place(x=260, y=5, width=220)
label4 = tk.Label(text="Seni Takip Etmeyen Kullanıcılar", font=("Helvetica", 10, BOLD), fg="white", bg="#4a494d")
label4.place(x=260, y=25, width=220)

instagram_logo = PhotoImage(file="instagram.png")
instagram_label = tk.Label(image=instagram_logo, bg="#4a494d")
instagram_label.place(x=20, y=130)

igb_logo = PhotoImage(file="pngwing.com.png")
igb_label = tk.Label(image=igb_logo, bg="#4a494d")
igb_label.place(x=20, y=430)

label15 = tk.Label(text="onemanbattalion", font=("Helvetica", 13, BOLD), fg="black", bg="#4a494d")
label15.place(x=110, y=450)

label5 = tk.Label(text="- Program'a Kullanıcı Adı ve", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label5.place(x=90, y=135)

label6 = tk.Label(text="Şifre Girilir.", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label6.place(x=120, y=155)

label7 = tk.Label(text="- Ardından Giriş Tuşuna Basıldığında", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label7.place(x=20, y=190)

label8 = tk.Label(text="Chrome Tarayıcısı Açılır.", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label8.place(x=50, y=210)

label9 = tk.Label(text="- Uygun ChromeDriver Yüklü Olmalıdır.", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label9.place(x=20, y=250)

label10 = tk.Label(text="- Program Çalışırken Müdahale Etmeniz", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label10.place(x=20, y=290)

label11 = tk.Label(text="Durumunda Sorun Yaşanabilir.", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label11.place(x=50, y=310)

label12 = tk.Label(text="- Giriş Yapılırken veya Program", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label12.place(x=20, y=350)

label13 = tk.Label(text="Çalışırken Sorun Yaşarsanız", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label13.place(x=27, y=370)

label13 = tk.Label(text="Lütfen Kapatıp Tekrar Açınız.", font=("Helvetica", 9, BOLD), fg="#f0f2f7", bg="#4a494d")
label13.place(x=27, y=390)

list1 = []
list2 = []

class Browser:
    def __init__(self, link):
        options = webdriver.ChromeOptions()
        options.headless = False
        self.link = link
        chrome_service = ChromeService('chromedriver.exe')
        chrome_service.creationflags = CREATE_NO_WINDOW
        self.browser = webdriver.Chrome(service=chrome_service, options=options)

        self.goInstagram()

    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        self.login()
        self.getFollowers()

    def getFollowers(self):
        self.browser.get("https://www.instagram.com/" + ud.userName + "/followers/")
        time.sleep(4)

        self.scrollDown()

        takipciler = self.browser.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")
        for takipci in takipciler:
            list1.append(takipci.text)

        self.browser.get("https://www.instagram.com/" + ud.userName + "/following/")
        time.sleep(4)
        self.scrollDown()

        takipedilenler = self.browser.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")
        for takipedilen in takipedilenler:
            list2.append(takipedilen.text)

        for c in list2:
            if c not in list1:
                listbox.insert(END, c)

    def scrollDown(self):
        jsKomut = """
        sayfa = document.querySelector("._aano");
        if (sayfa) {
            sayfa.scrollTo(0, sayfa.scrollHeight);
            var sayfaSonu = sayfa.scrollHeight;
            return sayfaSonu;
        } else {
            return null;
        }
        """
        try:
            sayfaSonu = self.browser.execute_script(jsKomut)
            while True:
                son = sayfaSonu
                time.sleep(2)
                sayfaSonu = self.browser.execute_script(jsKomut)
                if son == sayfaSonu:
                    break
        except JavascriptException as e:
            print(f"JavaScript error: {e}")

    def login(self):
        try:
            username = self.browser.find_element(By.NAME, "username")
            password = self.browser.find_element(By.NAME, "password")
            username.send_keys(ud.userName)
            password.send_keys(ud.password)

            loginBtn = self.browser.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button > div")
            loginBtn.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print(f"Login error: {e}")

form.mainloop()
