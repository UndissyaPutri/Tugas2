# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

##### Undissya Putri Maharani
##### 2106650935
##### PBP-F

**Halaman Utama Aplikasi** [here](https://katalogapplication.herokuapp.com/)
**Katalog Aplikasi** [here](https://katalogapplication.herokuapp.com/katalog/)\

## Bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html` ## 

!(https://github.com/UndissyaPutri/tugas2/issues/1#issue-1373095661)

- Terdapat request dari klien melalui web browser
- Request diterima dan dilanjutkan routing oleh URL (urls.py)
- Request diteruskan ke View (views.py) yang sesuai
- Terdapat operasi dengan data menggunakan Model (models.py)
- Model akan mengambil data dari database
- HTTP Response akan berisi penyelesaian dari request klien
- Web browser akan menampilkan web page sebagai bentuk respons kepada klien\

## Mengapa menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment?* ##

Alasan pentingnya menggunakan virtual environment:
1. Apabila kita sedang mengerjakan banyak proyek, tak jarang, kita memerlukan *library* yang berbeda. Jika hanya memiliki 1 environtment global, maka  kita tidak dapat bekerja dengan versi yang berbeda sehingga proyek jadi tidak terorganisir dan banyak tumpang tindih.
2. Virtual environment memberikan perkembangan environment yang independen dalam sistem operasi. Hal ini menyebabkan tingginya tingkat konsistensi program apabila ada perpindahan mesin.
3. Perpindahan *package directory* rapih, tidak banyak menampung *package* yang tidak penting.

Apakah kita dapat membuat aplikasi web tanpa virtual environment?
Ya, bisa. Namun, penggunaan virtual environment lebih direkomendasikan karena dapat menjadi sandbox saat menginstall *library* apapun tanpa memberi pengaruh pada komputer. Ketika virtual environment dihapus, maka *library* yang kita install menjadi hilang. Virtual environment membantu meminimalisir masalah pengembangan dan produksi.\

## Penjelasan cara kamu implementasi poin 1 sampai dengan 4 di atas ##
1. Kita dapat menambahkan fungsi pada file `views.py` untuk mengambil data dari model yang tersedia. Fungsi tersebut berguna untuk mengambil data pada CatalogItem. Dictionary yang dibentuk akan diteruskan untuk dikembalikan dalam HTML.
2. Lanjutkan dengan migrasi skema model ke dalam database lokal dan masukkan data ke dalam database Django lokal. Lalu, bentuk routing pada file `urls.py` dengan memetakan fungsi yang telah dibikin pada langkah pertama. 
3. Lakukan pengambilan data dari database dengan meng-import ke `views.py`. Panggil fungsi `show_katalog` untuk memanggil fungsi query ke model database. Jangan lupa untuk tambahkan `context` untuk mengembalikan fungsi render. 
4. Mapping dilakukan terhadap data dan dimunculkan pada halaman HTML. Modifikasi file `katalog.html` dan gunakan `list_barang` untuk menampung objek dan panggil dengan nama spesifik. 
5. Terakhir, lakukan *deployment* ke Heroku untuk mendapatkan hasil aplikasi web. Jangan lupa pastikan API sesuai untuk Github dan Heroku.\


Resource:
https://complicatedphenomenon.gitlab.io/2018/06/15/django/