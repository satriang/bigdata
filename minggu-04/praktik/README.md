# Bab 6

*membuat modul python dengan nama modul fibo.py*
```bash
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
*setelah itu modul tersebut bisa gunakan lagi dengan file yang berbeda dengan cara import*
```bash
>>> import fibo
```
*kita coba untuk menggunakan modul fibo dengan menampilkan bilangan fibo sampai dengan 1000*
```bash
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```
*untuk menggunakan modul python, bisa juga dengan cara nama modul ke dalam suatu variabel seperti contoh dibawah ini*
```bash
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
*selain import modul, kita dapat juga menggunakan fungsi yang terdapat di dalam modul. Contoh*
```bash
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
*selain itu kita juga dapat menggunakan semua fungsi yang terdapat pada modul. Contoh*
```bash
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
*nama modul dapat dialiaskan dengan nama yang lainnya. Contoh*
```bash
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
*pemanggilan alias dapat juga melalui from. Contohnya*
```bash
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
## Bab 6.1.1

*modul python juga dapat di eksekusi dengan menjalankan perintah Python kemudian nama modul. Contoh*
```bash
$ python3.7 fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
## Bab 6.1.2

*Jika modul diimport, intepreter pertama mencari dan akan membuild modul dengan nama tersebut. Jika tidak ditemukan dia akan mencari nama modul tersebut yang ada dalam list direktori yang di berikan variabel sys.path. sys.path*

## Bab 6.1.3

## Bab 6.2

*Python mempunyai kumpulan pustaka modul standart dari python. Kumpulan modul tersebut merupakan salah satu alternatif konfigurasi yang juga bergantung pada platform yang mendasarinya. Contoh*
```bash
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C>
```
*Dari contoh diatas merupakan salah satu modul yang digunakan untuk mengganti intepreter default dari python. Variabel sys.pathadalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkunganPYTHONPATH, atau dari bawaan bawaan jika PYTHONPATH tidak diatur. Anda dapat memodifikasinya menggunakan operasi daftar standar seperti contoh berikut*
```bash
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## Bab 6.3

*The built-in function dir() digunakan untuk mencari tahu nama-nama yang didefinisikan modul. Ini mengembalikan daftar string yang diurutkan. Contoh*
```bash
>>> import fibo, sys
>>> dir(fibo)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook','dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
```

## Bab 6.4

