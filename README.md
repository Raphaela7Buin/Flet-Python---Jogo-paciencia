#Jogo de Cartas Solitário (Paciência) em Flet

Projeto desenvolvido em Python utilizando a biblioteca **Flet** para a construção de uma interface gráfica interativa baseada na mecânica do jogo de cartas Solitário (Paciência).

##Relatório do Projeto

### 1 Objetivos
O objetivo deste projeto é implementar uma aplicação desktop/web interativa para movimentação de cartas em slots estilo Paciência, aplicando conceitos de manipulação de estados, tratamento de eventos e interfaces declarativas.

### 2. Funcionalidades Implementadas
- **Sistema Drag & Drop:** Movimentação fluida de cartas através de coordenadas dinâmicas (`top` e `left`) tratadas via `GestureDetector`.
- **Cascata e Empilhamento:** Ao soltar uma carta sobre um slot ocupado, ela se posiciona automaticamente abaixo da carta anterior com um offset vertical de 25px.
- **Movimentação em Grupo:** Seleção e arraste encadeado de uma pilha completa de cartas mantendo a hierarquia do slot.
- **Mecânica de Retorno (Bounce Back):** Identificação de soltura fora dos alvos com restauração das posições originais gravadas em memória.
- **Layout Personalizado:** Container de fundo estilizado com gradiente de cor verde mesa de jogo (`#0d3b23` a `#0a2918`) e alinhamento via `ft.Alignment`.
- **Renderização de Mídia Remota:** Suporte a carregamento direto de fotos via URL em dimensões padronizadas de 70x100px.

## Tecnologias Utilizadas
- **Python 3.x**
- **Flet Framework**
- **Git & GitHub**


## Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone [https://github.com/Raphaela7Buin/Flet-Python---Jogo-paciencia.git](https://github.com/Raphaela7Buin/Flet-Python---Jogo-paciencia.git)
   cd Flet-Python---Jogo-paciencia
