# Tutorial belajar Python


## Bab 2

 * satria@satria-HP-1000:~$ python3.7

Python 3.7.0 (default, Sep 12 2018, 05:42:18) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be Carefull not to fall off!")
... 
Be Carefull not to fall off!

*Perintah Untuk mengawali dalam penggunaan bahasa pemrograma Python* 
## Bab 3

### 3.1.1 Angka
.>>> 2+2

4


.>>> 50 - 5

45

.>>> (50 - 5*6) / 4

5.0

.>>> 8/5

1.6

.>>> 17 / 3

5.666666666666667

.>>> 17 // 3

5

.>>> 17 % 3

2

.>>> 5 * 3 + 2

17

.>>> 5 ** 2 

25

.>>> 2 ** 7

128

.>>> width = 20
.>>> height = 5 * 9
.>>> width * height

900

.>>> n  # try to access an undefined variable

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
.>>> 4 * 3.75 - 1

14.0

.>>> tax = 12.5 / 100

.>>> price = 100.50

.>>> price * tax

12.5625

.>>> price + _

113.0625

.>>> round(_, 2)

113.06

*dari bagian diatas merupakan cara menggunakan berbagai macam operasi matematika dengan bahasa program python*

### 3.1.2 String

.>>> 'spam eggs'  # single quotes

'spam eggs'

.>>> 'doesn\'t'

"doesn't"

.>>> "doesn\'t"

"doesn't"

.>>> '"Yes," they said.

  File "<stdin>", line 1
    '"Yes," they said.
                     ^
SyntaxError: EOL while scanning string literal

.>>> '"Yes," they said.'

'"Yes," they said.'

.>>> "\"Yes,\" they said."

'"Yes," they said.'

.>>> '"Isn\'t," they said.'

'"Isn\'t," they said.'

.>>> '"Isn\'t," they said.'

'"Isn\'t," they said.'

.>>> print('"Isn\'t," they said.')

"Isn't," they said.

.>>> s = 'First line.\nSecond line.'

.>>> s

'First line.\nSecond line.'

.>>> print(s)

First line.

Second line.

.>>> print('C:\some\name')

C:\some
ame

.>>> print(r'C:\some\name')

C:\some\name

.>>> print("""\

. ... Usage: thingy [OPTIONS]

...      -h                        Display this usage message

...      -H hostname               Hostname to connect to

... """)

Usage: thingy [OPTIONS]

     -h                        Display this usage message

     -H hostname               Hostname to connect to

.>>> 3 * 'un' + 'ium'

'unununium'

.>>> 'Py' 'thon'

'Python'

.>>> text = ('Put several strings within parentheses '

...             'to have them joined together.')

.>>> text

'Put several strings within parentheses to have them joined together.'

.>>> prefix = 'Py'

.>>> prefix 'thon'

 File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax

.>>> ('un' * 3) 'ium'

  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax

.>>> prefix + 'thon'

'Python'

.>>> word = 'Python'

.>>> word[0]

'P'

.>>> word[5]

'n'

.>>> word[-1]

'n'

.>>> word[-2]

'o'

.>>> word[-6]

'P'

.>>> word[0:2]

'Py'

.>>> word[2:5]

'tho'

.>>> word[:2] + word[2:]

'Python'

.>>> word[:4] + word[4:]

'Python'

.>>> word[:2]

'Py'

.>>> word[4:]

'on'

.>>> word[-2:]

'on'

.>>> word[42]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

.>>> word[4:42]

'on'

.>>> word[42:]

''

.>>> word[0] = 'J'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

.>>> word[2:] = 'py'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

.>>> 'J' + word[1:]

'Jython'

.>>> word[:2] + 'py'

'Pypy'

.>>> s = 'supercalifragilisticexpialidocious'

.>>> len(s)

34

.>>> squares = [1, 4, 9, 16, 25]

.>>> squares

[1, 4, 9, 16, 25]

.>>> squares[0]

1

.>>> squares[-1]

25

.>>> squares[-3:]

[9, 16, 25]

.>>> squares[:]

[1, 4, 9, 16, 25]

.>>> squares + [36, 49, 64, 81, 100]

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

.>>> cubes = [1, 8, 27, 65, 125] 

.>>> 4 ** 3

64

.>>> cubes[3] = 64

.>>> cubes

[1, 8, 27, 64, 125]

.>>> cubes.append(216)

.>>> cubes.append(7 ** 3) 

.>>> cubes

[1, 8, 27, 64, 125, 216, 343]

.>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

.>>> letters

