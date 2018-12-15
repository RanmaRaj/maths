import sys

if len(sys.argv) != 2:
	print("Usage: python numbers_in_words.py <number>")
	sys.exit(1)

argument = sys.argv[1]

UNIT = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", 'thirteen', "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

THOUSANDS = ["", "thousand", "million", "billion", "trillion", "quadrillion"]

def get_digit(num, n):
	return num // 10**n % 10

def get_length(num):
	return len(str(abs(num)))

def convert_less_than_thousand(num):
	l = get_length(num)
	#print(1000**(l//3))
	exponent = (l-1)//3
	temp_num = num // (1000**(exponent))
	#print(temp_num)
	#print(temp_num//100)
	num_string = ""	
	if temp_num < 20:
		num_string = UNIT[temp_num]
	elif temp_num < 100:
		num_string = TENS[get_digit(temp_num,1)] + " " + UNIT[get_digit(temp_num,0)]
	else:
		num_string = UNIT[get_digit(temp_num,2)] + " hundred " + TENS[get_digit(temp_num,1)] + " " + UNIT[get_digit(temp_num,0)]

	new_num = num - (temp_num * (1000**exponent))
	return num_string + " " +  THOUSANDS[exponent], new_num
	
def number_to_words(num):
	words = ""
	while num >= 1000:
		ans, num = convert_less_than_thousand(num)
		words += ans + ""
		if num != 0:
			words += ', '
	if num != 0:
		ans, num = convert_less_than_thousand(num)
		words += ans
	return words.capitalize()	

print(number_to_words(int(argument)))
			

