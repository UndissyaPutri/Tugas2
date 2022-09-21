# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

**Undissya Putri Maharani**<br/>
**2106650935 - PBP F**

**Halaman Utama Aplikasi** [here](https://katalogapplication.herokuapp.com/)<br/>
**Halaman HTML** [here](https://katalogapplication.herokuapp.com/mywatchlist/html/)<br/>
**Halaman JSON** [here](https://katalogapplication.herokuapp.com/mywatchlist/json/)<br/>
**Halaman XML** [here](https://katalogapplication.herokuapp.com/mywatchlist/xml/)<br/>

## Perbedaan antara JSON, XML, dan HTML ## 

HTML
HTML merupakan kependekan dari HyperText Markup Language. HTML digunakan untuk mendesain halaman web menggunakan bahasa markup. Bahasa menggunakan tag untuk menentukan manipulasi apa yang harus dilakukan pada teks.<br/>

JSON
JSON merupakan kependekan dari JavaScript Object Notation, JSON adalah format pertukaran data yang ringan dan tidak bergantung pada bahasa. Ini didasarkan pada bahasa pemrograman JavaScript dan mudah dimengerti dan dihasilkan.<br/>

XML
XML adalah kependekan dari Extensible markup language dirancang untuk membawa data, bukan untuk menampilkan data. XML adalah bahasa markup yang mendefinisikan seperangkat aturan yang fokus pada kesederhanaan, umum, dan kegunaan di Internet.<br/>

Perbedaan dari ketiganya adalah
HTML
- Sangat mudah untuk dipelajari dan digunakan
- HTML merupakan platform independen
- Gambar, video, dan audio dapat ditambahkan ke halaman web
- Hypertext dapat ditambahkan ke teks<br/>

JSON
- Mudah untuk digunakan
- Kinerja JSON cukup cepat
- JSON bersifat open source dan gratis untuk digunakan
- Hasil JSON bersih dan kompatibel yang mudah dibaca
- JSON tidak memerlukan pustaka lain untuk diproses<br/>

XML
- XML dirancang untuk membawa data
- XML sult untuk dibaca dan diinterpretasikan
- Lebih terjamin keamanannya daripada JSON<br/>

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? ##

Alasan pentingnya menggunakan data delivery adalah kita dapat dengan mudah mengakse dan mengirim ke pengguna dan aplikasi. Biasanya kita dapat menggunakan HTML, JSON, atau XML dalam mengolah data. Dengan begitu, kita data yang ada jadi lebih terstruktur dan dapat memprediksi keadaan jangka panjang dengan data.<br/>

## Implementasi Checklis ##

1. Pertama kita dapat membuat aplikasi baru dengan `python manage.py startapp mywatchlist`, selanjutnya kita bisa set up migrasi skema model ke database Django lokal.
2. Kita dapat mengolah data dalam `fixtures`, dalam file `initial_mywatchlist_data.json`. Jangan lupa untuk loaddata untuk memasukkan datababse ke Django lokal.
3. Kita dapat set up `urls.py` dilanjutkan dengan runserver agar dapat melihat halaman pada `http://localhost:8000/mywatchlist/`.
4. Olah model dengan 5 atribut yaitu `watched`, `title`, `rating`, `release_date`, `review`. Buat juga format untuk HTML, JSON, dan HML sekaligus routingnya dengan URL `http://localhost:8000/mywatchlist/` + `format`.
5. Terakhir, kita dapat langsung melakukan deploy ke Heroku dan dapat di tes kebenarannya. Gunakan juga Postman untuk uji coba API sehingga aplikasi yang kita kembangkan tervalidasi.

## Screenshot Postman ##
1. HTML
![messageImage_1663767760728](https://user-images.githubusercontent.com/112463909/191523457-b2f3590f-eb17-4582-88d0-69fa64a44df8.jpg)
2. JSON
![messageImage_1663767690504](https://user-images.githubusercontent.com/112463909/191522841-ee3a0f93-4eda-4523-8269-87911b06bed9.jpg)
3. XML
![messageImage_1663767822767](https://user-images.githubusercontent.com/112463909/191524565-7b0cd721-f796-4955-a804-69e323cd08ec.jpg)
