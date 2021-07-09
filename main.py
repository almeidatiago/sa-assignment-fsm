#!/usr/bin/env python
# coding: utf-8

# In[232]:


get_ipython().run_line_magic('matplotlib', 'inline')
import os
import sys
import string
import numpy as np
import matplotlib.pyplot as plt
#from sympy import *
#from qm import*
import math
#from random import shuffle
import random
import time
import csv

plt.rcParams['figure.figsize'] = (15,10)

import subprocess
import glob
import itertools


# In[233]:


##########################  
# Essa funcao é definitiva, ela das três formas é a mais eficiente, 
def novo_shuffle(numero_estados, tamanho_espaco_busca):
    espaco_busca = []
    for i in range (2**tamanho_espaco_busca):
        espaco_busca.append(bin(i)[2:].zfill(tamanho_espaco_busca))
    lista_remover = list(espaco_busca)
    nova_atrib = []
    for i in range(numero_estados):
        valor = random.choice(lista_remover)
        lista_remover.remove(valor)
        nova_atrib.append(valor)
    
    return nova_atrib


# In[234]:


def correspondente(palavra1, palavra2, tam_space):
    espaco_busca = []
    for i in range (2**tam_space):
        espaco_busca.append(bin(i)[2:].zfill(tam_space))
    espaco_aleatorio = palavra2
    #print(palavra1)
    #print(palavra2)
    for i in range(len(espaco_busca)):
        if palavra1 == espaco_busca[i]:
            return str(espaco_aleatorio[i])


# In[235]:


def simplifica_maquina(filename):
    teste = subprocess.run(['./espresso',filename],stdout=subprocess.PIPE,universal_newlines=True)
    saida = teste.stdout
    a = open(filename,'w')
    a.write(saida)
    a.close()


# In[236]:


def leitura(filename):
    nova = open(filename,'r')
    line_char = nova.readlines()
    custo_nova = int(line_char[2][3:])
    nova.close()
    return custo_nova


# In[237]:


def troca_maquina(newfilename, bestfilename):
    nova = open(newfilename,'r')
    melhor = open(bestfilename,'w')
    nova_lista = nova.readlines()
    for i in range(len(nova_lista)):
        melhor.write(str(nova_lista[i]))
    nova.close()
    melhor.close()


# In[238]:


def calculo_custo(filename, entrada_input, saida_output, numero_estados):
    transicoes_nova = leitura(filename)
    area = transicoes_nova*(2*entrada_input + 3*(np.log2(numero_estados)) + saida_output)
    return area


# In[239]:


