#fatiamento
frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise
print(len(frase)) #length - mostra quantos caracteres tem a frase
print(frase.count('o'))
print(frase.count('o', 0, 13)) #contagem com fatiamento
print(frase.find('deo')) #mostra em que momento começou a posição
print(frase.find('Android'))
print('Curso' in frase)

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #função parecida com o title, porém. deixa apenas o começo maiúsculo
print(frase.title())
frase2 = 'Aprenda Python'
print(frase2.strip()) #remove todos os espaços inúteis
print(frase2.rstrip()) #r de right (direito)
print(frase2.lstrip()) #l de left (esquerda)

#Divisão
print(frase.split())

#Junção
print('-'.join(frase))