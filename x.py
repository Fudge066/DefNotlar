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

