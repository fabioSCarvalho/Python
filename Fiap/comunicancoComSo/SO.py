import platform

import platform

print("Distribuição do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versão do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())

print('-='*10)


import getpass
from datetime import datetime

print("Usuário.......: ", getpass.getuser())
print("Data Completa.: ", datetime.now())
print("Dia...........: ", datetime.now().day)
print("Mês...........: ", datetime.now().month)
print("Ano...........: ", datetime.now().year)
print("Hora..........: ", datetime.now().hour)
print("Minuto........: ", datetime.now().minute)
print("Segundo.......: ", datetime.now().second)

print('-='*10)

import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login Negado")