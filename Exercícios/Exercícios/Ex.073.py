times = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia',
         'Botafogo', 'Bragantino', 'Corinthians', 'Criciúma',
         'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',
         'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'São Paulo',
         'Vasco', 'Vitória')
print('TABELA BRASILEIRÃO')
print('=' * 30)
print('TOP 5 -')
for t in range(0, 5):
    print(f'{t + 1}º - {times[t]}')
print('=' * 30)
print('ZONA DE REBAIXAMENTO -')
for t in range(16, 20):
    print(f'{t + 1}º - {times[t]}')
print('=' * 30)
sorted(times)
print('TABELA EM ORDEM ALFABÉTICA -')
for t in range(0, len(times)):
    print(f'{t + 1}º - {times[t]}')
print('=' * 30)
print('POSIÇÃO DO CRICIÚMA NA TABELA -', end=' ')
print(f'{times.index("Criciúma") + 1}º')
