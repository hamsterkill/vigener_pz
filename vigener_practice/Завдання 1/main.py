from db import ab_rus
from vigener import *

if __name__ == "__main__":	
	text = ""
	with open("bulgakov.txt") as f:
		text = f.read()

	f_text = filter_text(text, "normal", ab_rus) 
	fs_text = filter_text(text, "with_space", ab_rus)

	cf_count, cf_stats = get_char_stats(f_text) #частоти символів без пробілу
	cs_count, cs_stats = get_char_stats(fs_text) #частоти символів із урахуванням пробілу
	bf_count_cross, bf_stats_cross = get_bigram_stats(f_text, "crossing") #частоти біграм без пробілів, біграми з перетином
	bs_count_cross, bs_stats_cross = get_bigram_stats(fs_text, "crossing") #частоти біграм із урахуванням пробілу, біграми з перетином
	bf_count_def, bf_stats_def = get_bigram_stats(f_text, "default") # частоти біграм без пробілів, біграми без перетину.
	bs_count_def, bs_stats_def = get_bigram_stats(fs_text, "default") #частоти біграм із урахуванням пробілу, біграми без перетину;

	f_index = index_of_considence(f_text, cf_count) #індекс відповідності для форматованого тексту без пробілів
	s_index = index_of_considence(fs_text, cs_count) #ндекс відповідності для форматованого тексту з пробілами

	print('Таблиця частот символів без пробілу:')
	for key in cf_stats.keys():
		print(key + ": " + str(cf_stats[key]))

	print('Таблиця частот символів з пробілом:')
	for key in cs_stats.keys():
		print(key + ": " + str(cs_stats[key]))

	print('Таблиця частот біграм без пробілів, біграми з перетином:')
	for key in bf_stats_cross.keys():
		print(key + ": " + str(bf_stats_cross[key]))

	print('Таблиця частот біграм без пробілів, біграми без перетину:')
	for key in bf_stats_def.keys():
		print(key + ": " + str(bf_stats_def[key]))

	print('Таблиця частот біграм з пробілами, біграми з перетином:')
	for key in bs_stats_cross.keys():
		print(key + ": " + str(bs_stats_cross[key]))

	print('Таблиця частот біграм з пробілами, біграми без перетину:')
	for key in bs_stats_def.keys():
		print(key + ": " + str(bs_stats_def[key]))

	print('Індекс відповідності для форматованого тексту без пробілів: ' + str(f_index))
	print('Індекс відповідності для форматованого тексту з пробілами: ' + str(s_index))

	input()