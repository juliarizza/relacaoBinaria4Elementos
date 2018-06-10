# -*- coding: utf-8 -*-
import time

inicio = time.time()

# Por motivos de performance, as classificações evitam for loops

def simetrica(num):
    sim = True

    # Para ser simétrica (x,y) e (y,x) devem existir simultâneamente

    # Não é simétrica se (1,2) ou (2,1) existem, mas não simultâneamente
    if ((num&2) or (num&16)) and not ((num&2) and (num&16)):
        sim = False
    # Não é simétrica se (1,3) ou (3,1) existem, mas não simultâneamente
    if ((num&4) or (num&256)) and not ((num&4) and (num&256)):
        sim = False
    # Não é simétrica se (1,4) ou (4,1) existem, mas não simultâneamente
    if ((num&8) or (num&4096)) and not ((num&8) and (num&4096)):
        sim = False
    # Não é simétrica se (2,3) ou (3,2) existem, mas não simultâneamente
    if ((num&64) or (num&512)) and not ((num&64) and (num&512)):
        sim = False
    # Não é simétrica se (2,4) ou (4,2) existem, mas não simultâneamente
    if ((num&128) or (num&8192)) and not ((num&128) and (num&8192)):
        sim = False
    # Não é simétrica se (3,4) ou (4,3) existem, mas não simultâneamente
    if ((num&2048) or (num&16384)) and not ((num&2048) and (num&16384)):
        sim = False

    return sim

def transitiva(num):
    trans = True

    # Para ser transitiva, se (x,y) e (y,z) existem
    # então (x,z) deve existir

    ##### Relação 1->2 e 2->x
    # Não é transitiva se existem (1,2) e (2,3), mas não (1,3)
    if (num&2) and (num&64) and not (num&4):
        trans = False
    # Não é transitiva se existem (1,2) e (2,4), mas não (1,4)
    if (num&2) and (num&128) and not (num&8):
        trans = False

    #### Relação 1->3 e 3->x
    # Não é transitiva se existem (1,3) e (3,2), mas não (1,2)
    if (num&4) and (num&512) and not (num&2):
        trans = False
    # Não é transitiva se existem (1,3) e (3,4), mas não (1,4)
    if (num&4) and (num&1024) and not (num&8):
        trans = False

    #### Relação 1->4 e 4->x
    # Não é transitiva se existem (1,4) e (4,2), mas não (1,2)
    if (num&8) and (num&8192) and not (num&2):
        trans = False
    # Não é transitiva se existem (1,4) e (4,3), mas não (1,3)
    if (num&8) and (num&16384) and not (num&4):
        trans = False

    #### Relação 2->1 e 1->x
    # Não é transitiva se existem (2,1) e (1,3), mas não (2,3)
    if (num&16) and (num&4) and not (num&64):
        trans = False
    # Não é transitiva se existem (2,1) e (1,4), mas não (2,4)
    if (num&16) and (num&8) and not (num&128):
        trans = False

    #### Relação 2->3 e 3->x
    # Não é transitiva se existem (2,3) e (3,1), mas não (2,1)
    if (num&64) and (num&256) and not (num&16):
        trans = False
    # Não é transitiva se existem (2,3) e (3,4), mas não (2,4)
    if (num&64) and (num&2048) and not (num&128):
        trans = False

    #### Relação 2->4 e 4->x
    # Não é transitiva se existem (2,4) e (4,1), mas não (2,1)
    if (num&128) and (num&4096) and not (num&16):
        trans = False
    # Não é transitiva se existem (2,4) e (4,3), mas não (2,3)
    if (num&128) and (num&16384) and not (num&64):
        trans = False

    #### Relação 3->1 e 1->x
    # Não é transitiva se existem (3,1) e (1,2), mas não (3,2)
    if (num&256) and (num&2) and not (num&512):
        trans = False
    # Não é transitiva se existem (3,1) e (1,4), mas não (3,4)
    if (num&256) and (num&8) and not (num&2048):
        trans = False

    #### Relação 3->2 e 2->x
    # Não é transitiva se existem (3,2) e (2,1), mas não (3,1)
    if (num&512) and (num&16) and not (num&256):
        trans = False
    # Não é transitiva se existem (3,2) e (2,4), mas não (3,4)
    if (num&512) and (num&128) and not (num&2048):
        trans = False

    #### Relação 3->4 e 4->x
    # Não é transitiva se existem (3,4) e (4,1), mas não (3,1)
    if (num&2048) and (num&4096) and not (num&256):
        trans = False
    # Não é transitiva se existem (3,4) e (4,2), mas não (3,2)
    if (num&2048) and (num&8192) and not (num&512):
        trans = False

    #### Relação 4->1 e 1->x
    # Não é transitiva se existem (4,1) e (1,2), mas não (4,2)
    if (num&4096) and (num&2) and not (num&8192):
        trans = False
    # Não é transitiva se existem (4,1) e (1,3), mas não (4,3)
    if (num&4096) and (num&4) and not (num&16384):
        trans = False

    #### Relação 4->2 e 2->x
    # Não é transitiva se existem (4,2) e (2,1), mas não (4,1)
    if (num&8192) and (num&16) and not (num&4096):
        trans = False
    # Não é transitiva se existem (4,2) e (2,3), mas não (4,3)
    if (num&8192) and (num&64) and not (num&16384):
        trans = False

    #### Relação 4->3 e 3->x
    # Não é transitiva se existem (4,3) e (3,1), mas não (4,1)
    if (num&16384) and (num&256) and not (num&4096):
        trans = False
    # Não é transitiva se existem (4,3) e (3,2), mas não (4,2)
    if (num&16384) and (num&512) and not (num&8192):
        trans = False

    return trans

