# Cohorts_python_uygulama_2
# Python ile Öklid Mesafesi Hesaplama

## Genel Bakış
Bu Python betiği, 2D uzayındaki noktalar arasındaki Öklid mesafelerini hesaplar. Özel bir fonksiyon kullanarak mesafeleri hesaplar ve tüm nokta çiftleri arasındaki en küçük mesafeyi bulur.

## Özellikler
- 2D noktaları demetler (tuple) olarak tanımlayın.
- Matematiksel bir formül kullanarak iki nokta arasındaki Öklid mesafesini hesaplayın.
- Mesafeleri bir listede saklayın ve en küçük mesafeyi bulun.

## Nasıl Çalışır?
1. **Noktaların Tanımlanması**: `points` listesi, 2D koordinatları temsil eden demetlerden oluşur (örneğin `(x, y)`).
2. **Mesafe Hesaplama**:
   - `euclideanDistance` fonksiyonu, iki nokta arasındaki mesafeyi şu formül ile hesaplar:
     \[ \text{mesafe} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \]
3. **Döngüsel Çiftler Hesaplaması**: İç içe döngü ile listedeki her nokta çifti için mesafeler hesaplanır.
4. **Sonuçların Saklanması**: Hesaplanan tüm mesafeler `distances` listesine eklenir.
5. **Minimum Mesafenin Bulunması**: `min()` fonksiyonu kullanılarak en küçük mesafe belirlenir.

## Betik Çıktısı
Betik şu çıktıları verir:
1. Tüm nokta çiftleri için hesaplanan mesafelerin listesi.
2. Bu çiftler arasındaki en küçük mesafe.

## Örnek
Giriş Noktaları:
```python
points = [(1, 2), (4, 6), (7, 1), (3, 3)]
```

Çıktı:
```
Mesafeler: [5.0, 6.324555320336759, 2.23606797749979, 5.830951894845301, 4.47213595499958, 4.123105625617661]
Minimum mesafe: 2.23606797749979
```

## Gereksinimler
- Python 3.x
- `math` modülü (standart kütüphane)

## Çalıştırma Talimatları
1. Betiği bir dosyaya kaydedin, örneğin `euclidean_distance.py`.
2. Betiği çalıştırın:
   ```bash
   python euclidean_distance.py
   ```

## Özelleştirme
- Farklı noktalar için mesafeleri hesaplamak üzere `points` listesine yeni noktalar ekleyebilir veya mevcut noktaları değiştirebilirsiniz.
- 3D noktaları desteklemek için `euclideanDistance` fonksiyonunu güncelleyerek işlevselliği genişletebilirsiniz.