*Packages merupakan struktur modul python yang menggunakan dottes module name. Berikut contoh penggunaan dari packages*
```bash 
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
*Python mencari melalui direktori pada sys.path untuk melakukan pencarian ke sebuah  subdirektori paket. The __init__.pyfile diperlukan agar Python mengidentifikasi direktori sebagai direktori yang terdapat paket. ini dilakukan untuk mencegah direktori dengan nama yang sering digunakan. Cara penggunaan paket dengan cara import modul individual dari paket, misalnya:*
```bash
import sound.effects.echo
```
*alternatif yang lain untuk import submodul dengan contoh dibawah ini*
```bash
from sound.effects import echo
```

## Bab 6.4.1
*Untuk import semua modul, pada __init__.py dapat mendefinisikan kode _all_. Hal ini berarti semua modul di import dari sebuah paket. Cara lain yang dapat dilakukan dengan menambahkan karakter * untuk mengimport semua modul dalam sebuah paket. Contoh*
```bash
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```
*Dalam contoh ini, echo dan surround modul diimpor dalam namespace saat ini karena mereka didefinisikan dalam sound.effects paket saat pernyataan from...import dijalankan.*

# Bab 7

## Bab 7.1

*Untuk menggunakan Formated string literal, pertama gunakan simbol f atau F sebelim tanda kutip. Di dalam string ini, Anda dapat menulis Python expression antara {dan } karakter yang dapat merujuk ke variabel atau nilai literal. Contoh*
```bash
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```
*str.format() merupakan method yang memungkinkan kita menyesuaikan string secara manual sesuai kebutuhan. Tetapi masih menggunakan {and} untuk menandai variabel yang akan diganti atau memberiksn format yang detail. Contoh*
```bash
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```
*Ketika Anda tidak membutuhkan keluaran yang mewah tetapi hanya ingin menampilkan beberapa variabel untuk keperluan debugging, Anda dapat mengkonversi nilai apa pun ke string dengan fungsi repr()atau str().Fungsi str() digunakan untuk mengembalikan representasi dari nilai-nilai yang cukup terbaca-manusia, sementara repr()digunakan untuk menghasilkan representasi yang dapat dibaca oleh interpreter. Contoh*
```bash
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>>
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
...
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>>
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
...
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"x
```

## Bab 7.1.1
*Formatted string literals atau bisa disebut f-string untuk yang berformat pendek memungkinkan Anda menyertakan nilai ekspresi Python di dalam string dengan mengawali string denganfatauFdan menulis ekspresi sebagai {expression}. Penentu format opsional dapat mengikuti ekspresi. Ini memungkinkan kontrol lebih besar atas bagaimana nilai diformat. Contoh*
```bash
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```
*format integer setelah dikiuti tanda : memungkinkan untuk meminimalkan lebar karakter yang biasanya digunakan untuk membuat kolom berbaris. Contoh*
```bash
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>>
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
*Pengubah lain dapat digunakan untuk mengonversi nilai sebelum diformat. '!a'berlaku ascii(), '!s'berlaku str(), dan '!r' berlaku repr(). Contoh*
```bash
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
## Bab 7.1.2

*Penggunaan dasar dari str.format()metode ini terlihat seperti ini:*
```bash
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
*Tanda kurung dan karakter di dalamnya (disebut kolom format) diganti dengan objek yang dilewatkan ke dalam str.format()metode. Angka dalam tanda kurung dapat digunakan untuk merujuk pada posisi objek yang dilewatkan ke dalam str.format()metode.Contoh*
```bash
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```
*Jika argumen kata kunci digunakan dalam str.format()metode, nilainya akan dirujuk dengan menggunakan nama argumen. Contoh*
```bash
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```
*Posisi dan keyword statement dapat digabung.Contoh*
```bash
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```
*Jika Anda memiliki string format yang sangat panjang yang tidak ingin dipisahkan,  alangkah baiknya jika Anda bisa mereferensikan variabel yang akan diformat dengan nama alih-alih berdasarkan posisi. Ini dapat dilakukan hanya dengan melewati dikt dan menggunakan tanda kurung siku '[]'untuk mengakses kunci. Contoh*
```bash
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>>
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
*Ini juga bisa dilakukan dengan melewatkan tabel sebagai argumen kata kunci dengan notasi ```**```.Contoh*
```bash
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
*Ini sangat berguna dalam kombinasi dengan fungsi built-in vars(), yang mengembalikan kamus yang berisi semua variabel lokal.Sebagai contoh, garis-garis berikut menghasilkan satu set kolom-kolom yang diratakan memberikan integer dan kotak dan kubus. Contoh*
```bash
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
## Bab 7.1.3
*Ada metode lain str.zfill(),, yang memberikan string numerik di sebelah kiri dengan nol. Ia mengerti tentang tanda plus dan minus. Contoh*
```bash
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```
## Bab 7.1.4
*The %Operator juga dapat digunakan untuk string format. Ini menafsirkan argumen kiri seperti sprintf()string format -style untuk diterapkan ke argumen yang tepat, dan mengembalikan string yang dihasilkan dari operasi format ini. Sebagai contoh:*
```bash
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```
## Bab 7.2
*open()mengembalikan file objek , dan ini paling sering digunakan dengan dua argumen: .open(filename, mode). Contoh*
```bash
>>> f = open('workfile', 'w')
```
*Ini adalah praktik yang baik untuk menggunakan withkata kunci ketika berhadapan dengan objek file. Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaian selesai, bahkan jika pengecualian dibesarkan di beberapa titik. Penggunaannya withjuga jauh lebih pendek daripada menulis setara try- finallyblok. Contoh*
```bash
>>> with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
True
```
*Untuk membaca isi file, panggilan f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau byte objek (dalam mode biner).Contoh*
```bash
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```
*f.readline()membaca satu baris dari file; karakter baris baru ( \n) dibiarkan di ujung string, dan hanya dihilangkan pada baris terakhir file jika file tidak berakhir di baris baru.Contoh*
```bash
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```
*Untuk membaca garis dari sebuah file, Anda dapat mengulang objek file. Ini adalah memori yang efisien, cepat, dan mengarah ke kode sederhana.Contoh*
```bash
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```
## Bab 7.2.2
*Jika Anda memiliki objek x, Anda dapat melihat representasi string JSON-nya dengan baris kode sederhana.Contoh*
```bash
>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
```
# Bab 8
*Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contoh yang mungkin Anda lihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan:syntax errors and exceptions.*
## Bab 8.1
*Parser mengulangi garis yang menyinggung dan menampilkan sedikit 'panah' yang menunjuk pada titik paling awal di garis tempat kesalahan terdeteksi. Kesalahan ini disebabkan oleh (atau setidaknya terdeteksi pada) token yang mendahului panah: pada contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua ( ':') hilang sebelum itu. Nama file dan nomor baris dicetak sehingga Anda tahu di mana harus mencari jika input berasal dari skrip.contoh*
```bash
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```
## Bab 8.2
*Kesalahan terdeteksi selama eksekusi disebut exceptions. Anda akan segera belajar bagaimana menangani mereka dalam program Python. Sebagian besar pengecualian tidak ditangani oleh program, namun, dan menghasilkan pesan kesalahan.Contoh*
```bash
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
## Bab 8.3
*Pada klausa Try dan except merupakan langkah unuk menangani sebuah pengecualian. Pernyataan try akan dijalankan jika kondisi benar dan jika salah akan menjalankan klausa except. Except bisa di sesuaikan dengan kebutuhan aplikasi. Contoh*
```bash
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
Please enter a number: l
Oops!  That was no valid number.  Try again...
``` 
## Bab 8.4
*The raise pernyataan memungkinkan programmer untuk membuat pengecualian tertentu terjadi. Sebagai contoh:*
```bash
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
## Bab 8.5
*Exception dapat dibuat oleh pengguna dengan membuat kelas exception dimana kelas ini dapat menyesuaikan dengan keinginan pengguna. Bisa juga dibuat sebagai pesan kesalahan ataupun yang lainnya tergantu dari keinginan pengguna. Contoh*
```bash
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```
## Bab 8.6
*The trypernyataan memiliki klausul opsional lain yang dimaksudkan untuk menentukan tindakan bersih-bersih yang harus dijalankan dalam semua keadaan. Sebagai contoh:*
```bash
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>> KeyboardInterrupt
<class 'KeyboardInterrupt'>
```
## Bab 8.7
*Beberapa objek menetapkan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihatlah contoh berikut, yang mencoba membuka file dan mencetak isinya ke layar.*
```bash
for line in open("myfile.txt"):
    print(line, end="")
```



