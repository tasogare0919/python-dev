# coding:utf-8
x = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'
result = []
xwords = x.split(' ')

for xword in xwords:
         result.append(len(xword) - xword.count(',') - xword.count('.'))
         
print(result)
