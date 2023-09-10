import speech_recognition as sr
import datetime  # anlık zamanı öğrenmek için
import webbrowser
import smtplib
from gtts import gTTS  # text i ses e çevirmek için
from playsound import playsound  # ses dosyasını çalmak için
from random import choice  # random bir değer seçmek için
import os  # sistem ayarları değiştirmk için
import feedparser  # hava  durumunu çekmek için
import wikipedia
import ctypes
import subprocess
from ecapture import ecapture as ec
import random

def speak(string):  # speak adlı bir fonksiyon oluştuyouz
    tts = gTTS(string, lang='tr')  # sesi text e türkçe olarak çevirip tts adlı değişkene tanımlıyouz
    rand = random.randint(1,
                          100)  # random 1 ve 100 arası bir sayı üretip rand adlı değişkene tanımlıyouz bunun amacı bir hata ile karşılaşıp mp3 dosyası silinmezse üsütne yazmasın diye
    file = 'ses-' + str(rand) + '.mp3'  # .mp3 uzantılı bir ses dosyası oluşturuyoruz
    tts.save(file)  # dosyayı kayıt ediyouz
    playsound(file)  # dosyayı okutuyoyz
    os.remove(file)  # dosyayı siliyouz

def ilk_konusma():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("günaydın patron !")

    elif hour >= 12 and hour < 18:
        speak(" iyi gün ortaları efendim")

    else:
        speak("iyi akşamlar efendim")

    assname = ("benim ismim friday v2.0")
    speak("sizin yeni ve türkçe dil desteği kazanmış bir asistanınızım")
    speak(assname)
    speak(" size nasıl yardımcı olabilirim")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bir komut verin...")
        audio = r.listen(source)
    try:
        voice = r.recognize_google(audio, language="tr-TR")
        print("Söylediğiniz komut:", voice)
        return voice
    except sr.UnknownValueError:
        print("Komut anlaşılamadı.")
        speak("üzgünüm anlayamadım")
    except sr.RequestError as e:
        print("Ses tanıma servisi çalışmıyor; {0}".format(e))
        speak('Sistemin çalışmıyor')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # gmail bilgilerini gir
    server.login('korayabaci67@gmail.com', 'Biyodes16')
    server.sendmail('koray.knk.koray67@gmail.com', to, content)
    server.close()



if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    ilk_konusma()



    while True:
        voice = listen().lower()

        if 'teşekkür ederim' in voice:  # eğer voice nin içinde teşekkür ederim diye bir değer varsa bunları yap
                print("rica ederim başka bir sorunuz varmı")  # ekrana yazılacak veri
                speak("rica ederim başka bir sorunuz varmı")  # sesli bir şekilde söylenmesi için

        if 'iyiyim' in voice:  # eğer voice nin içinde iyiyim diye bir değer varsa bunları yap
                print("iyi olmanıza sevindim")  # ekrana yazılacak veri
                speak("iyi olmanıza sevindim")  # sesli bir şekilde söylenmesi için

        if 'kötüyüm ' in voice:  # eğer voice nin içinde kötüyüm diye bir değer varsa bunları yap
                # sozlerOlumsuz adlı bir dizi tanımlıyoruz
                sozlerOlumsuz = ["neyiniz var belki yardımcı olabilirim",
                                 "umarım en kısa zamanda iyi olursunuz",
                                 "Allah bazen kullarını imtihan eder bize sabretmek ve tevekkül etmek düşer lütfen sabredin"
                                 ]
                secimolumsuz = choice(sozlerOlumsuz)  # sozlerden birini karışık olarak seçilecek

                speak(secimolumsuz)  # seçilen söz seslendiriliecek
                print("friday  = " + secimolumsuz)  # seçilen söz ekrana yazılması için

        if 'fıkra anlat' in voice:  # eğer voice nin içinde Fıkra anlat diye bir değer varsa bunları yap
                # fıkralar adlı bir dizi tanımlıyoruz
                fikralar = ["bir kuş diğer kuşla dalga geçerken ne demiş kuş beyinli hahahaha ",
                            "bir espiri yapayım mı bomm haahaha ",
                            "bir tane biyoloji fıkrası biliyorum iki sağlık görevlisi yolda yürüyormuş biri diğerine dokunup aaaa enfekte oldum demiş diğeride o zaman seni hastaneye yatırmamız gerek demiş hahahahahah",
                            "fıkraya gerek yok kerem önder izle gülmezsen gel beni sil",

                            ]
                secimfik = choice(fikralar)  # sozlerden birini karışık olarak seçilecek

                speak(secimfik)  # seçilen söz seslendiriliecek
                print("friday  = " + secimfik)  # seçilen söz ekrana yazılması için


        if 'neler yapabilirsin' in voice:  # eğer voice nin içinde neler yapabilirsin diye bir değer varsa bunları yap
                speak(' geliştirilmeye devam eden bir sesli asistanım ama size çoğu konuda yardım edebilirim  ')
                print(' geliştirilmeye devam eden bir sesli asistanım ama size çoğu konuda yardım edebilirim')

        if 'sen kimsin' in voice:  # eğer voice nin içinde sen kimsin diye bir değer varsa bunları yap
                speak('Benim adım friday, beni tasarlayan ve geliştiren korayın çok emeği var üstümde çok severim kendisini')  # selendirelecek
                print(
                    ' Benim adım friday, beni tasarlayan ve geliştiren korayın çok emeği var üstümde çok severim kendisini')  # ekrana yazılacak

        if 'saat kaç' in voice:  # eğer voice nin içinde saat kaç diye bir değer varsa bunları yap
                speak(datetime.now().strftime(
                    '%H:%M:%S'))  # datetime.now sayesinde anlık saati alıyoruz ve seslendiriyouz
                print("friday  = " + datetime.now().strftime(
                    '%H:%M:%S'))  # datetime.now sayesinde anlık saati alıyoruz ve yazdırıyoruz

        if 'arama yap' in voice:  # eğer voice nin içinde arama yap diye bir değer varsa bunları yap
                search = listen(
                    'ne aramamı istersin')  # record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp search değişkenine tanımlıyouz
                url = 'https://google.com/search?q=' + search  # https://google.com/search?q= adresine aldığımız search ı ekliyoruz ve url değişkenine tanımlıyouz
                webbrowser.get().open(url)  # web browserı açıyouz ve  url değişkenini dönderiyouz
                speak(search + ' için bulduğum sonuçlar')  # sesli bir şekilde seslendirme yapıyouz
                print("friday  = " + search + ' için bulduğum sonuçlar')  # ekrana yazdırma yapıyouz

        if "youtube'da ara" in voice:  # eğer voice nin içinde arama yap diye bir değer varsa bunları yap
                searchy = listen('ne aramamı istersin')  # record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp searchy değişkenine tanımlıyouz
                urly = 'https://www.youtube.com/results?search_query=' + searchy  # https://google.com/search?q= adresine aldığımız searchy ı ekliyoruz ve urly değişkenine tanımlıyouz
                webbrowser.get().open(urly)  # web browserı açıyouz ve  urly değişkenini dönderiyouz
                speak(searchy + ' için bulduğum sonuçlar')  # sesli bir şekilde seslendirme yapıyouz
                print("friday = " + searchy + ' için bulduğum sonuçlar')  # ekrana yazdırma yapıyouz

        if 'hava durumu' in voice:  # eğer voice nin içinde hava durumu diye bir değer varsa bunları yap
                # feedparser ile link deki veriyi çekip parçalıyouz bunuda parse değişkenine tanımlıyouz
                parse = feedparser.parse(
                    "https://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR%7CTR%7C71100%7CBURSA")
                parse = parse["entries"][0]["summary"]
                parse = parse.split()
                havail = parse[2]  # havaiiladlı adlı değişkene parsenin 3.değeri olan il adını tanımlıyoruz
                havadetay = parse[4]  # havadetay adlı  değişkene parsenin 5. değeri olan dereceyi tanımlıyoruz
                havanem = parse[3]
                speak(havail + " için hava" + havadetay + " derece" + havanem + "nem")  # sesli söyletiouz
                print("friday  = " + havail + " için hava" + havadetay + " derece"+ havanem + "nem")  # ekrana yazdırıyouz

        if 'kendine iyi bak' in voice:  # eğer voice nin içinde güle güle diye bir değer varsa bunları yap
                speak('sizde kendinize iyi bakın ')  # sesli söyletiouz
                print('friday  = sizde  kendinize iyi bakın ')  # ekrana yazdırıyouz
                exit()  # uygulamadan çıkış yapıyouz

        if 'wikipediayı aç' in voice:
            speak(' wikipediya açılıyor...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Wikipedia ya göre...")
            print("friday = bulduğum sonuc")
            speak("bulduğum sonuç")

        if ' email at ' in voice:
            try:
                speak("ne yazayım")
                content = listen()
                to = "alıcı kim"
                sendEmail(to, content)
                speak("alıcıya gönderildi !")
            except Exception as e:
                print(e)
                speak("e maili gönderemedim tekrar deneyin")

        if 'pencereyi kapat' in voice:
            speak("bilgisayar ekranı kapanıyor")
            ctypes.windll.user32.LockWorkStation()

        elif 'bilgisayarı kapat' in voice:
            speak("1 saniye bilgisayarınız kapatılıyor.")
            subprocess.call('kapat / p /f')

        if "ben neredeyim" in voice:
            query = query.replace("buradasınız:", "")
            location = query
            speak("suan buradasınız")
            speak(location)
            webbrowser.open("https://www.google.com.tr/maps/@41.1034552,29.0255963,17z?hl=tr" + location + "")


        elif "fotoğraf çek" in voice:
            ec.capture(0, "Friday Camera ", "img.jpg")

        elif "video çek" in voice:
            ec.capture(0, "Friday Camera ", "img.mp4")

        elif "yeniden başlat " in voice:
            subprocess.call(["yeniden başlatılıyor", "/r"])

        elif "uyku modu " in voice:
            speak("uyku  moduna geçiliyor")
            subprocess.call("uyku / h")


        elif "not tut" in voice:
            speak("ne yazayım ")
            note = listen()
            file = open('friday.txt', 'w')
            speak("yazıya tarih de eklemek istermisiniz ")
            snfm = listen()
            if 'evet' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "notu göster" in voice:
            speak("notu gösteriyorum")
            file = open("friday.txt", "r")
            print(file.read())
            speak(file.read(6))
