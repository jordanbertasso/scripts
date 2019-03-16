import itertools

def cProduct(lang1, lang2):
	tuples = []

	strings = []

	# Populates tuples with all possible combos as tuples
	for element in itertools.product(lang1,lang2):
		tuples.append(element)

	# Converts each tuple to a string in 'strings'
	for pair in tuples:
		strings.append(pair[0]+pair[1])

	# Removes duplicates as dicts can't have duplicate keys
	strings = list(dict.fromkeys(strings))

	return strings

def union(lang1, lang2):
	result = []

	for a in lang1:
		if a in lang2:
			result.append(a)

	for b in lang2:
		if b in lang1:
			result.append(b)

	# Removes duplicates as dicts can't have duplicate keys
	result = list(dict.fromkeys(result))

	return result
