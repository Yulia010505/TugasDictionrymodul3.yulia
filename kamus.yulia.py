kamus ={"jurusan Informatika":" ilmu yang mempelajari tentang ilmu komputer",
        "jurusan FFarmasi":" ilmu yang mempelajari tentang pengembangan dan penggunaan obat-obatan",
        "jurusan Peternakan":" ilmu yang mempelajari pengembangan sumber daya hewan",
        "jurusan Arsitektur":" ilmu yang mempelajari desain dan perencanaan bangunan"
        }
kata= input("masukkan kata yang ingin anda cari di dalam kamus:")

if kata in kamus:
    print(f"Arti dari'{kata}' adalah: {kamus[kata]}")
else:
    print(f"sorry,  arti dari'{kata}' yang anda cari tidak terdaftar dalam kamus.")
