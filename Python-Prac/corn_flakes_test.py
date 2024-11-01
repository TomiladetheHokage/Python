from corn_flakes import length
from corn_flakes import length_characters
from corn_flakes import add_ing
from corn_flakes import longest_word
from corn_flakes import odd_index
from corn_flakes import min_Number
from corn_flakes import max_Number

def test_length():
	assert length('semicolon') == 9

def test_length_characters():
	assert length_characters ('semicolon') == 'seon'
	assert length_characters ('on') == 'onon'
	assert length_characters ('o') == " "

def test_add_ing():
	assert add_ing('on') == 'on'
	assert add_ing('abc') == 'abcing'
	assert add_ing('String') == 'Stringily'

def test_longest_word():
	words = ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']
	longest, length = longest_word(words)
	assert longest == 'breakfast' and length == 9

def test_odd_index():
	word = "semicolon"
	assert odd_index(word) == 'eioo'

def test_min_number():
	numbers = [1,2,2,4,6,7,8,9,0]
	min_Number = max_Number(numbers)
	assert min_number(numbers) == 0

def test_max_number():
	numbers = [1,2,2,4,6,7,8,9,0]
	max_Number = max_Number(numbers)
	assert max_number == 9


	

	
