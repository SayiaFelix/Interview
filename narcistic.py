def is_narcissistic_num(num):
	return num == sum([int(x) ** len(str(num)) for x in str(num)])

print(is_narcissistic_num(153))
print(is_narcissistic_num(201))
print(is_narcissistic_num(259))
print(is_narcissistic_num(371))
print(is_narcissistic_num(407))
print(is_narcissistic_num(595))
print(is_narcissistic_num(825))
print(is_narcissistic_num(1634))