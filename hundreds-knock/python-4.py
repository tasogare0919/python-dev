# coding:utf-8
output_num = (0, 4, 5, 6, 7, 8, 14, 15, 18)
words = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
result = {} 
wordssplits = words.split(' ')

i = 0

for (num, wordssplit) in enumerate(wordssplits, i):
    if num in output_num:
        result[wordssplit[0:1]] = num
    else:
        result[wordssplit[0:2]] = num

print(result)
