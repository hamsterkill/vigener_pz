from db import ab_rus
from vigener import *
import matplotlib as mpt
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #використані ключі
    keys = ['на', 'кот', 'день', 'трава', 'космос', 'антагонист', 'авиапутешествие', 'высокопреосвященство']

    #отримання відформатованого відкритого тексту
    open_text = ''
    with open('perspekt.txt', 'r') as f:
        open_text = f.read()
        open_text = filter_text(open_text, 'normal', ab_rus)
        
    #шифрування тексту ключами до папки enc/<ключ>.txt
    for k in keys:
        with open('enc/' + k + '.txt', 'w') as f:
            enc_text = encrypt(open_text, k, ab_rus)
            f.write(enc_text)

    #отримання даних та вивід індексу відповідності відкритого тексту
    open_count, open_stats = get_char_stats(open_text)
    print('Індекс відповідності для оригінального тексту: ' + str(index_of_considence(open_text, open_count)))
    
    #отримання даних та вивід індексу відповідності зашифрованих текстів
    print('Індекси відповідностей для зашифрованих текстів: ')
    for k in keys:
        with open('enc/' + k + '.txt', 'r') as f:  
            enc_text = f.read()
            enc_count, enc_stats = get_char_stats(enc_text)
            index = index_of_considence(enc_text, enc_count)
            print("Для ключа '" + k + "': " + str(index))

    #-----------------------Завдання 3----------------------#

    #отримання зашифрованого тексту з файлу та його даних
    enc_text = ''
    with open('encrypted.txt', encoding='utf-8') as f:
        enc_text = f.read()
    enc_text = filter_text(enc_text, 'normal', ab_rus)
    enc_count, enc_stats = get_char_stats(enc_text)

    #вивід значення D для значень r від 2 до 40
    print("D: <значення>")
    for r in range(2,40):
       print(str(r) + ": " + str(get_repeats(enc_text, r)))

    #отримання блоків тексту для знайденої довжини ключа
    blocks = get_blocks(enc_text, 12)

    #отримання ключа шляхом співставлення найчастіших літер
    key = ''
    for block in blocks:
        b_count, b_stats = get_char_stats(block)
        o = max(b_count, key = b_count.get)
        k_o = (ab_rus.index(o) - ab_rus.index("о")) % 26
        key += ab_rus[k_o]
    print(key)

    #вивід розшифрованого тексту розбитого на блоки по 12 символів для аналізу тексту та отримання вихідного ключа
    t1 = decrypt(enc_text, key, ab_rus)
    t1_arr = [t1[i:i+12] for i in range(0, len(t1), 12)]
    for t in t1_arr:
        print(t)

    #вивід розшифрованого тексту
    t_decrypted = decrypt(enc_text, "вшекспирбуря", ab_rus)
    print(t_decrypted)

    input()

#-------------- Невдала спроба реалізації функції M(g) :) ------------------

    """
    for block in blocks:
        b_count, b_stats = get_char_stats(block)
        g_s = {}
        for g in range(0, 26):
            s = 0
            for b in block:
                b_i = ab_rus.index(b)
                try:
                    s += open_stats[b] * b_count[ab_rus[(b_i + g) % 26]]
                except KeyError:
                    continue

            g_s[ab_rus[g]] = s
            print(ab_rus[g] + ": " + str(s))

        key += max(g_s, key = g_s.get)

    print(key)
    """