['a', 'b', 'c', 'd', 'e', 'f', 'g']

.>>> letters[2:5] = ['C', 'D', 'E']

.>>> letters

['a', 'b', 'C', 'D', 'E', 'f', 'g']

.>>> letters[2:5] = []

.>>> letters

['a', 'b', 'f', 'g']

.>>> letters[:] = []

.>>> letters

[]

.>>> letters = ['a', 'b', 'c', 'd']

.>>> len(letters)

4

.>>> a = ['a', 'b', 'c']

.>>> n = [1, 2, 3]

.>>> x = [a, n]

.>>> x

[['a', 'b', 'c'], [1, 2, 3]]

.>>> x[0]

['a', 'b', 'c']

.>>> x[0][1]

'b'

*dari bagian diatas merupakan cara-cara yang digunakan untuk melakukkan pengolahan untuk string dimulai dari membentuk kata, menghitung banyaknya huruf sampai mengambil beberapa huruf yang ada di dalam variabel* 

### 3.2

.>>> a, b = 0, 1

.>>> while a < 10:

...     print(a)

...     a, b = b, a+b

... 

0

1

1

2

3

5

8

.>>> i = 256*256

.>>> print('The value of i is', i)

The value of i is 65536

.>>> a, b = 0, 1

.>>> while a < 1000:

...     print(a, end=',')

...     a, b = b, a+b

... 

0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,>>>

*bagian diatas merupakan bentuk dari penggunaan while yang pada kasus diaatas di gunakan untuk menentukan bilangan berapa saja yang termasuk bilangan fibonasi*

##Bab 4

.>>> x = int(input("Please enter an integer: "))

Please enter an integer: 42

.>>> if x < 0:

...     x = 0

...     print('Negative changed to Zero')

... elif x == 0:

...     print('Zero')

... elif x == 1:

...     print ('Single')

... else:

...     print('More')

... 

More

*Dari bagian diatas merupakan cara penggunaan notasi if pada bahasa program python*

.>>> words = ['cat', 'window', 'defenestrate']

.>>> for w in words:

...     print(w, len(w))

... 

cat 3

window 6

defenestrate 12

*Bagian diatas ialah menampilkan isi dari variabel yang di atur secara array* 

.>>> for w in words[:]:

...     if len(w) > 6:

...             words.insert(0, w)

... 

.>>> words

['defenestrate', 'cat', 'window', 'defenestrate']

*Contoh diatas merupakan kombinasi antara penggunaan statement if dan for*

.>>> for i in range(5):

...     print(i)

... 

0

1

2

3

4

*menampilkan 5 bilangan dimulai dari 0 dengan menggunakan statement for untuk membuat perulangan*
 
.>>> range(5, 10)

range(5, 10)

.>>> for i in range(5, 10):

...     print(i)

... 

5

6

7

8

9

*dari bagian diatas merupakan fungsi perulangan untuk menampilkan bilangan yang dimulai dari angka 5 sampai dengan kurang dari 10 
.>>> for i in range(0, 10, 3):

...     print(i)

... 

0

3

6

9

*menampilkan bilangan yang dimulai dari 0 sampai kurang dari 10 yang berkelipatan 3*

.>>> for i in range(-10, -100, -30):

...     print(i)

... 

-10

-40

-70

*menampilkan bilangan yang dimulai dari -10 sampai kurang dari -100 yang berkelipatan -30*

.>>> a = ['Mary', 'had', 'a', 'little', 'lamb']

.>>> for i in range(len(a)):

...     print(i, a[i])

... 

0 Mary

1 had

2 a

3 little

4 lamb

*menampilkan index kata yang terdapat pada suatu variabel array*

.>>> print(range(10))

range(0, 10)

*
.>>> list(range(5))

[0, 1, 2, 3, 4]

.>>> for n in range(2, 10):

...     for x in range(2, n):

...             if n % x == 0:

...                     print(n, 'equals', x, '*', n//x)

...                     break

...     else:

...             print(n, 'is a prime number')

... 

2 is a prime number

3 is a prime number

4 equals 2 * 2

5 is a prime number

6 equals 2 * 3

7 is a prime number

8 equals 2 * 4

9 equals 3 * 3

*dari bagian diatas digunakan untuk menentukan bilangan utama*

.>>> for num in range(2, 10):

...  if num % 2 == 0:

...   print("Found an even number", num)

...   continue

...  print("Found a number", num)

... 

Found an even number 2

Found a number 3

Found an even number 4

Found a number 5

Found an even number 6

Found a number 7

Found an even number 8

Found a number 9

*dari bagian diatas untuk menentukan bilangan ganjil genap*

.>>> while True:

...  pass

... 

^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt

.>>> while True:

...  pass

... 

^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt

.>>> class MyEmptyClass:

...  pass

... 

.>>> def initlog(*args):

...  pass

... 

*pass digunakan untuk sebuah sintak tidak perlu di jalankan*


.>>> def fib(n):

...  """Print a Fibonacci series up to n."""

...  a, b = 0, 1

...  while a < n:

...   print(a, end=' ')

...   a, b = b, a+b

...  print()

... 

.>>> fib(2000)

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 

*menampilkan bilangan fibonasi dengan batas tertentu*

.>>> fib

<function fib at 0x7f7c6a8c6f28>

.>>> f = fib

.>>> f(100)

0 1 1 2 3 5 8 13 21 34 55 89 

*menginisialkan sebuah variabel*

.>>> fib(0)

.>>> print(fib(0))

None

.>>> def fib2(n):

...  """Return a list containing the Fibonacci series up to n."""

...  result = []

...  a, b = 0, 1

...  while a < n:

...   result.append(a)

...   a, b = b, a+b

...  return result

... 

.>>> f100 = fib2(100)

.>>> f100

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


*returnpernyataan kembali dengan nilai dari fungsi. result.append(a)memanggil metode objek daftar result*


.>>> def ask_ok(prompt, retries=4, reminder='Please try again!'):

...  while True:

...   ok = input(prompt)

...   if ok in ('y', 'ye', 'yes'):

...    return True

...   if ok in ('n', 'no', 'nop', 'nope'):

...    return False

...   retries = retries - 1

...   if retries < 0:

...    raise ValueError('invalid user response')

...   print(reminder)

... 

.>>> ask_ok('Do you really want to quit?')

Do you really want to quit?y
True

.>>> ask_ok('OK to overwrite the file?', 2)

OK to overwrite the file?n
False

.>>> ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

OK to overwrite the file?

Come on, only yes or no!

OK to overwrite the file?b

Come on, only yes or no!

OK to overwrite the file?n

False

*dari bagian diatas untuk membuat beberapa nilai default argumen*

.>>> i = 5

.>>> 

.>>> def f(arg=i):

...  print(arg)

... i = 6

  File "<stdin>", line 3

    i = 6

    ^
SyntaxError: invalid syntax

.>>> i = 5

.>>> 

.>>> def f(arg=i):

...  print(arg)

... 

.>>> i = 6

.>>> f()

5

.>>> def f(a, L=[]):

...  L.append(a)

...  return L

... 

.>>> print(f(1))

[1]

.>>> print(f(2))

[1, 2]

.>>> print(f(3))

[1, 2, 3]

*dari bagian diatasmembuat definisi di dalam ruang lingkup dari varabel yang di beri nilai di awal*


.>>> concat("earth", "mars", "venus")

'earth/mars/venus'

.>>> concat("earth", "mars", "venus", sep=".")

'earth.mars.venus'

*dari bagian merupakan pembuatan beberapa pilihan tertentu* 

.>>> list(range(3, 6))

[3, 4, 5]

.>>> args = [3, 6]

.>>> list(range(*args))

[3, 4, 5]

*dari bagian diatas merupakan beberapa cara untuk mengetahui batas range dalam suatu bilangan*


.>>> def make_incrementor(n):

...  return lambda x: x + n

... 

.>>> f = make_incrementor(42)

.>>> f(0)

42

.>>> f(1)

43

.>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

.>>> pairs.sort(key=lambda pair: pair[1])

.>>> pairs

[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

*dari bagian diatas merupakan penggunaan lambda. Fungsi ini digunakan untuk mengembalikan jumlah dari dua argumen*

.>>> def my_function():

...  """Do nothing, but document it.

...  

...  No, really, it doesn't do anything.

...  """

...  pass

... 

.>>> print(my_function.__doc__)

Do nothing, but document it.
 
 No, really, it doesn't do anything.

*dari bagian diatas merupakan suatu literasi untuk membuat rangkaian kata-kata dengan suatu tatanan penulisan*
 
.>>> def f(ham: str, eggs: str = 'eggs') -> str:

...  print("Annotations:", f.__annotations__)

...  print("Arguments:", ham, eggs)

...  return ham + ' and ' + eggs

... 

.>>> f('spam')

Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments: spam eggs
'spam and eggs'

*dari bagian diatas Anotasi fungsi informasi metadata opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna*