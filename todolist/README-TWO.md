# Tugas 6: Javascript dan AJAX
<b>Undissya Putri Maharani
<b>2106650935 - PBP F

<b>Tampilan Register [here](https://katalogapplication.herokuapp.com/todolist/)<br/>

<b>Akun Dummy

Username = dumm4, password = fasilkom1
Username = dummy0, password = fasilkom1

## Perbedaan antara asynchronous programming dengan synchronous programming ##

<b> Asynchronous Programming </b><br>
Asynchronus programming akan terus menjalankan program tanpa perlu memperhatikan I/O. Jadi, program dapat berjalan tanpa perlu menunggu proses selesai. Secara independen, program dapat mengeksekusi beberapa proses sehingga pengguna dapat mendapatkan respons lebih cepat daripada synchronus programming.

<b> Synchronous Programming </b><br>
Synchronus programming akan melakukan eksekusi satu per satu proses berdasarkan urutan prioritas. Secara modular, untuk melakukan proses lain, pengguna perlu untuk meunggu event yang sedang dieksekusi untuk berakhir. Terdapat antrean eksekusi program karena program berjalan secara sequential.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini ##
Suatu Event-Driven Programming akan bergantung pada event yang diberi oleh pengguna. Proses penerapannya ada event - trigger - event handler - event loop - event - drive. Contoh penerapan pada tugas kali ini adalah saat menambah task, pengguna diminta untuk melakukan event Submit yang akan mengembalikan respons card secara asinkronus.<br>

## Penerapan asynchronous programming pada AJAX ##
Asynchronis programming pada AJAX berarti client dapat mendapatkan halaman terbaru tanpa perlu me-reload keseluruhan page. Penerapan asynchronus dapat dengan mengubah View dan Template pada aplikasi. Tambahkan fungsi yang akan merujuk pada pembaruan langsung tampa redirect ke page lain. Ubah atau tambahkan routing pada `urls.py` ke alamat json. Pakai AJAX GET atau AJAX POST dalam mengambil data ke server.<br>

## Implementasi Checklist ##
- Manipualasi tugas 4 dengan AJAX, gunakan AJAX GET untuk mengambil data json dan AJAX POST untuk meminta tambah pekerjaan secara asinkronus
- Ubah `views.py` dengan menambah fungsi untuk menampilkan data json dan fungsi untuk menambah task ajax 
- Ubah `urls.py`dengan menambahkan path untuk mengembalikan data json `.../todolist/json`dan menambah data ajax `.../todolist/add`
- Perbarui tampilan html dengan meng-import bootstrap, letakkan pada head
- Lanjut dengan membuat `<script>` (Javascript) yang berisi pembaruan dari tugas 4
- Melakukan load data json pada path `.../todolist/json`
- Menampilkan data pada card dengan memodifikasi card dengan AJAX dan mengecek data dengan loop 
- Ubah delete task berdasarkan ID yang valid dengan AJAX
- Karena sudah modifikasi pada card, lanjut untuk modisikasi button `Add Task`. Gunakan modal agar dapat menambah task secara asinkronus, minta pengguna untuk mengisi form.
- Untuk mengecek, lakukan refresh secara asinkronus untuk penambahan data, halaman utama todolist akan memperbarui tanpa me-reload seluruh halaman