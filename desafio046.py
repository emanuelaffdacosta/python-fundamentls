import emoji
from time import sleep
print('-*' * 16)
print(emoji.emojize(':sparkles: VAMOS A CONTAGEM REGRESSIVA :sparkles:', use_aliases=True))
print('-*' * 16)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':tada: {} FELIZ ANO NOOVO {} :tada:'.format('\033[1;30m', '\033[m'), use_aliases=True))
