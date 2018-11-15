# Jupyter Notebook

Jupyter Notebook adalah aplikasi web open-source yang memungkinkan Anda untuk membuat dan berbagi dokumen yang berisi kode langsung, persamaan, visualisasi dan teks naratif. 

# Fungsi Jupyter Notebook
* Edit kode di dalam browser
* Menjalankan kode dari browser
* Melihat hasil perhitungan dengan media representations, seperti HTML, LaTeX, PNG, SVG, PDF, dan lain sebagainya.
* Membuat dan menggunakan interactive JavaScript widgets
* Membuat dokumen dengan format Markdown
* Membuat persamaan matematika menggunakan sintaks LaTeX di Markdown yang kemudian dirender di-browser oleh MathJax 

# Cara Instalasi Jupyter Notebook di Linux Mint 19
Untuk instalasi Jupyter Notebook dapat menggunakan beberapa cara. Bisa menggunakan Conda, virtualenv atau pip. Disarankan dari  [sumber](http://jupyter.org/install "Pergi ke jupyter.org") menggunakan pip. Berikut langkah-angkah instalasi Jupyter Notebook menggunakan pip:

* Pastikan komputer anda sudah terinstal python. Cara mengetahui apakah komputer sudah terinstal python dengan cara ketikkan perintah *python --version* kemudian tekan enter. Setelah itu jika terdapat versi python berarti sudah terinstal seperti contoh dibawah ini
```bash
      $ python --version
        Python 3.6.7 :: Anaconda, Inc.
```
* Ketikkan perintah *python3 -m pip install --upgrade pip*. Langkah ini melakukan upgrade pada pip. Hasilnya seperti dibawah ini
```bash
        $ python3 -m pip install --upgrade pip
          Requirement already up-to-date: pip in ./miniconda3/lib/python3.6/site-packages (18.1)
```
* Selanjutnya ketikkan perintah *python3 -m pip install jupyter* untuk memulai instalasi. Pada proses ini yaitu mendownload package Jupypter Notebook. 
* Setelah proses Download dan instalasi sudah selesai jalankan perintah *jupyter notebook* untuk mencoba menjalankan server jupyter notebook. 
* Jika berhasil maka web browser akan tampil dan akan muncul gambar dibawah ini
![Gambar Web Server Jupyter Notebook](https://github.com/satriang/bigdata/tree/master/minggu-09/praktik/src/sc.png)

