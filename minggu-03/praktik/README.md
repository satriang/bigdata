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

*menampilkan list yang berada disebelah kiri yang terdapat pada variabel*