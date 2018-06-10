# Trabalho de Lógica e Matemática Discreta
## Relação Binária para conjunto de 4 elementos

Script que gera um arquivo com todas as possíveis relações binárias de AxA e suas classificações para um conjunto de 4 elementos A=[1,2,3,4].
Os resultados da execução são salvos em um arquivo `conj.txt` e o tempo de execução do script é printado no console.

As relações são classificadas como:
* Simétrica (S)
* Transitiva (T)
* Reflexiva (R)
* Equivalência (E)
* Irreflexiva (I)
* Função (F)
* Função bijetora (Fb)
* Função sobrejetora (Fs)
* Função injetora (Fi)

O código está comentado explicando cada função de classificação e a geração do arquivo resultante. Todas as comparações são feitas bitwise. Ou seja, para as 16 possíveis relações:

```
    0000000000000001 = {(4,4)}
    0000000000000010 = {(4,3)}
    0000000000000100 = {(4,2)}
    E assim por diante de forma que
    1111000011000011 = {(1,1), (1,2), (1,3), (1,4), (3,1), (3,2), (4,3), (4,4)}
```

Gerando o total de 2^16 possíveis conjuntos e onde:

```
    0000000000000001 & 2^0 = 0000000000000001
    0000000000000010 & 2^1 = 0000000000000010
    0000000000000100 & 2^2 = 0000000000000100
    ...
    1111111111111111 & 2^16 = 1111111111111111
```
