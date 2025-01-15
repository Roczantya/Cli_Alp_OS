# Fany's CLI
Fany's CLI adalah alat **Command Line Interface (CLI)** khusus yang dibuat dengan Python. Alat ini menyediakan berbagai fungsi untuk manajemen file dan direktori, navigasi sistem, serta utilitas tambahan. Alat ini dirancang untuk menyederhanakan tugas-tugas umum dan mencakup perintah standar serta perintah tambahan untuk operasi lanjutan.

## Fitur
#### Perintah Standar
* `ls [path]` - Menampilkan isi direktori (default adalah direktori saat ini).
* `pwd` - Menampilkan direktori kerja saat ini.
* `cd <path>` - Mengubah direktori kerja saat ini ke path yang ditentukan.
* `mkdir <path>` - Membuat direktori baru pada path yang ditentukan.
* `rmdir <path>` - Menghapus direktori kosong.
* `touch <path>` - Membuat file kosong pada path yang ditentukan.
* `rm <path>` - Menghapus file pada path yang ditentukan.
* `cp <source> <destination>` - Menyalin file dari sumber ke tujuan.
* `mv <source> <destination>` - Memindahkan atau mengganti nama file atau direktori.
* `clear` - Membersihkan layar terminal.
* `help` - Menampilkan daftar perintah yang tersedia beserta deskripsinya.
* `exit` - Keluar dari CLI.

#### Perintah Tambahan
* `search <pattern>` - Mencari file atau direktori yang sesuai dengan pola.
* `tree` - Menampilkan struktur direktori dalam bentuk pohon.
* `treec`- Menampilkan struktur direktori drive C:\ dalam bentuk pohon dengan entri terbatas.
* `find_large <size>` - Menemukan file yang lebih besar dari ukuran tertentu (dalam KB).
* `size <file_name>` - Menampilkan ukuran file yang ditentukan.
* `kobo` - Menampilkan gambar menarik dari Kobo Kanaeru.
* `pantun` - Menikmati dan membuat pantun yang menyenangkan dan menginspirasi.

## Utilitas Tambahan
* `display_tree_DirC`: Menampilkan struktur direktori drive C:\ secara rekursif dengan batasan entri dan kedalaman.
* `find_large_files`: Menemukan file yang lebih besar dari ukuran tertentu dengan hasil dibatasi hingga 10 entri untuk efisiensi.

## Cara Penggunaan
  1. Jalankan CLI: Jalankan skrip Python dengan perintah berikut di terminal:
      ```
      python cli.py
      ```
  3. Lihat Bantuan: Ketik `help` untuk melihat daftar perintah yang tersedia.

  4. Jalankan Perintah: Masukkan salah satu perintah yang terdaftar di bagian bantuan untuk menjalankan operasi.
    Contoh:
      ```
     Fany's CLI> ls
      ```
  5. Keluar dari CLI: Ketik `exit` untuk keluar dari program.

## Catatan

> Alat ini mencakup penanganan kesalahan untuk masalah umum seperti file atau direktori yang hilang dan kesalahan izin.
Fungsi `display_tree_DirC` dioptimalkan untuk menangani struktur direktori besar dengan membatasi entri dan kedalaman.
Perintah tambahan menyediakan fungsionalitas yang lebih baik, seperti pencarian file, analisis file besar, dan output menarik.

## Kontribusi
  Silakan berkontribusi pada `Fany's CLI` dengan mengusulkan fitur baru atau melaporkan masalah. Kontribusi dapat dilakukan melalui pull request.


