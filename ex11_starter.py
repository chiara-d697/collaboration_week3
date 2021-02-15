#!/usr/bin/python
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Part a
print(Belgium.replace(Belgium, '---------------------------------------------------------------------------------'))
# Part b
print(Belgium.replace(',',':'))
# Part c
value1 = int(Belgium[8:16])
value2 = int(Belgium[26:32])
sum = value1 + value2
print(sum)

