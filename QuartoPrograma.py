nomeVariavel = 43
print(nomeVariavel)

# Verificar o tipo de variável
print(type(nomeVariavel))

# Convertendo para float
nomeVariavel = float(nomeVariavel)
print(type(nomeVariavel))

# Soma com um número
resultado = nomeVariavel + 57
print(resultado)  # Resultado: 100.0

# Tentativa de somar string com float (vai dar erro)
# resultado = nomeVariavel + "57"  # Isso causaria erro de tipo

# Convertendo o número para string
nomeVariavel = str(nomeVariavel)
print(nomeVariavel)  # Resultado: '43.0'
print(type(nomeVariavel))  # Tipo: <class 'str'>

# Agora podemos concatenar
resultado = nomeVariavel + "57"
print(resultado)  # Resultado: '43.057'
