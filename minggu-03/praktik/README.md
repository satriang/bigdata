# Minggu ke-3

## Bab 5.1

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print fruits.count('apple')

2

print fruits.count('tangerine')

0

*menghitung banyaknya kata apple yang terdapat pada variabel fruit*

print fruits.index('banana', 4)

6

*mencari kata banana dalam variabel fruits dimulai dari index ke 4*

fruits.reverse()

print fruits


['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

*Mengurutkan dari yang paling terakhir ke yang pertama*

fruits.append('grape')

print fruits

['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

*menambahkan data baru di akhir barisan*

fruits.sort()

print fruits

['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

*mengelompokkan kata menurut abjad*

print fruits.pop()

pear

*menampilkan kata di akhir baris*

## Bab 5.1.2

stack = [3, 4, 5]

stack.append(6)

stack.append(7)

print stack

[3, 4, 5, 6, 7]

*menambahkan list baru pada baris terakhir*

stack.pop()

print stack

[3, 4, 5, 6]

*menghilangkan list terakhir pada barisan dalam variabel*

stack.pop()

stack.pop()

print stack

[3, 4]

*menghilangkan 2 list terakhir pada barisan dalam variabel*

## Bab 5.1.2

from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           

queue.append("Graham")          

print queue.popleft()           

Eric

queue.popleft()                

print queue  

deque(['Michael', 'Terry', 'Graham'])

*menghilangkan 2 list yang berada paling kiri dan menambahkan data baru di dalam variabel*


## Bab 5.1.3

squares = []

for x in range(10):

>    squares.append(x**2)

print squares

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

*menambahkan bilangan kuadrat pada variabel menggunakan perulangan for*
```bash
>>> combs = []
>>>
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> print combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
*pembuatan list menggunakan for*

```bash
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```
*script diatas menunjukkan jika list adalah tuple harus disisipkan (...)*

## Bab 5.1.4

```bash
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print matrix

[[row[i] for row in matrix] for i in range(4)]

[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```
*dari script diatas merupakan implementasi matrik 3x4*

```bash
print list(zip(*matrix))
```
*perintah diatas merupakan penggunaan dari fungsi zip*

## Bab 5.2

```bash
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a

del a[2:4]
print a

del a[:]
print a

[1, 66.25, 333, 333, 1234.5]
[1, 66.25, 1234.5]
[]
```
*perintah diatas ialah penggunaan del statement untuk menghapus suatu list*

## Bab 5.3

```bash
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> print t
(12345, 54321, 'hello!')
>>> u = t, (1, 2, 3, 4, 5)
>>> print u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> v = ([1, 2, 3], [3, 2, 1])
>>> print v
([1, 2, 3], [3, 2, 1])
```
*dari script diatas tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma. kadang bisa bersifat nested. pada sintak eror disebabkan karena tuples immutable. tuple bisa untuk objek yang selalu berubah*

## Bab 5.4

*python juga terdapat tipe data set. cara penggunaan fungsi set dengan cara set(...). contoh*
```bash
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)
set(['orange', 'pear', 'apple', 'banana'])
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                             
set(['r', 'b', 'd'])
>>> a | b                             
set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])
>>> a & b                              
set(['a', 'c'])
>>> a ^ b
set(['b', 'd', 'm', 'l', 'r', 'z'])
```
*contoh diatas merupakan cara penggunaan tipe data set*
```bash
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
set(['r', 'd'])
```
*tipe data set juga dapat digabungkan dengan penggunakan for dan if*

## Bab 5.5

*tipe data yang lain pada python yaitu dictionary Operasi utama pada kamus menyimpan nilai dengan beberapa kunci dan mengekstraksi nilai yang diberikan kunci. Anda juga dapat menghapus kunci: pasangan nilai dengan del. contoh berikut*
```bash
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'irv': 4127, 'guido': 4127}
>>> list(tel)
['jack', 'irv', 'guido']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
*dari contoh diatas dapat menggunakan fungsi dict seperti contoh dibawah ini*
```bash
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```
*untuk membuat dictionaries kita dapat menggunakan dict comprehensions. Contoh*
```bash
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
*Ketika kunci adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci. Contoh*
```bash
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

## Bab 5.6

*looping dengan dictionary. Contoh*
```bash
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>>
>>> for k, v in knights.items():
...     print(k, v)
...
('gallahad', 'the pure')
('robin', 'the brave'
```
*Ketika mengulang melalui urutan, indeks posisi dan nilai yang terkait dapat diambil pada saat yang sama menggunakan fungsi enumerate(). Contoh*
```bash
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
(0, 'tic')
(1, 'tac')
(2, 'toe')
```
*Untuk mengulang lebih dari dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi zip().Contoh*
```bash
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>>
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
*Untuk mengulang suatu urutan secara terbalik, gunakan fungsi reserved(). Contoh*
```bash
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```
*Untuk mengulang urutan dalam urutan yang diurutkan, gunakan sorted(). Contoh*
```bash
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>>
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```
*untuk menyederhanakan dan mengamankan list, lebih baik kta membuat daftar list. Contoh*
```bash
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>>
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

## Bab 5.7

*perbandingan boolean ke dalam suatu variabel lain. Contoh*
```bash
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

## Bab 5.8

*Objek urutan dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan ini menggunakan urutan leksikografis : pertama dua item pertama dibandingkan, dan jika mereka berbeda, ini menentukan hasil perbandingan; jika keduanya sama, dua item berikutnya akan dibandingkan, dan seterusnya, hingga urutannya habis.*