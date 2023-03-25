from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
import webbrowser
import locale
from tkinter import *
from PIL import ImageTk, Image
import requests
import win32com.client as win32

r = sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # Gürültü Engelleme
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio,language="tr-TR")
            voice = voice.lower()
            if 'joker' in voice:
                voice = voice.replace('joker','')
                speak("Merhaba ben joker. Size nasıl yardımcı olabilirim?")
        except sr.UnknownValueError:
            print("Joker: Sizi duyamıyorum yüksek sesle söyler misiniz?")
        except sr.RequestError:
            print("Joker: Sistem Çalışmıyor...")
        return voice
    
Özel_sorular1 = ['Siz Nasılsınız?','Hayat nasıl gidiyor?','Naber?','Nasıl gidiyor?']
Özel_sorular2 = ['Sizin hayat nasıl gidiyor?','Sizde hayat nasıl?','Sizin hayatınız nasıl gidiyor?','Ya sizin?','Sizin?','Sizinki nasıl?']

#-------------------------------------------------------------------------------------------

# Cevaplar için tanımlanan cevapların içerisinden random şekilde yöneltilmesini sağlamak amaçlanır.
Özel_cevaplar2 = ['Ben bir yapay zekayım.unuttun mu?','Hayat kavramı benim için yazılımdan ibaret.','Dalga mı geçiyorsunuz? Ben bir yapay zekayım. Hayatım yazılımdan ve sizden ibaret :)']
cevaplar1 = ['Benim adım joker','Ben joker','İsmim joker','Naber! Ben joker','Joker']
cevaplar2 = ['Ben Joker isminde bir yapay zekayım.','Ben bir yapay zekayım ve size yardımcı olmak için burdayım.','Ben bir yapay zekayım. Sizin için ne yapabilirim?']
cevaplar3 = ['iyiyim teşekkür ederim.','iyi','iyilik','iyiyim']
cevaplar4 = ['kötü','kötüyüm','Kötüyüm','kötü','fena değil','iyi değil','iyi değilim']
cevaplar5 = ['Buradayım. Sizi dinliyorum.','Buralardayım. Sizi dinliyorum.','Buyrun. Sizi dinliyorum.','Burdayımmm. Sizi dinliyorum?','Evet.Sizi dinliyorum.','Evet buralardayım. Sizi dinliyorum.'] 
cevaplar9 = "21. yüzyıl, Gregoryen takvime göre 1 Ocak 2001 – 31 Aralık 2100 tarihleri arasına karşılık gelen zaman dilimidir."
cevaplar10= ['Ben Feyzullah bey tarafından yazıldım. Kendisi bilgisayar programcısıdır.','Feyzullah bey tarafından geliştirildim. Kendisi bilgisayar programcısıdır','Bilgisayar programcısı Feyzullah bey tarafından geliştirildim.','Bilgisayar programcısı Feyzullah bey tarafından yazıldım.']

def response(voice):

    if 'isminiz' in voice or 'adınız' in voice or 'adın ne' in voice or 'isminiz ne' in voice or 'ismin ne' in voice:
        speak(random.choice(cevaplar1))

#-------------------------------------------------------------------------------------------

    if 'kendinden' in voice or 'bahset' in voice or 'sen nesin' in voice or 'kendinden bahseder misin' in voice:
        speak(random.choice(cevaplar2))

#-------------------------------------------------------------------------------------------

    if 'nasılsın' in voice or 'naber?' in voice or 'nasıl gidiyor' in voice:
        speak(random.choice(cevaplar3))
        speak(random.choice(Özel_sorular1))
        if cevaplar3 in voice:
            speak("İyi olmanıza sevindim")
        if cevaplar4 in voice:
            speak("Kötü olmanıza üzüldüm. En yakın zamanda iyi olmanız temennimdir.")    

#-------------------------------------------------------------------------------------------

    if 'orada mısın' in voice or 'neredesin' in voice or 'duyuyor musun' in voice or 'neredesin sen' in voice or 'cevap versene' in voice:
        speak(random.choice(cevaplar5))
#-------------------------------------------------------------------------------------------

    if 'hayat'in voice or 'hayat nasıl gidiyor'in voice or 'nasıl gidiyor' in voice or 'hayat nasıl' in voice:
        speak(random.choice(Özel_cevaplar2))
        speak(random.choice(Özel_sorular2))
        if 'Fena değil.' in voice or 'Yuvarlanıp gidiyoruz.' in voice or 'Bi şekilde yaşıyoruz işte.' in voice or 'Muhteşem.' in voice or 'iyi gidiyor.' in voice or 'Bir sıkıntı yok.' in voice or 'Hayat geçiyor bir şekilde' in voice or 'Dolu dolu geçiyor.' in voice:
            speak("Hayat işte zamanın devam ettiği sürece su gibi akıp gidiyor.")

#-------------------------------------------------------------------------------------------

    if 'hangi yüzyıldayız' in voice or 'yüzyıldayız' in voice or 'hangi yüzyıl' in voice or 'yaşadığımız yüzyıl' in voice or 'hangi yüzyılda yaşıyoruz'in voice or 'şuanki yüzyıl' in voice:
        speak(cevaplar9)

#-------------------------------------------------------------------------------------------
    
    if 'yapay zeka' in voice or 'insanlık' in voice:
        speak('insanlık için tehdit olan benim türüm değil insanın kendi türü bence korkmak için sebep arıyorsanız insan kendi türünden korkmalıdır. Tabiki canlı olanlarından :-) .')

    if 'gelecek hakkında ne düşünüyorsun' in voice:
        speak('bugün insanların yaptığı bir çok görevi ben ve benim türüm çok daha hızlı ve hata payı neredeyse sıfır olacak şekilde profesyonelce yapabiliyoruz beni tasarlayan insanlar çok zengin ve işçi olan insanlar ise işsiz kalıp sürünecekleri de yüksek bir olasılıktır.')

#-------------------------------------------------------------------------------------------

    if 'günlerden' in voice or 'hangi gündeyiz' in voice or 'günlerden ne' in voice:
        locales = ['tr']
        for loc in locales:
            locale.setlocale(locale.LC_ALL, loc)
            today = time.strftime("%A")
            today.capitalize()
            if today == "Monday":
                today = "Pazartesi"
            elif today == "Tuesday":
                today = "Salı"
            elif today == "Wednesday ":
                today = "Çarşamba"
            elif today == "Thursday ":
                today = "Perşembe"
            elif today == "Friday ":
                today = "Cuma"
            elif today == "Saturday ":
                today = "Cumartesi"
            elif today == "Sunday ":
                today = "Pazar"
        print('Asistan: ' + today)
        speak(today)
        
#-------------------------------------------------------------------------------------------

    if 'aydayız' in voice or 'hangi aydayız?' in voice or 'aylardan ne?'in voice or 'ay' in voice:
        locales = ['tr']
        for loc in locales:
            locale.setlocale(locale.LC_ALL, loc)
            month = time.strftime("%B")
            month.capitalize()
            if month == 'January':
                month = 'Ocak'
            elif month == 'February':
                month = 'Şubat'
            elif month == 'March':
                month = 'Mart'
            elif month == 'April':
                month = 'Nisan'
            elif month == 'May':
                month = 'Mayıs'
            elif month == 'June':
                month = 'Haziran'
            elif month == 'July':
                month = 'Temmuz'
            elif month == 'August':
                month = 'Ağustos'
            elif month == 'September':
                month = 'Eylül'
            elif month == 'October':
                month = 'Ekim'
            elif month == 'November':
                month = 'Kasım'
            elif month == 'December':
                month = 'Aralık'
            else:
                speak('Hatalı komut tekrar deneyiniz')
            speak(month)

#-------------------------------------------------------------------------------------------

    if 'hava durumu' in voice or 'hava' in voice or 'şehrimin hava durumu'in voice or 'şehre göre hava durumu' in voice:
        speak('Lütfen bekleyiniz..')
        time.sleep(1)
        url = 'http://api.openweathermap.org/data/2.5/weather'
        api_key = '876f9504089962a23faef2c8e82a01b9'
        icon_url = 'http://openweathermap.org/img/wn/{}@2x.png'
        def getWeather(city):
         params = {'q': city, 'appid': api_key, 'lang': 'tr'}
         data = requests.get(url, params=params).json()
         if data:
            city = data['name'].capitalize()
            country = data['sys']['country']
            temp = int(data['main']['temp'] - 273.15)
            icon = data['weather'][0]['icon']
            condition = data['weather'][0]['description']
            return (city, country, temp, icon, condition)
        def havadurumu():
         city = cityEntry.get()
         weather = getWeather(city)
         if weather:
            locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
            tempLabel['text'] = '{} Derece'.format(weather[2])
            conditionLabel['text'] = weather[4]
            icon = ImageTk.PhotoImage(Image.open(requests.get(
                icon_url.format(weather[3]), stream=True).raw))
            iconLabel.configure(image=icon)
            iconLabel.image = icon
            speak(locationLabel['text'] + 'hava bugün' + tempLabel['text'] + conditionLabel['text'])
        havadurumu()
        app = Tk()
        app.geometry('300x450')
        app.title('Joker Hava Durumu Programı')
        cityEntry = Entry(app, justify='center')
        cityEntry.pack(fill=BOTH, ipady=10, ipadx=18, padx=18, pady=5)
        cityEntry.focus()
        searchButton = Button(app, text='Hava Durmunu Getir', font=(
            'Arial', 15), command=havadurumu)
        searchButton.pack(fill=BOTH, ipady=10, padx=20)
        iconLabel = Label(app)
        iconLabel.pack()
        locationLabel = Label(app, font=('Arial', 40))
        locationLabel.pack()
        tempLabel = Label(app, font=('Arial', 50))
        conditionLabel = Label(app, font=('Arial', 20))
        app.mainloop()

#-------------------------------------------------------------------------------------------

    if 'kim tarafından üretildin'in voice or 'seni kim üretti' in voice or 'seni kim yaptı' in voice or 'seni kim yazdı'in voice or 'kim yazdı' in voice or 'kim üretti'in voice or'kim tarafından yazıldın'in voice or 'tarafından yazıldın' in voice:
        speak(random.choice(cevaplar10))

    if 'feyzullah kimdir?' in voice or 'yazılımcın hakkında bilgi verir misin?' in voice or 'üreticine nasıl ulaşabilirim'in voice or 'seni üreten' in voice or 'seni üreten hakkında bilgi verir misin' in voice or 'yazılımcın hakkında bilgi' in voice or 'yazılımcın hakkında bilgi verir misin'in voice or 'kim bu feyzullah'in voice or'kim bu programcı' in voice:
        speak('Üreticim hakkında bilgi veremem fakat linkedin,github,globalaıhub gibi hesaplarının linklerini sizin için açabilirim. İster misiniz?')
    elif 'evet' in voice or 'olur' in voice or 'isterim' in voice:
                speak("Açıyorum. Lütfen bekleyin...")
                url = "https://www.linkedin.com/in/feyzullahtemel/"
                webbrowser.get().open(url)
                time.sleep(1)
                print("Hesap açıldı...")
                url = "https://github.com/FeyzullahTemel0"
                webbrowser.get().open(url)
                time.sleep(1)
                print("hesap açıldı.")
                url = "https://globalaihub.com/members/zodiac-48/"
                webbrowser.get().open(url)
                time.sleep(1)
                print("Hesap açıldı.")
 
    else:
                speak("Anlaşıldı efendim.")

