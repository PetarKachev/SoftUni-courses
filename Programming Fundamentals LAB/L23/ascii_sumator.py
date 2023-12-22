first_symbol = input()
second_symbol = input()
string = input()
first_symbol = ord(first_symbol)
second_symbol = ord(second_symbol)
info_list = []
for symbol in string:
    if first_symbol < ord(symbol) < second_symbol:
        info_list.append(ord(symbol))
print(sum(info_list))