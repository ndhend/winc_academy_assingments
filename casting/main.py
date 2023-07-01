# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
#part 1
leek_price = 2
print ('Leek is ' + str(leek_price) + ' euro per kilo.')
# part 2
four_leeks = 'leek 4'
order_index = four_leeks.find ('4')
order = four_leeks[5]
sum_total = leek_price * int(order)
print(sum_total)

# part 3
"""price_broccoli = 2.34
order_broccoli = 'broccoli 1.6'
total_price_broccoli = 2.34 * 1.6
total_price_broccoli = price_broccoli * order_broccoli (find spatie) alles vanaf die index is het getal
print (total_price_broccoli)
print('1.6kg broccoli costs ' + (str(total_price_broccoli)).replace ('9999999999998', 'e'))
s= 'hello'
print (s.replace ('h', 'j'))
print ((str(total_price_broccoli)).replace ('9999999999998', 'e'))
print('1.6kg broccoli costs ' + (str(total_price_broccoli)).replace ('9999999999998', 'e'))
print ('broccoli 1.6'.split())
print(order_broccoli.split ())"""

broccoli_price = 2.34 
broccoli_order = 'broccoli 1.6'      
broccoli_order_no = float(broccoli_order[broccoli_order.find(" ") + 1:])
total_price = round(broccoli_price * broccoli_order_no, 2)
print(total_price)
print(str(broccoli_order_no) + 'kg broccoli costs ' + str(total_price) + 'e')
print(float(broccoli_order[broccoli_order.find(" ") + 1:]))
