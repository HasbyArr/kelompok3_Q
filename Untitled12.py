#!/usr/bin/env python
# coding: utf-8

# In[14]:


from browser import document, console, alert

input = document['input']
button = document['btn']
output = document['output']
select = document['select']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Masukkan angka terlebih dahulu')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(x, y):
    match x:
        case 'keliling lingkaran':
            return 2 * 3.14 * y 
        case 'luas lingkaran':
            return 3.14 * y * y
        case _:        
            return 0

# def f(x):
#     return {
#         'keliling lingkara': 1,
#         'luas lingkaran': 2,
#     }[x]

def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output.textContent = str(result)

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)
input.bind("keypress", keyEnter)

