import string

letters = list(string.ascii_lowercase)
letters_count = [0] * len(string.ascii_lowercase)
letters_probability = [0] * len(string.ascii_lowercase)
total_letters_count = 0

known_words = ['hallo', 'klempner','das','ist','fantastisch','fluggegecheimen']
print('Введите стоп-слово')
stop_word = input()

for i in range(0, len(known_words)):
    total_letters_count += len(known_words[i])
    for j in range(0, len(known_words[i])):
        for k in range(0, len(letters)):
            if letters[k] == known_words[i][j]:
                letters_count[k] += 1
                break

for i in range(0, len(letters)):
    letters_probability[i] = letters_count[i] / total_letters_count

chance = 1
for i in range(0, len(stop_word)):
    for j in range(0, len(letters)):
        if stop_word[i] == letters[j]:
            chance *= letters_probability[j]
            
print('Вероятность:', chance)