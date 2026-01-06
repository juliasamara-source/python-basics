hello.py
nome = input("Qual é o seu nome? ")
cidade = input("De onde você é? ")
idade = input("Quantos anos você tem? ")

print("Oi", nome)
print("Você é de", cidade)
print("Você tem", idade, "anos")
 
print("-----")

# Parte com decisão
idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print("Você é maior de idade 🙂")
else:
    print("Você é menor de idade 🙃")


 
