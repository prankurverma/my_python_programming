class HashMap:
	def __init__(self):
		self.size = 6
		self.map = [None] + self.size()
	def _get_hash (self, key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size
	def add (self, key, value):
		key_hash = self._get_hash(key)
		key_value = [key, value]
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True
	def get(self, key):
		key_hash + self._get_hash[key]
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None
	def delete(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is None:
			return False
		for i in range (0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True
	def print(self):
		print('Hashmap')
		for item in self.map:
			if item is not None:
				print (str(item))

h = HashMap()
h.add('Bob', '1234567890')
h.add('Ming', '7418529630')
h.add('David', '7896543210')
h.add('Shefali', '9638527410')
h.add('Rajat', '1594872630')
h.add('Hrithik', '1472583690')
h.add('Robin', '6549873219')
h.print()
h.delete('Bob')
h.print()
print('Ming:' + h.get('Ming'))
