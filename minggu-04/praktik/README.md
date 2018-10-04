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