def reflexiva(num):
    # É reflexiva apenas se existem (1,1) e (2,2) e (3,3) e (4,4)
    return (num&1) and (num&32) and (num&1024) and (num&32768)

def equivalencia(num):
    # É equivalente se for simétrica e transitiva e reflexiva
    return simetrica(num) and transitiva(num) and reflexiva(num)

def irreflexiva(num):
    # É irreflexiva se não for reflexiva
    return not reflexiva

def funcao(num):
    func = True

    # Não é função se 1 se relaciona com mais de um elemento
    # ou seja, é falso (1,1) XOR (1,2) XOR (1,3) XOR (1,4)
    if not (num&1) ^ (num&2) ^ (num&4) ^ (num&8):
        func = False
    # Não é função se 2 se relaciona com mais de um elemento
    # ou seja, é falsi (2,1) XOR (2,2) XOR (2,3) XOR (2,4)
    if not (num&16) ^ (num&32) ^ (num&64) ^ (num&128):
        func = False
    # Não é função se 3 se relaciona com mais de um elemento
    # ou seja, é falso (3,1) XOR (3,2) XOR (3,3) XOR (3,4)
    if not (num&256) ^ (num&512) ^ (num&1024) ^ (num&2048):
        func = False
    # Não é função se 4 se relaciona com mais de um elemento
    # ou seja, é falso (4,1) XOR (4,2) XOR (4,3) XOR (4,4)
    if not (num&4096) ^ (num&8192) ^ (num&16384) ^ (num&32768):
        func = False

    return func

