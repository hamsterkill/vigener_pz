def filter_text(text: str, mode: str, ab: str):
	"""
	Фільтрує текст відповідно до заданого значення mode:
	'normal' - текст без пробілів
	'with_space' - текст з пробілами
	"""
	filtered_text = ""
	if mode == "normal":
		for char in text:
			if char.lower() in ab:
				filtered_text += char.lower()
			elif char.isupper() and char.lower() in ab:
				filtered_text += char.lower()
	elif mode == "with_space":
		for char in text:
			if char.lower() in ab:
				filtered_text += char.lower()
			elif char.isspace():
				filtered_text += " "
		filtered_text = "_".join(filtered_text.split()) # видаляємо зайві пробіли
	return filtered_text

def get_char_stats(text: str):
	"""
	Функція отрмання частот для символів
	"""
	s = 0
	d = {}
	
	for c in text:
		s+=1
		if c in d.keys():
			d[c] += 1
		else:
			d[c] = 1

	stats = {}

	for k in d:
		stats[k] = round(d[k] / s * 100, 3) 

	d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
	stats = dict(sorted(stats.items(), key=lambda x:x[1], reverse=True))

	return d, stats

def get_bigram_stats(text: str, mode: str):
	"""
	Функція отрмання частот для біграм відповідно до значення mode:
	'crossing' - з перетином
	'default' - без перетину
	"""
	s = 0
	d = {}

	if mode == "crossing":
		for i in range(0, len(text)-1):
			s+=1
			if text[i]+text[i+1] in d.keys():
				d[text[i]+text[i+1]] += 1
			else:
				d[text[i]+text[i+1]] = 1
	elif mode == "default":
		for i in range(0, len(text)-1, 2):
			s+=1
			if text[i]+text[i+1] in d.keys():
				d[text[i]+text[i+1]] += 1
			else:
				d[text[i]+text[i+1]] = 1

	stats = {}

	for k in d:
		stats[k] = d[k] / s * 100

	d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
	stats = dict(sorted(stats.items(), key=lambda x:x[1], reverse=True))

	return d, stats

def index_of_considence(text: str, char_count:dict):
	"""
	Функція обрахування індексу відповідності
	"""
	n = len(text)
	s = 0
	for key in char_count.keys():
		s += (char_count[key]*(char_count[key]-1))

	return s  / (n*(n-1))