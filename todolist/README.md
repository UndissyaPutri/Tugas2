# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

**Undissya Putri Maharani**<br/>
**2106650935 - PBP F**

**Tampilan Register** [here](https://katalogapplication.herokuapp.com/todolist/register/)<br/>
**Tampilan Login** [here](https://katalogapplication.herokuapp.com/todolist/login/)<br/>
**Halaman TODO List** [here](https://katalogapplication.herokuapp.com/todolist/)<br/>
**Halaman New Task** [here](https://katalogapplication.herokuapp.com/todolist/create-task/)<br/>

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

</br></br>

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

## Perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style? ##

<b> Inline Style </b>
Kode internal CSS merupakan kode yanng berisi tampilan aplikasi yang diletakkan sebagai atribut pada bagian HTML, biasanya kode CSS ada pada `head`. 

```
<style>
body {
    background-color: blue;
}
h1 {
    color: red;
    padding: 60px;
} 
</style>
```

Kelebihan:
- Lebih cepat karena pembacaan kode secara langsung dalam satu file
- Perubahan hanya ada dalam satu halaman<br>

Kekurangan:
- Hanya aktif pada halaman tertentu tempat kode berada
- Sulit jika digunakan untuk banyak modul<br>

<b> Internal Style Sheet </b>
Inline CSS digunakan di dalam tag kode HTML langsung. Biasanya style akan diterapkan pada ID, class, atau elemen.

```
<h1 style="color:white;padding:30px;">Hostinger Tutorials</h1>
<p style="color:white;">Something usefull here.</p>
```

Kelebihan:
- Efektif untuk melakukan perubahan ringan kode
- Digunakan untuk *testing* tampilan<br>

Kekurangan:
- Terjadi redundan, pengulangan style pada tiap elemen
- Loading page semakin berat<br>

<b> External Style Sheet </b>
Eksternal CSS pelru duhubungkan ke file eksternal yang bertipe .css. Perubahan yang terjadi akan mempengaruhi keseluruhan tampilan. 

```
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>
```

Kelebihan:
- Rapi dalam penulisan kode
- Mudah untuk melakukan perubahan saat berkolaborasi<br>


Kekurangan:
- Ada delay dalam pengaksesan file eksternal
- Waktu *load* halaman dapat belum ditampilkan secara sempurna<br>

## Tag HTML 5 ##
Dalam pengerjaan tugas kali ini, saya menggunakan beberapa tag seperti berikut,
1. `<a>`digunakan untuk hyperlink web page
2. `<b>`digunakan untuk memberi *style* bold
3. `<body>` digunakan untuk mendeklarasikan bagian utama HTML
4. `<br>` digunakan untuk merepresentasikan whitespace line break atau enter
5. `<button>` digunakan untuk membuat kontrol tombol
6. `<div>` digunakan untuk mendefinisikan suatu bagian yang dapat berisi elemen
7. `<dl>` digunakan untuk mendefinisikan *definiiton list*
8. `<form>` digunakan untuk merepresentasikan form pada dokumen seperti input, button
9. `<h1>, <h2>, ..., <h6>` digunakan untuk merepresentasikan heading sesuai dengan level yang diinginkan
10. `<head>` digunakan untuk merepresentasikan bagian awal seperti judul, deskripsi
11. `<html>` digunakan untuk merepresentasikan induk dari HTML 
12. `<input>` digunakan untuk mengontrol input user
13. `<label>` digunakan untuk merepresentasikan form 
14. `<li>` digunakan untuk merepresentasikan *list item*
15. `<meta>` digunakan untuk merepresentasikan metadata seperti `<title>, <base>, dan <style>`
16. `<p>` digunakan untuk merepresentasukan paragraf
17. `<style>` digunakan untuk mengubah gaya dari elemen mengguankan dokumentasi style
18. `<table>` digunakan untuk merepresentasikan tabel lebih dari satu dimensi emnggunakan baris dan kolom
19. `<title>` digunakan untuk merepresentasikan judul
20. `<ul>` digunakan untuk  <br>

## Tipe CSS Selector#
**1. ID Selector**
Selector yang penggunaannya memerlukan id unik dari elemen HTML 
```
#title1 {
    text-align: center;
    padding-top: 15px;
}
```

**2. Classes Selector**
Selector yang penggunaannya berdasar pada nama elemen HTML
 ```
h1 {
    font-size: 12px;
    width: 100%;
    font-weight: bold;
}
 ```

**3. Element Selector**
Selector yang penggunaannya memanggil class yang telah didefinisikan pada elemen HTML
```
.class1 {
    width: 400px;
    margin: auto;
    padding: 100px;
}
```
**4. Universal Selector**
Selector yang menggunakan `*` dalam mendeklarasikan *style*
```
* {
    margin: 8px 0;
    display: inline-block;
    box-sizing: border-box;
}
```
<br>

## Implementasi Checklist ##
- Implementasi External Style Sheet CSS dengan membuat folder `static` yang berisi file dengan tipe .css. Di dalam file .css ini, kita perlu menggunakan kreativias dalam memberi gaya. Jangan lupa untuk menyambungkan file .css pada file .html di `Templates` menggunakan
```
{% load static %}
<head>
    <link rel="stylesheet" href="{% static 'logincss.css' %}">
</head>
```
- Lakukan kustomisasi untuk 4 halaman, utama, login, register, dan create_task. Tambahkan framework untuk mempermudah perubahan. 
- Ubah tabel pada `todolist.html` dari bentuk tabel menjadi card. Pembaruan ini dapat dengan menggunakan `<div>`. 
```
{% for todo in todolist %}
    <div class="card lg:grid-cols-4 md:grid-cols-3 gap-5 mt-8 sm:mt-5">
        {% if todo.is_finished == False %}
            <p style="text-align: end; font-size: 85%; opacity: 0.7;">{{todo.date}}</p>
            <h2>{{todo.title}}</h2>
            <p style="font-size: 90%;">{{todo.description}}</p>
            <h4>Pending</h4>
                <div style="text-align: end;">
                    <a href="/todolist/update-status/{{todo.id}}">
                        <button class="update" type="submit">Update</button>
                    </a>
                    <a href="/todolist/delete-task/{{todo.id}}">
                        <button class="delete" type="submit">Delete</button>
                    </a>
                </div>
                ...
```
- Membuat semua halaman menjadi *responsive* dengan mengimport `{% extends 'base.html' %}` dan tambahkan `display: flex;` saat memberi *style* utama halaman