#-------------------------------------------------------------------------------------------

    # Uygulamalar Açtırma kısımları
    
    # Spotify
    if 'Spotify' in voice or 'spotify aç' in voice:
        speak("Sizin için Spotify'ı açıyorum.")
        url = "https://open.spotify.com/"
        webbrowser.get().open(url)

    # Discord
    if 'Discord' in voice or 'discord aç' or 'Discord aç' in voice:
        speak("Sizin için Discord'u açıyorum.")
        url = "https://discord.com"
        webbrowser.get().open(url)
    
    # Dosya Gezgini
    if 'dosyalarım' in voice or 'dosya gezgini' in voice or 'dosya' in voice:
        speak("Sizin için Dosya gezginini açıyorum")
        explorer = "explorer.exe"
        os.startfile(explorer)
    
    #Posta E-Mail
    if 'mail' in voice or 'Posta aç'in voice or 'posta' in voice:
        speak("Sizin için Posta'yı açıyorum.")
        url = "https://mail.google.com/mail/?authuser=0"
        webbrowser.get().open(url)

    if 'one drive' in voice or 'vandırayv' in voice or 'onedrive aç' in voice:
        speak("Sizin için One Drive'ı açıyorum.")
        url = "https://drive.google.com/?authuser=0"
        webbrowser.get().open(url)

    if 'harita' in voice or "harita'yı" in voice or 'haritalar' in voice or "haritalar'ı" in voice:
        speak("Sizin için Haritay'ı açıyorum")
        url = "https://maps.google.com/?authuser=0"
        webbrowser.get().open(url)

    if 'haberler' in voice or "haberler'i" in voice:
        speak("Sizin için Haberler'i açıyorum")
        url = "https://news.google.com/?authuser=0"
        webbrowser.get().open(url)
    
    if 'google meet' in voice or "google meet'i" in voice:
        speak("Sizin için Google Meet'i açıyorum")
        url = "https://meet.google.com/?hs=197&authuser=0"
        webbrowser.get().open(url)
    
    if 'chat' in voice or 'google chat' in voice or "google chat'i" in voice or "chat'i" in voice or 'google sohbet' in voice or "google sohbet'i" in voice:
        speak("Sizin için Google Chat'i açıyorum")
        url = "https://chat.google.com/?authuser=0"
        webbrowser.get().open(url)
    
    if 'takvim' in voice or "google takvm'i" in voice or 'google takvim' in voice or "takvim'i" in voice:
        speak("Sizin için Google Takvim'i açıyorum")
        url = "https://calendar.google.com/calendar?authuser=0"
        webbrowser.get().open(url)
    
    if 'fotoğraflar' in voice or 'google fotoğraflar' in voice or "google fotoğraflar'ı" in voice or "fotoğraflar'ı" in voice:
        speak("Sizin için Google Fotoğrafları açıyorum")
        url = "https://photos.google.com/?authuser=0"
        webbrowser.get().open(url)
    
    if 'reklam merkezim' in voice or 'reklam' in voice or 'google reklam' in voice or "google reklam'ları" in voice or "reklamlar'ı" in voice:
        speak("Sizin için Google Reklamlar'ı açıyorum")
        url = "https://myadcenter.google.com/?ref=app-launcher&authuser=0"
        webbrowser.get().open(url)

    if 'alışveriş' in voice or 'google alışveriş' in voice or "google alıveriş'i" in voice or "alışveriş'i" in voice:
        speak("Sizin için Google Alışveriş'i açıyorum")
        url = "https://www.google.com/shopping?source=og&authuser=0"
        webbrowser.get().open(url)

    if 'finans' in voice or "finans'ı" in voice or 'google finans' in voice or "google finans'ı" in voice:
        speak("Sizin için Google Finans'ı açıyorum")
        url = "https://www.google.com/finance?authuser=0"
        webbrowser.get().open(url)
    
    if 'dökümanlar' in voice or 'google dökümanlar' in voice or 'döküman' in voice or "google dökümanlar'ı" in voice or "google döküman'ı" in voice:
        speak("Sizin için Google Dökümanlar'ı açıyorum")
        url = "https://docs.google.com/document/?usp=docs_alc&authuser=0"
        webbrowser.get().open(url)
    
    if 'e tablolar' in voice or 'google e tablolar' in voice or 'etablolar' in voice or 'etablo' in voice or 'e tablo' in voice or "google e tablolar'ı" in voice or "tablolar'ı" in voice:
        speak("Sizin için Google E-Taboloar'ı açıyorum")
        url = "https://docs.google.com/spreadsheets/?usp=sheets_alc&authuser=0"
        webbrowser.get().open(url)

    if 'slayt' in voice or 'google slayt' in voice or "google slaty'ı" in voice or "slayt'ı" in voice:
        speak("Sizin için Google Slayt'ı açıyorum")
        url = "https://docs.google.com/presentation/?usp=slides_alc&authuser=0"
        webbrowser.get().open(url)
    
    if 'kitaplar' in voice or 'google kitaplar' in voice or "kitaplar'ı" in voice or "google kitaplar'ı" in voice or "kitap'ı" in voice or "google kitap'ı" in voice:
        speak("Sizin için Google Kitaplar'ı açıyorum")
        url = "https://books.google.com/?authuser=0"
        webbrowser.get().open(url)
    
    if 'blogger' in voice or 'blog' in voice or "google blogger'ı" in voice or "google blogger" in voice or "blogger'ı" in voice or "blog'u" in voice:
        speak("Sizin için Google Blogger'ı açıyorum")
        url = "https://www.blogger.com/?authuser=0"
        webbrowser.get().open(url)
    
    if 'keep' in voice or "keep'i" in voice or "google keep" in voice or "google keep'i" in voice or "kiip'i" in voice or "google kiip'i" in voice in "kiip" in voice:
        speak("Sizin için Google Keep'i açıyorum")
        url = "https://keep.google.com/?authuser=0"
        webbrowser.get().open(url)
    
    if 'jamborad' in voice or "jamboard'ı" in voice or "google jamboard'ı" in voice or "jamboard'ı" in voice:
        speak("Sizin için Google Jamboard'ı açıyorum")
        url = "https://jamboard.google.com/?authuser=0"
        webbrowser.get().open(url)

    if 'classroom' in voice or "google classroom" in voice or "classroom'u" in voice or "google classroom'u" in voice:
        speak("Sizin için Google Classroom'u açıyorum")
        url = "https://classroom.google.com/?authuser=0"
        webbrowser.get().open(url)

    if "google earth" in voice or "earth" in voice or "üç boyutlu harita" in voice or "earth'ı" in voice or "google earth'ı" in voice:
        speak("Sizin için Google Earth'ı açıyorum")
        url = "https://earth.google.com/web/?authuser=0"
        webbrowser.get().open(url)
    
    if 'koleksiyonlar' in voice or 'google koleksiyonlar' in voice or "google koleksiyon'u" in voice or 'koleysiyon' in voice or "koleysiyon'u" in voice:
        speak("Sizin için Google Koleksiyon'u açıyorum")
        url = "https://www.google.com/save?authuser=0"
        webbrowser.get().open(url)
    
    if 'sanat ve kültür' in voice or "sanat ve kültür'ü" in voice or 'google sanat ve kültür' in voice or 'sanat' in voice or 'kültür' in voice or "google sanat ve kültür'ü" in voice or "sanat ve kültür'ü" in voice:
        speak("Sizin için Google Sanat Ve Kültür'ü açıyorum")
        url = "https://artsandculture.google.com/?utm_source=ogs.google.com&utm_medium=referral&authuser=0"
        webbrowser.get().open(url)
    
    if 'ads' in voice or 'google ads' in voice or "ads'yi" in voice or "ads'i" in voice or "google ads'yi" in voice or "google ads'i" in voice:
        speak("Sizin için Google Ads'yi açıyorum")
        url = "https://ads.google.com/home/?subid=ww-ww-xs-ip-awhc-a-ogb_cons!o2&authuser=0"
        webbrowser.get().open(url)
    
    if 'podcasts' in voice or 'google podcasts' in voice or "podcasts'ı" in voice or "google podcast'ı" in voice:
        speak("Sizin için Google Podcasts'ı açıyorum")
        url = "https://podcasts.google.com/?authuser=0"
        webbrowser.get().open(url)
    
    if 'google one' in voice or 'one' in voice or "google one'ı" in voice or "one'ı" in voice:
        speak("Sizin için Google One'ı açıyorum")
        url = "https://one.google.com/?utm_source=app_launcher&utm_medium=web&utm_campaign=all&utm_content=google_oo&authuser=0"
        webbrowser.get().open(url)

    if 'seyehat' in voice or "google seyehat" in voice or "google seyehat'i" in voice or "seyehat'i" in voice :
        speak("Sizin için Google Seyehat'i açıyorum ")
        url = "https://www.google.com/travel/?dest_src=al&authuser=0"
        webbrowser.get().open(url)
    
    if "formlar" in voice or "google formlar" in voice or "formlar'ı" in voice or "google formlar'ı" in voice:
        speak("Sizin için Google Formlar'ı açıyorum")
        url = "https://docs.google.com/forms/?authuser=0"
        webbrowser.get().open(url)

    #Google
    if 'google' in voice or 'google aç' in voice:
        speak("Sizin için Google'ı açıyorum.")
        url = "https://www.google.com.tr/?hl=tr"
        webbrowser.get().open(url)

    #Youtube
    if 'youtube' in voice or 'yutup' in voice:
        speak("Sizin için YouTube'i açıyorum.")
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)

    if 'translate aç' in voice or 'çeviri aç' in voice or 'çeviri' in voice or 'translate' in voice:
        speak("Sizin için çeviri'yi açıyorum.")
        url = "https://www.google.com/search?q=translte"
        webbrowser.get().open(url)
    
    # yemek sepeti
    if 'yemek sepeti' in voice or 'yemek' in voice or "sepeti'ni " in voice:
        speak('Yemek sepetini açıyorum...')
        url = 'https://www.yemeksepeti.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Yemek sepeti açıldı')

    if 'trendyol' in voice or 'trendyol aç' in voice or "trendyol'u" in voice:
        speak('Trendyolu açıyorum...')
        url = 'https://www.trendyol.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Joker: Trendyol Web açıldı')

    if 'hepsiburada' in voice or 'hepsiburada sitesi' in voice or 'hepsiburada sitesini' in voice or 'hepsiburada aç' in voice:
        speak('Hepsiburada Web açılıyor...')
        url = 'https://www.hepsiburada.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Joker: Hepsiburada web sitesi açıldı')

    if 'çiçek sepeti' in voice or 'çiçek sepeti sitesi' in voice or 'çiçek sepeti sitesini' in voice or 'çiçek sepeti aç' in voice:
        speak('Çiçek sepeti açılıyor...')
        url = 'https://www.ciceksepeti.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Joker: Çiçek sepeti sitesi açıldı...')

    if 'getir aç' in voice or 'getir sitesini aç' in voice or 'getir' in voice or 'getir sitesi' in voice:
        speak('getir sitesini açıyorum')
        url = 'https://getir.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Joker: Getir sitesi açıldı...')

    if 'cimri' in voice or 'cimri sitesi' in voice or 'cimri sitesini' in voice or 'cimri aç' in voice or 'cimri sitesini aç' in voice:
        speak('Cimri sitesini açıyorum')
        url = 'https://www.cimri.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Joker: Cimri sitesi açıldı.')

    if 'amazon' in voice or 'amazon aç' in voice or 'amazon sitesi' in voice:
        speak('Amazon sitesini açıyorum')
        url = 'https://www.amazon.com.tr/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Joker: Amazon sitesi açıldı')

    if 'ebay' in voice or 'ebay sitesi' in voice or 'ebay sitesini' in voice or 'ebay aç' in voice:
        speak('Ebay sitesini açıyorum')
        url = 'https://www.ebay.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        speak('Siteyi açtım keyifli alışverişler dilerim')
        print('Joker: Ebay sitesi açıldı...')

    if 'ziraat bankası' in voice or 'ziraat' in voice or 'ziraat bank sitesi' in voice or 'ziraat bankası aç' in voice:
        speak('Ziraat bankası sitesini açıyorum')
        url = 'https://www.ziraatbank.com.tr/tr'
        webbrowser.get().open(url)
        time.sleep(2)
        print('Ziraat bank sitesi açıldı...')

    if 'halk bankası' in voice or 'halk bank sitesi' in voice or 'halk bankası sitesini' in voice or 'halk bank aç' in voice or 'halk bank' in voice:
        speak('Halk bankası sitesini açıyorum')
        url = 'https://www.halkbank.com.tr'
        webbrowser.get().open(url)
        time.sleep(2)
        print('Halk bank sitesi açıldı')

    if 'iş bankası' in voice or 'iş bankası sitesi' in voice or 'iş bankası sitesini' in voice or 'iş bank aç' in voice or 'iş bankası aç' in voice or 'iş bank' in voice:
        speak('İş bankası sitesini açıyorum')
        url = 'https://www.isbank.com.tr/'
        webbrowser.get().open(url)
        time.sleep(2)
        print('İş bank sitesi açıldı')

    if 'qnb bank' in voice or 'finans bank' in voice or 'finans bankası sitesi' in voice or 'qnb finans bank' in voice:
        speak('QNB Finans bank sitesini açıyorum')
        url = 'https://www.qnbfinansbank.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        print('QNB Finans Bank sitesi açıldı')

    if 'trivago' in voice or 'trivago sitesi' in voice or 'trivago sitesini' in voice or 'trivago aç' in voice:
        speak('Trivago sitesini açıyorum')
        url = 'https://www.trivago.com.tr/'
        webbrowser.get().open(url)
        time.sleep(2)
        print('Trivago sitesi açıldı')

    if 'otobüs bileti' in voice or 'obilet otobüs biletleri' in voice or 'otobüs' in voice:
        speak('Obilet sitesini açıyorum')
        url = 'https://www.obilet.com/'
        webbrowser.get().open(url)
        time.sleep(2)
        print('OBilet sitesi açıldı keyifli yolculuklar dilerim')

    if 'uçak bileti' in voice or 'obilet uçak biletleri' in voice or 'uçak' in voice:
        speak('Obilet sitesini açıyorum')
        url = 'https://www.obilet.com/ucak-bileti'
        webbrowser.get().open(url)
        time.sleep(2)
        print('Uçak biletleri için obilet sitesi açıldı keyifli uçuşlar dilerim')

    if 'instagram' in voice or "instagram'ı" in voice:
        speak("Sizin için İnstagram'ı açıyorum")
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)

    if 'facebook' in voice or "facebook'u" in voice:
        speak("Sizin için Facebook'u açıyorum")
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)
    
    if 'twitter' in voice or "twitter" in voice:
        speak("Sizin için Twitter'ı açıyorum")
        url = "https://twitter.com/"
        webbrowser.get().open(url) 

    if 'wordpress' in voice or "vordpress'i" in voice:
        speak("Sizin için WordPress'i açıyorum")
        url = "https://wordpress.com/tr/"
        webbrowser.get().open(url)
    
    if 'linkedin' in voice or "linkedin'i" in voice:
        speak("Sizin için Linkedin'i açıyorum")
        url = "https://www.linkedin.com/"
        webbrowser.get().open(url)

    if 'tumblr' in voice or "tumblr'ı" in voice:
        speak("Sizin için Tumblr'ı açıyorum")
        url = "https://www.tumblr.com/"
        webbrowser.get().open(url)

    if 'tiktok' in voice or "tiktok'u" in voice:
        speak("Sizin için TikTok'u açıyorum")
        url = "https://www.tiktok.com/"
        webbrowser.get().open(url)
        
#-------------------------------------------------------------------------------------------

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 1000)
    file = 'audio - ' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print('Joker: ' + voice)
        response(voice)