def resfriamento_simulado(casefilename, temperatura, vizinhos):
    #####################################################################
    # Faz a leitura do arquivo KISS2 e prepara as variáveis globais
    l = []
    entrada = []
    lista_entradas = []
    saida = []
    lista_saidas = []

    estados = []

    atual = []
    atual_inteiro = []
    atual_convertido = []

    proximo = []
    proximo_inteiro = []
    proximo_convertido = []

    espaco_aleatorio = []

    comprimento_input = 0
    comprimento_output = 0
    line_char = []
    msf_pronta = []

    tamanho_espaco_busca = 0
    
    temp = open('msfs/' + casefilename +'.kiss2')

    line_char = temp.readlines()
    #print(line_char)

    estados = line_char[4:5]
    estados_convertido = int(estados[0].split()[1])

    #define o tamanho do espaço de busca basedado no valor entregue pelo arquivo

    tamanho_espaco_busca = math.ceil(np.log2(estados_convertido))

    entrada_input = int(line_char[1][3:])
    saida_output = int(line_char[2][3:])
    numero_estados = int(line_char[4][3:])

    #msf_pronta = []

    l = line_char[5:]
    #print(l)
    
    for i in range(len(l)):
        entrada = l[i].split()[0]
        lista_entradas.append(entrada)
    
        atual = l[i].split()[1]
        proximo = l[i].split()[2]
        saida = l[i].split()[3]
        lista_saidas.append(saida)
    
        atual_inteiro = int(''.join([i for i in atual if i.isdigit()]))
        #print(atual)
        proximo_inteiro = int(''.join([i for i in proximo if i.isdigit()]))

        atual_convertido.append(bin(atual_inteiro)[2:].zfill(tamanho_espaco_busca))
        #atual_binario = atual_convertido[i]
        proximo_convertido.append(bin(proximo_inteiro)[2:].zfill(tamanho_espaco_busca))
        #proximo_binario = proximo_convertido[i]
        linha = str(lista_entradas[i])+str(atual_convertido[i])+' '+str(proximo_convertido[i])+str(lista_saidas[i])
        msf_pronta.append(linha)
        #print(msf_pronta[i])
    
    #msf_pronta.append('.e')
    #print(atual_convertido)
    comprimento_input = str(len(lista_entradas[0])+len(atual_convertido[0]))
    comprimento_output = str(len(proximo_convertido[0])+len(lista_saidas[0]))
    #print(comprimento_input)

    d = open('melhor.pla','w')
    #d.write('\n')
    d.write('.i '+comprimento_input+'\n')
    d.write('.o '+comprimento_output+'\n')
    d.write(line_char[3])
    
    size = len(msf_pronta)

    for i in range(size):
        d.write(msf_pronta[i]+'\n')

    d.close()
    #######################################################################
    #reseta_msf('melhor.pla')
    temperatura_inicial = temperatura
    temperatura_final = 1

    simplifica_maquina('melhor.pla')
    custo_melhor = calculo_custo('melhor.pla', entrada_input, saida_output, numero_estados)
    custo_init = custo_melhor
    historico_temperatura = [temperatura]
    historico = [custo_melhor]
    while(temperatura > temperatura_final):
        for i in range(vizinhos):
            custo_melhor = calculo_custo('melhor.pla', entrada_input, saida_output, numero_estados)
            #################################################################################
            # Cria nova MSF
            novo_atual = []
            novo_proximo = []
            nova_msf = []
    
            espaco_aleatorio = list(novo_shuffle(numero_estados, tamanho_espaco_busca))
    
            for i in range(len(l)):
                novo_atual.append(correspondente(atual_convertido[i],espaco_aleatorio, tamanho_espaco_busca))
                novo_proximo.append(correspondente(proximo_convertido[i],espaco_aleatorio, tamanho_espaco_busca))
                nova_atrib = str(lista_entradas[i])+str(novo_atual[i])+' '+str(novo_proximo[i])+str(lista_saidas[i])
                nova_msf.append(nova_atrib)
            #print(nova_msf)
        
            d = open('nova.pla','w')
            d.write('.i ' + str(comprimento_input) + '\n')
            d.write('.o ' + str(comprimento_output) + '\n')
            d.write(line_char[3])

            for i in range(len(nova_msf)):
                d.write(nova_msf[i]+'\n')
            d.close()
            ##########################################################################
    
            #nova_maquina('nova.pla', qt_estados)
            simplifica_maquina('nova.pla')
            custo_nova = calculo_custo('nova.pla', entrada_input, saida_output, numero_estados)
            probabilidade = np.random.random_sample()

            if (custo_nova < custo_melhor):
                if (probabilidade < (1+np.exp(-(custo_melhor-custo_nova)/temperatura))**-1):
                    troca_maquina('nova.pla', 'melhor.pla')
                    custo_melhor = custo_nova
        
        if temperatura > temperatura_inicial/2:
            temperatura = temperatura - 1.2
        else:
            temperatura = temperatura - 0.8

        historico.append(custo_melhor)
        historico_temperatura.append(temperatura)
        
    return custo_init, custo_melhor, historico, historico_temperatura


# In[240]:


kissfiles = []
for file in glob.glob("msfs/*.kiss2"):
    name = file.split('/')
    name = name[1].split('.')
    kissfiles.append(name[0])
kissfiles.sort()
#kissfiles = ['bbtas']    
print(kissfiles)

with open('resultados.csv', mode='w') as csv_file:
    fieldnames = ['Caso', 'Custo Inicial', 'Custo Final', 'Percentual', 'Tempo (s)']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    markers = itertools.cycle(['o','v','^','<','>','s','p','*','h','+','x','d','1','2','3','4','8'])
    
    for name in kissfiles:
        temperatura = 100
        custo_init = 0
        custo_final = 0
        valores = []
        temperatura_iter = []
        
        #qt_entradas, qt_saida, qt_estados = get_ready_fsm(name, 'melhor.pla')
    
        tic = time.perf_counter()
        custo_init, custo_final, valores, temperatura_iter = resfriamento_simulado(name, temperatura, 100)
        toc = time.perf_counter()
        tempo = str(toc-tic)
        
        print("Melhor custo:",custo_final)
        print("Tempo de execucao:",toc-tic)
    
        writer.writerow({'Caso': name, 
                         'Custo Inicial': str(custo_init), 
                         'Custo Final': str(custo_final),
                         'Percentual': str(1 - (custo_final/custo_init)),
                         'Tempo (s)': tempo
                        })
        
        for i in range(len(valores)):
            valores[i] = valores[i] / custo_init
            temperatura_iter[i] = temperatura_iter[i] / temperatura
        
        #plt.cla()
        plt.title('Resultados Normalizados')
        plt.xlabel('Iterações')  # Add an x-label to the axes.
        plt.ylabel('Custo')
        plt.plot(valores, marker=next(markers), label=name)
        
        print(name + ': ok')
        
    plt.plot(temperatura_iter, '-*', label='Temperatura')    
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.figure(1)    
    plt.savefig('resultados.png')


# In[ ]:





# In[ ]:




