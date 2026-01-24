##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace('\n', ' ')
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = 0

for symbol in adwentures_of_tom_sawer:
    if symbol == "h":
        count_h = count_h + 1

print(f"count_h = {count_h}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?"""

words_list = adwentures_of_tom_sawer.split()
count_capital = 0

for word in words_list:
    if word.istitle():
        count_capital = count_capital + 1

print(f"count_capital = {count_capital}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom_index = adwentures_of_tom_sawer.find("Tom")
second_tom_index = adwentures_of_tom_sawer.find("Tom", first_tom_index + 1)

print(f"second_tom_index = {second_tom_index}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
print(fourth_sentence.lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

is_by_the_time_start = False

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        is_by_the_time_start = True

if is_by_the_time_start:
    print("Sentence starts with 'By the time'")
else:
    print("No sentence starts with 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence_words = last_sentence.split()
print(len(last_sentence_words))