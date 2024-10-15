class FilaPartida:
    def __init__(self):
        self.fila = []
        self.limite_fila = 50

    # Função para adicionar um jogador à fila com verificação de limite.
    def adicionar_jogador(self, id_jogador, nivel_habilidade):
        if len(self.fila) >= self.limite_fila:
            print("A fila está cheia. Não é possível adicionar mais jogadores.")
        else:
            jogador = {"id": id_jogador, "nivel": nivel_habilidade}
            self.fila.append(jogador)
            print(f"Jogador {id_jogador} adicionado à fila (Nível {nivel_habilidade}).")
    
    # Função para remover um jogador da fila.
    def remover_jogador(self):
        if self.fila:
            jogador_removido = self.fila.pop(0)
            print(f"Jogador {jogador_removido['id']} foi alocado para uma partida.")
        else:
            print("Nenhum jogador na fila para ser removido.")

    # Função para retornar o número de jogadores que estão aguardando na fila.
    def verificar_fila(self):
        return len(self.fila)

    # Sistema de matchmaking para partidas 5 vs 5 com níveis aproximados.
    def matchmaking(self):
        if len(self.fila) < 10:
            print("Não há jogadores suficientes para formar uma partida 5 vs 5.")
            return None
        
        partida = []
        # Agrupa jogadores com diferença de nível máxima de 2, até formar um grupo de 10.
        jogador_base = self.fila[0]
        partida.append(jogador_base)
        
        for jogador in self.fila[1:]:
            if abs(jogador["nivel"] - jogador_base["nivel"]) <= 2:
                partida.append(jogador)
            if len(partida) == 10:
                break

        if len(partida) == 10:
            # Remove os jogadores da fila que foram agrupados.
            for jogador in partida:
                self.fila.remove(jogador)
            print(f"Partida formada com 10 jogadores: {[jog['id'] for jog in partida]}")
        else:
            print("Nenhuma partida pôde ser formada com os jogadores disponíveis.")

    # Função para permitir que sejam adicionados jogadores via terminal.
    def adicionar_jogadores_via_terminal(self):
        while True:
            nome = input("Digite o nome do jogador (ou 'sair' para encerrar): ")
            if nome.lower() == 'sair':
                break
            nivel = int(input(f"Digite o nível de habilidade do jogador {nome}: "))
            self.adicionar_jogador(nome, nivel)

    # Mostra o número de jogadores e pergunta se deseja adicionar mais.
    def gerenciar_fila(self):
        while True:
            # Tenta formar uma partida.
            self.matchmaking()

            # Mostra o número de jogadores após a formação da partida.
            jogadores_restantes = self.verificar_fila()
            print(f"Jogadores restantes na fila: {jogadores_restantes}")

            # Pergunta ao usuário se deseja adicionar mais jogadores.
            continuar = input("Deseja adicionar mais jogadores à fila? (sim/não): ")
            if continuar.lower() == 'sim':
                self.adicionar_jogadores_via_terminal()
            else:
                print("Encerrando o sistema de fila.")
                break

# Exemplo de uso no VSCode:
fila = FilaPartida()

# Adiciona jogadores via terminal.
fila.adicionar_jogadores_via_terminal()

# Gerencia a fila, formando partidas e permitindo adicionar mais jogadores.
fila.gerenciar_fila()
