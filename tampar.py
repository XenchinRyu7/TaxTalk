import time
import sys

def ketik(teks, delay=0.05):
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    lirik = [
        ("Entah sudah selasa yang ke berapa", 2),
        ("Masih saja kau ada lekat di kepala", 2),
        ("Hari ini janji esok mesti lupa", 2),
        ("Tetapi hati tak tepati", 2),
        ("Tampar aku di pipi", 1.5),
        ("Biar sadar dan ku mengerti", 1.5),
        ("Hujan samarkan derasnya", 1.5),
        ("Tutup air mata", 1.5),
        ("Temani kecewaku yang telah lama", 2),
        ("Berdosa kah ku berdoa", 2),
        ("Minta kau terluka", 2),
        ("Dan tinggalkan dirinya", 2),
        ("Hari ini janji esok mesti lupa", 2),
        ("Tetapi hati tak tepati", 2),
        ("Tampar aku di pipi", 1.5),
        ("Biar sadar dan ku mengerti", 1.5),
        ("Hujan samarkan derasnya", 1.5),
        ("Tutup air mata", 1.5),
        ("Temani kecewaku yang telah lama", 2),
        ("Berdosa kah ku berdoa", 2),
        ("Minta kau terluka", 2),
        ("Dan tinggalkan dirinya", 2),
        ("Ho", 1),
        ("Bukan ku tak berupaya", 1.5),
        ("Berusaha", 1.5),
        ("Hujan samarkan derasnya", 1.5),
        ("Tutup air mata", 1.5),
        ("Tiga tahun tak terasa", 2),
        ("Masih kau yang ada", 2),
        ("Bodoh yang sebenarnya", 2),
        ("Tampar aku di pipi", 1.5),
        ("Sadarkan kau aku takkan terjadi", 2)
    ]
    
    for baris, jeda in lirik:
        ketik(baris)
        time.sleep(jeda)

if __name__ == "__main__":
    main()
