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

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual. ##

Kita dapat membuat ekemen `<form>` secara manual melalui tag form, caranya sebagai berikut:
1. Memposting data ke URL tujuan (pengguna melakukan submit data)
2. Menyesuaikan pemilihan method untuk menyalurkan variabel-variabel pada URL tujuan menggunakan GET atau POST
3. Gunakan INPUT dan INPUT TYPE untuk data atribut dari browser ke server<br/>

##  Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. ##

Alur dari pengumpulan data pengguna sebagai berikut:
1. Pengguna membuat HTTP request melalui brower menuju alamat hosting
2. Server akan menerima HTTP Request pengguna lalu akan menghandle path yang sesuai menggunakan `views.py`. Server kemudian akan membuat HTML form yang akan dikirimkan ke browser pengguna
3. HTML akan ditampilkan dan pengguna bisa mengisi form. Browser akan membuat HTTP Request, method GET atau POST ke URL tujuan sesuai dengan HTML yang diterima
4. Server akan menerima request dan langsung meng-*handle* path melaksanakan request
5. Request akan dikembalikan kepada user menggunakan tampilan HTML</br>

##  Implementasi checklist ##

1. Masuk ke environtment lalu buat aplikasi baru dengan nama `todolist` menggunakan ```python manage.py startapp todolist```
2. Lakukan penambahan path nama aplikasi `todolist` pada `project_django` dan tambahkan path `path('todolist/', include('todolist.urls')),` dalam `urlpatterns` sehingga kita dapat mengakses layanan lokal melalui ```http://localhost:8000/todolist```
3. Buat model dengan nama `Task` lalu tambahkan atribut `user`, `date`, `title`, dan `description` pada `models.py`
``class Task(models.Model):
    ...``
4. Buat fungsi untuk ringkasan form utama todolist pengguna, registrasi, login, logout, membuat task baru, dan menghapus task
5. Buat interface aplikasi menggunakan HTML pada folder `templates`
6. Simpan atribut username, tombol `Add` untuk menambah task, tombol `Logout`, dan tabel yang berisi ringkasan input pengguna (tanggal pembuatan task, judul, deskripsi, tombol status, dan tombol hapus task)
7. Simpan atribut judul dan deskripsi task pada halaman `create-task`
8. Lakukan routing untuk masing-masing halaman pada `urls.py` yaitu untuk halaman utama, register, login, create-task, detele-task, update-status, dan  logout
9. Deploy aplikasi ke Heroku dan pastikan semua fungsi berjalan dengan baik. Lakukan langkah testing dengan login akun dan membuat todo list</b>

</b></b>
Sumber yang digunakan pada Tugas 4:
https://www.youtube.com/watch?v=Oy9K7iz3aa4
https://www.youtube.com/results?search_query=styling+button+in+html+in+the+middle+file+