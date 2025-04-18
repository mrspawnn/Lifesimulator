import random
import json
from time import sleep

def veri_kaydet(veri):
    with open("kullanici_veri.json", "w") as dosya:
        json.dump(veri, dosya)

def veri_oku():
    try:
        with open("kullanici_veri.json", "r") as dosya:
            return json.load(dosya)
    except:
        return {}

def yasam_simulatoru():
    print("Merhaba, ben Luna, senin yaşam koçunum!")
    sleep(1)
    veri = veri_oku()

    if not veri:
        print("Seni ilk kez görüyorum! Kendini tanıt.")
        veri["yas"] = int(input("Yaşın kaç? "))
        veri["meslek"] = input("Mesleğin nedir? ")
        veri_kaydet(veri)
    else:
        print(f"Hoş geldin! {veri['yas']} yaşında, {veri['meslek']} olarak seni hatırlıyorum.")

    while True:
        karar = input("Ne konuşalım? (ör: 'is degistir', 'cikis') ").lower().replace("ı", "i").replace("ş", "s")
        if karar == "cikis":
            print("Görüşürüz!")
            break
        elif "is degistir" in karar:
            basari = random.randint(50, 90) - (veri["yas"] // 10)
            print(f"Simülasyon: İş değiştirme başarı olasılığı: %{basari}")
            sleep(1)
            print("Başarılı!" if basari > 70 else "Zorlanabilirsin, ama devam!")
            veri["son_karar"] = "is degistir"
            veri_kaydet(veri)
        else:
            print("Bunu anlayamadım, başka bir şey dene! (ör: 'is degistir', 'cikis')")

yasam_simulatoru()
