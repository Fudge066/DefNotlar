def topla(a,b):
    return a+b
sonuc= topla(3,5)
print(sonuc)
"""#burda topla adlı bir fonksiyon tanımladık.
içine yazılan a ve b sayısını topluyor.
sonuc diye bir değişken ekleyip topla fonksiyonu ve 2 adet sayı girdik,
topla fonksiyonu otomatik olarak sayıları topladı.
""" 
# Not eklemek için bir fonksiyon
def not_ekle(notlar, yeni_not):
    notlar.append(yeni_not)
    return notlar

# Not ortalamasını hesaplamak için bir fonksiyon
def not_ortalamasi(notlar):
    if len(notlar) == 0:
        return 0
    return sum(notlar) / len(notlar)

# Harf notunu belirlemek için bir fonksiyon
def harf_notu(ortalama):
    if ortalama >= 90:
        return 'A'
    elif ortalama >= 80:
        return 'B'
    elif ortalama >= 70:
        return 'C'
    elif ortalama >= 60:
        return 'D'
    else:
        return 'F'

# Ana program
"""
def main():
    notlar = []
    while True:
        print("\n1. Not ekle")
        print("2. Not ortalamasını hesapla")
        print("3. Harf notunu belirle")
        print("4. Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == '1':
            yeni_not = float(input("Notu girin: "))
            notlar = not_ekle(notlar, yeni_not)
        elif secim == '2':
            ortalama = not_ortalamasi(notlar)
            print(f"Not ortalaması: {ortalama:.2f}")
        elif secim == '3':
            ortalama = not_ortalamasi(notlar)
            harf = harf_notu(ortalama)
            print(f"Harf notu: {harf}")
        elif secim == '4':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
    not örneği chatgptden alındı.
    """
"""
def carpma(a,b):
    return a*b
sonuc = carpma(4,6)
print(sonuc)
"24"
#def ile çarpma işlemi tanımladık ve bu çarpma işleminde a*b değerini döndürdük.
#böylece carpma(x,y) ile fonksiyonu her çağırdığımızda ilk sayıyı 2.sayıyla çarparak değer döndürecek
"""
"""
def helloworld():
    print("merhaba dünya")
helloworld()
#sabit tanımla helloworld fonksiyonunu her çağırdığımızda otomatik olarak ekrana merhaba dünya yazdırıyor.
"""
"""
def selam(isim="dünya"):
    print(f"merhaba {isim}")

selam()
selam("furkan")
"""
"""
def info(isim,yas):
    print(f"isim: {isim}\nyaş:{yas}")

info(yas=22, isim="furkan")
"""
""" 
pythonda listeleme yöntemleri ve kullanım alanları***
1-listeler
listeler sııralı ve değiştirilebilir en yaygın python listeleme yöntemidir.
listem = ["1","2","3","4","a","b","c"]:
 çıktısı 1,2,3,4,a,b,c olarak ekrana gelecektir.
listem.append(5)dersek
1,2,3,4,a,b,c,5 olarak ekrana yazdırılır.
listem.remove("a")dersek a harfi çıkacaktır.
listelerde erişim için index'ini yazıp çağırmamız gerekiyor
print listem[0]dersek çıktısı '1' olacaktır.
tanımlaması[] şeklinde yapılır

2-tuple'lar
tuple'lar değiştirilemez sıralı listelerdir tuple'abir şey eklemek istediğimizde
silmek veya manipüle etmek istediğimnizde typeError almış olacağız.
tanımlarken () kullanırız
tuple1=(1,2,3,4,'a','b','c')
print (tuple1[1])
çıktısı 2 olacaktır.
tuple1[1] = 13 #Hata TypeError alacağız.

3-set(kümeler)
Setler değiştirilebilir ve sırasızdır. aynı elemanlar kullanılamaz her eleman eşsizdir.
set1= {"1","2","3","4","a","b","c"}:
 çıktısı {1,2,3,4,a,b,c} olarak ekrana gelecektir.
listem.append(5)dersek
{1,2,3,4,a,b,c,5} olarak ekrana yazdırılır.
 Set elemanlarına indexle erişim sağlayamazsınız!,
 {} ile tanımlanır
 print(set1[1]) #Hata TypeError
 
4-Dictionary(sözlükler)
sözlükler anahtar ve değer çiflerinden oluşan değiştirilebilir sıralı veri yapısıdır.,
sozluk1={'isim': 'Ahmet', 'yaş': 25, 'şehir': 'İstanbul'}
print(sozluk)
çıktısı: isim: Ahmet yaş:25 şehir : istanbul
eleman eklemek için ekstra bir komut yoktur
sozluk1['meslek']= "mühendis" yazarak listenin en sonuna meslek : mührndis olarak ekleyebiliriz
del sozluk1['isim'] yazarak isim bölümünü sözlükten silebiliriz
erişim sağlamak için [] kullanırız
 print(sozluk1['sehir']) yazarsak sehir: istanbul yazdırılacaktır.
 
"""