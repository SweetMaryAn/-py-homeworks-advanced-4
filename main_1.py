nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
class FlatIterator:
	def __init__(self, ListIterator):
		self.ListIterator = ListIterator

	def __iter__(self):
		self.cursor_1 = 0
		self.cursor_2 = -1
		return self

	def __next__(self):
		self.cursor_2 += 1
		if self.cursor_2 == len(self.ListIterator[self.cursor_1]):
			self.cursor_2 = 0
			self.cursor_1 += 1
		if self.cursor_1 == len(self.ListIterator):
			raise StopIteration
		return self.ListIterator[self.cursor_1][self.cursor_2]


for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)