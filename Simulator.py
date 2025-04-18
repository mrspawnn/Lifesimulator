import random
import json
from time import sleep

# Kullanıcı verilerini saklama ve okuma
def veri_kaydet(veri):
    with open("kullanici_veri.json", "w") as dosya:
        json.dump(veri, dosya)

def veri_oku():
    try:
        with open("kullanici_veri.json", "r") as dosya:
            return json.load(dosya)
    except:
        return {}

# Simülasyon fonksiyonları
def is_degistir_simulasyon(veri):
    basari = random.randint(40, 90) - (veri["yas"] // 10)
    if veri["finansal_durum"] < 30:
        basari -= 10
    if veri["egitim_seviyesi"] == "yuksek":
        basari += 10
    print(f"Simülasyon: İş değiştirme başarı olasılığı: %{basari}")
    sleep(1)
    print("Başarılı!" if basari > 70 else "Zorlanabilirsin, ama devam!")
    return {"karar": "is degistir", "basari": basari}

def evlen_simulasyon(veri):
    basari = random.randint(50, 90)
    if veri["yas"] > 35:
        basari -= 10
    if veri["finansal_durum"] > 70:
        basari += 10
    print(f"Simülasyon: Evlilik kararı başarı olasılığı: %{basari}")
    sleep(1)
    print("Mutlu bir evlilik!" if basari > 70 else "Bazı zorluklar olabilir!")
    return {"karar": "evlen", "basari": basari}

def sehir_degistir_simulasyon(veri):
    basari = random.randint(40, 90)
    if veri["sehir"] == "kucuk":
        basari += 10
    if veri["finansal_durum"] < 50:
        basari -= 15
    print(f"Simülasyon: Şehir değiştirme başarı olasılığı: %{basari}")
    sleep(1)
    print("Yeni şehirde harika bir başlangıç!" if basari > 70 else "Adapte olmakta zorlanabilirsin!")
    return {"karar": "sehir degistir", "basari": basari}

def egitim_al_simulasyon(veri):
    basari = random.randint(50, 90)
    if veri["yas"] > 40:
        basari -= 10
    if veri["egitim_seviyesi"] == "dusuk":
        basari += 10
    print(f"Simülasyon: Yeni eğitim alma başarı olasılığı: %{basari}")
    sleep(1)
    print("Eğitimi başarıyla tamamladın!" if basari > 70 else "Eğitimde bazı zorluklar yaşadın!")
    return {"karar": "egitim al", "basari": basari}

# Geçmiş kararları gösterme
def gecmis_kararlari_goster(veri):
    if "gecmis_kararlar" not in veri or not veri["gecmis_kararlar"]:
        print("Henüz bir karar vermedin!")
    else:
        print("Geçmiş kararların:")
        for karar in veri["gecmis_kararlar"]:
            print(f"- {karar['karar']}: Başarı olasılığı %{karar['basari']}")

# Ana simülatör
def yasam_simulatoru():
    print("Merhaba, ben Luna, senin yaşam koçunum!")
    sleep(1)
    veri = veri_oku()

    # Eksik anahtarları kontrol et ve varsayılan değerler ekle
    if not veri or "yas" not in veri:
        veri = {"gecmis_kararlar": []}
        print("Seni ilk kez görüyorum! Kendini tanıt.")
        while True:
            try:
                veri["yas"] = int(input("Yaşın kaç? "))
                if veri["yas"] < 0 or veri["yas"] > 120:
                    print("Lütfen geçerli bir yaş gir (0-120 arası)!")
                    continue
                break
            except ValueError:
                print("Lütfen sayısal bir değer gir!")
        veri["meslek"] = input("Mesleğin nedir? ")
        veri["medeni_durum"] = input("Medeni durumun nedir? (bekar/evli) ").lower()
        veri["sehir"] = input("Hangi şehirde yaşıyorsun? (buyuk/kucuk) ").lower()
        veri["egitim_seviyesi"] = input("Eğitim seviyen nedir? (dusuk/orta/yuksek) ").lower()
        while True:
            try:
                veri["finansal_durum"] = int(input("Finansal durumun (0-100 arası bir sayı)? "))
                if veri["finansal_durum"] < 0 or veri["finansal_durum"] > 100:
                    print("Lütfen 0-100 arası bir sayı gir!")
                    continue
                break
            except ValueError:
                print("Lütfen sayısal bir değer gir!")
        veri_kaydet(veri)
    else:
        # Eksik anahtarları kontrol et ve varsayılan değerler ekle
        if "medeni_durum" not in veri:
            veri["medeni_durum"] = "bekar"
        if "sehir" not in veri:
            veri["sehir"] = "buyuk"
        if "egitim_seviyesi" not in veri:
            veri["egitim_seviyesi"] = "orta"
        if "finansal_durum" not in veri:
            veri["finansal_durum"] = 50
        if "gecmis_kararlar" not in veri:
            veri["gecmis_kararlar"] = []
        veri_kaydet(veri)  # Güncellenmiş veriyi kaydet
        print(f"Hoş geldin! {veri['yas']} yaşında, {veri['meslek']} olarak seni hatırlıyorum.")
        print(f"Medeni durum: {veri['medeni_durum']}, Şehir: {veri['sehir']}, Eğitim: {veri['egitim_seviyesi']}, Finansal durum: {veri['finansal_durum']}")

    # Ana döngü
    while True:
        karar = input("Ne konuşalım? (ör: 'is degistir', 'evlen', 'sehir degistir', 'egitim al', 'gecmis', 'cikis') ").lower().replace("ı", "i").replace("ş", "s")
        if karar == "cikis":
            print("Görüşürüz!")
            break
        elif "is degistir" in karar:
            sonuc = is_degistir_simulasyon(veri)
            veri["gecmis_kararlar"].append(sonuc)
            veri_kaydet(veri)
        elif "evlen" in karar:
            sonuc = evlen_simulasyon(veri)
            veri["gecmis_kararlar"].append(sonuc)
            veri_kaydet(veri)
        elif "sehir degistir" in karar:
            sonuc = sehir_degistir_simulasyon(veri)
            veri["gecmis_kararlar"].append(sonuc)
            veri_kaydet(veri)
        elif "egitim al" in karar:
            sonuc = egitim_al_simulasyon(veri)
            veri["gecmis_kararlar"].append(sonuc)
            veri_kaydet(veri)
        elif "gecmis" in karar:
            gecmis_kararlari_goster(veri)
        else:
            print("Bunu anlayamadım, başka bir şey dene! (ör: 'is degistir', 'evlen', 'sehir degistir', 'egitim al', 'gecmis', 'cikis')")

yasam_simulatoru()
