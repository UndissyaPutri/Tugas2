# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

**Undissya Putri Maharani**<br/>
**2106650935 - PBP F**

**Tampilan Register** [here](http://localhost:8000/todolist/register/)<br/>
**Tampilan Login** [here](http://localhost:8000/todolist/login/)<br/>
**Halaman TODO List** [here](http://localhost:8000/todolist/)<br/>
**Halaman New Task** [here](http://localhost:8000/todolist/create-task/)<br/>

##  Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`? ## 

CSRF adalah kependekan dari Cross Site Request Forgery. Django memiliki fitur proteksi secara default untuk mengatasi serangan CSRF. Tujuannya adalah untuk mengecek form yang diisi dan dikirim balik berasal dari pengguna atau bukan. Django akan mengecek token tersebut, jika sesuai maka akan memproses request pengguna.<br/>

Kita dapat membuat form kita dengan sengaja tidak ingin dicek karena data yang diisi tidak rahasia. Gunakan `@csrf_exempt`untuk mengabaikan token.<br/>

Apabila kita tidak menggunakan `{% csrf_token %}` pada form, maka ada kemungkinan hacker dapat mengirim form yang sudah di modifikasi dan menjadi berbahaya lalu dikirim ke website kita. Tidak ada pengecekan pada data yang masuk sehingga keamanan website rendah dan bisa merugikan *developer* dan pengguna.<br/>




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
