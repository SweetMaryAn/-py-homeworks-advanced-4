nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(ListGenerators):
	for ListGenerator in ListGenerators:
		for el in ListGenerator:
			yield el

for item in flat_generator(nested_list):
	print(item)