class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:

		result1 = []

		for i in s:
			if i != '#':
				result1.append(i)
			else:
				if result1:
					result1.pop()

		result2 = []

		for i in t:
			if i != '#':
				result2.append(i)
			else:
				if result2:
					result2.pop()

		if result1 == result2:
			return True
		else:
			return False