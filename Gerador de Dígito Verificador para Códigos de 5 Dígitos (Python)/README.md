# Gerador de Dígito Verificador para Códigos de 5 Dígitos (Python)

Este projeto foi desenvolvido para praticar a decomposição de strings, aplicação de matrizes de pesos fixos e aritmética de módulo. O programa lê continuamente códigos numéricos de 5 dígitos via terminal, calcula o seu respectivo Dígito Verificador (DV) através de uma função customizada e exibe um relatório formatado ao encerrar a execução.

## O que foi praticado neste exercício:
* **Mapeamento Posicional com Vetores:** Uso de uma lista de pesos fixos (`[6, 5, 4, 3, 2]`) alinhada ao índice dos dígitos para realizar multiplicações ponderadas.
* **Modularização com Funções:** Criação da função encapsulada `separardigitos()` para isolar a responsabilidade do cálculo matemático do fluxo principal do programa.
* **Acumulação e Iteração:** Uso de loops `for` para processamento sequencial de caracteres e armazenamento dos resultados formatados em uma lista global para exibição posterior.