def sobrejetora(num):
    # Se não for função não pode ser uma função sobrejetora
    if not funcao(num):
        return False

    sobrej = True
    # Para ser sobrejetora cada elemento do contradomínio
    # precisa estar associado a pelo menos um elemento do domínio

    # Não é sobrejetora se não existem (1,1) ou (2,1) ou (3,1) ou (4,1)
    if not ((num&1) or (num&16) or (num&256) or (num&4096)):
        sobrej = False
    # Não é sobrejetora se não existem (1,2) ou (2,2) ou (3,2) ou (4,2)
    if not ((num&2) or (num&32) or (num&512) or (num&8192)):
        sobrej = False
    # Não é sobrejetora se não existem (1,3) ou (2,3) ou (3,3) ou (4,3)
    if not ((num&4) or (num&64) or (num&1024) or (num&16384)):
        sobrej = False
    # Não é sobrejetora se não existem (1,4) ou (2,4) ou (3,4) ou (4,4)
    if not ((num&8) or (num&128) or (num&2048) or (num&32768)):
        sobrej = False

    return sobrej

def injetora(num):
    # Se não for função não pode ser uma função injetora
    if not funcao(num):
        return False

    inj = True
    # Para ser injetora cada elemento do domínio precisa estar
    # associado a um elemento exclusivo do contradomínio

    # Não é injetora se for falso
    # (1,1) XOR (2,1) XOR (3,1) XOR (4,1)
    if not (num&1) ^ (num&16) ^ (num&256) ^ (num&4096):
        inj = False
    # Não é injetora se for falso
    # (1,2) XOR (2,2) XOR (3,2) XOR (4,2)
    if not (num&2) ^ (num&32) ^ (num&512) ^ (num&8192):
        inj = False
    # Não é injetora se for falso
    # (1,3) XOR (2,3) XOR (3,3) XOR (3,4)
    if not (num&4) ^ (num&64) ^ (num&1024) ^ (num&16384):
        inj = False
    # Não é injetora se for falso
    # (1,4) XOR (2,4) XOR (3,4) XOR (4,4)
    if not (num&8) ^ (num&128) ^ (num&2048) ^ (num&32768):
        inj = False

    return inj

def bijetora(num):
    # Uma função é bijetora se for sobrejetora
    # e injetora simultâneamente
    return sobrejetora(num) and injetora(num)

# Cria ou sobreescreve o arquivo conj.txt no modo de escrita
file = open("conj.txt", "w")

# Faz um loop para escrever no arquivo todos os
# possíveis subconjuntos de relações binárias
# e suas classificações
for i in range(65536):
    subconj = "{"
    if (i&1) != 0:
        subconj += "(1,1)"
    if (i&2) != 0:
        subconj += "(1,2)"
    if (i&4) != 0:
        subconj += "(1,3)"
    if (i&8) != 0:
        subconj += "(1,4)"
    if (i&16) != 0:
        subconj += "(2,1)"
    if (i&32) != 0:
        subconj += "(2,2)"
    if (i&64) != 0:
        subconj += "(2,3)"
    if (i&128) != 0:
        subconj += "(2,4)"
    if (i&256) != 0:
        subconj += "(3,1)"
    if (i&512) != 0:
        subconj += "(3,2)"
    if (i&1024) != 0:
        subconj += "(3,3)"
    if (i&2048) != 0:
        subconj += "(3,4)"
    if (i&4096) != 0:
        subconj += "(4,1)"
    if (i&8192) != 0:
        subconj += "(4,2)"
    if (i&16384) != 0:
        subconj += "(4,3)"
    if (i&32768) != 0:
        subconj += "(4,4)"
    subconj += "} "

    if simetrica(i):
        subconj += "S"

    if transitiva(i):
        subconj += "T"

    if reflexiva(i):
        subconj += "R"

    if equivalencia(i):
        subconj += "E"

    if irreflexiva(i):
        subconj += "I"

    if funcao(i):
        subconj += "F"

    if bijetora(i):
        subconj += "Fb"

    if sobrejetora(i):
        subconj += "Fs"

    if injetora(i):
        subconj += "Fi"

    file.write(subconj + "\n")

# Fecha o arquivo para encerrar e gravar as edições
file.close()

# Exibe o tempo de execução
fim = time.time()
print("Tempo de execução: {0:.3f}seg".format(fim-inicio))
