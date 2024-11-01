def length(a):
	length = len(a)
	return length


def length_characters (a):
	if len(a) < 2:
		return " "
	else:
		return a[:2] + a[ -2:]

def add_ing (a):
	if len(a) < 3:
		return a
	elif  a[-3:] == 'ing':
		return a + 'ily'
	else:
		return a + 'ing'

def longest_word (a ):
	longest = ' '
	length = 0
	for i in a:
		if len(i) > len(longest):
			longest = i
			length = len(i)
			
	return longest, length

def odd_index(word):
	new_word = ""
	for i in range(len(word)):
		if i % 2 != 0:
			new_word += word[i]

	return new_word

def min_Number(numbers):
	minimum_Number = numbers[0]
	for i in numbers:
		if i < minimum_Number:
			minimum_Number = i

	return minimum_Number 

def max_Number(numbers):
	maximum_Number = numbers[0]
	for i in numbers:
		if i > maximum_Number:
			maximum_Number = i

	return maximum_Number


			

