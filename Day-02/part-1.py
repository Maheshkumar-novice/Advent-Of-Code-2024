with open('input.txt', 'r') as f:
	reports = [map(int, line.split()) for line in f.readlines()]

	def is_safe(report):
		desc = False
		asc = False
		prev = None
		for level in report:
			if not prev:
				prev = level
				continue

			if prev < level:
				asc = True
				if abs(prev - level) > 3:
					return False

			if prev > level:
				desc = True
				if abs(prev - level) > 3:
					return False

			if prev == level:
				return False
			
			if asc and desc:
				return False
		
			prev = level
		return True

	print(sum(is_safe(report) for report in reports))
