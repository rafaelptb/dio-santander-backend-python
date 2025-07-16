nome = 'Rafael'
idade = 46

# Forma não mais utilizada
print('%s tem %d anos.' %(nome, idade))

# Usando o método format
print('{} tem {} anos.' .format(nome, idade))

print('{1} tem {0} anos.' .format(idade, nome))

print('{name} tem {age} anos.' .format(name=nome, age=idade))

pessoa = {
    'nome': 'Rafael',
    'idade': 46
}

print('{nome} tem {idade} anos.' .format(**pessoa))

# Usando fstring (mais usado hoje em dia)

print(f"{nome} tem {idade} anos.")

PI = 3.14159
print(f'Valor de PI: {PI:.2f}' )
print(f'Valor de PI: {PI:10.2f}' )