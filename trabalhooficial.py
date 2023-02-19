# Informações sobre o estudante que fez o trabalho:
print ('Nome do Estudante: Marcos Henrique Dias Zampieri')
print ('Curso: Analise e Desenvolvimento de Sistemas')
print ('Turma: Raciocínio Computacional (11100010563_20221_01)')
print ('Professor: Galbas Milleo Filho')

# Iniciando jogo com uma pequena explicação!
print ('-' * 35)
print ('😄' ' ┊ Seja bem vindo(a) ao Zombie Dice!')
print ('🧟‍♂️' ' ┊ Em Zombie Dice, você é um zumbi! ┊ ''🧟‍♂️')
print ('-' * 35)

print ('📖' ' ┊ Regras do Jogo: Você quer cérebros - mais cérebro do que qualquer um de seus amigos zumbis. Os 13 dados personalizados são suas vítimas. Empurre a sua sorte para comer seus cérebros 🧠, mas pare de rolar antes que os tiros de espingarda terminem o seu turno! Vence aquele que recolher 🧠 13 cérebros primeiro.🧠')
print ('-' * 35)
input ('🎲' ' ┊ Para iniciar o jogo aperte *ENTER*')
print()

# Ligações usadas no codigo
import random
from random import shuffle


# Criar jogadores que irão jogar o jogo
def criar_jogadores():
    lista_jogadores = []
    quan_jogadores = 0
    while quan_jogadores < 2:
        try:
            quan_jogadores = int(input( '💠 Para darmos continuidade a partida, por favor informe a quantidade de jogadores que irão jogar: '))
            print()
            if quan_jogadores < 2:
                print('❎' ' ┊ Desculpa, mas para iniciar uma partida, o jogo precisa de ao menos 2 jogadores!')
                print()
        except ValueError:
            print()
            print('❎' '┊ Digite um numero inteiro, por favor!')
            print()
    for i in range(quan_jogadores):
        nome = str(input('💻' ' ┊ Por Favor, informe o nome do jogador: ' + str(i + 1) + ': ')).strip().upper()
        lista_jogadores.append(nome)
    print('✅' ' ┊ Nomes registrados com sucesso!')
    str(input('🚨' ' ┊ Vamos começar a partida? Pressione "y" para sim: ')).strip().upper()
    return lista_jogadores

# Função para definir os copos
def encher_copo():
    copo_dados = [d_green, d_green, d_green, d_green, d_green, d_green, d_yellow, d_yellow,
              d_yellow, d_yellow, d_red, d_red, d_red]
    shuffle(copo_dados)
    return copo_dados

# Resultados da partida
def pontuar(faces_sorteadas):
    for lado in faces_sorteadas:
        if lado == 'C':
            score_atual['Cérebros'] += 1
        elif lado == 'E':
            score_atual['Tiros'] += 1
        else:
            score_atual['Passos'] += 1
    print(f'Resultado desta rodada: {score_atual}.\n')
    return score_atual

# Controle dos dados
def devolver_dados(faces_sorteadas, dados_na_mao):
    for i in range(2, -1, -1):
        if faces_sorteadas[i] != 'P':
            dados_na_mao.pop(i)
    cor_dado = [cor for dado in dados_na_mao for cor in dado.keys()]
    print(f'Jogador permanece com {len(dados_na_mao)} dados na mão: {[i for i in cor_dado]}\n')
    return dados_na_mao

# Jogar os dados
def jogar_dados():
    faces_sorteadas = [dado[face][random.randint(0, 5)] for dado in dados_na_mao for face in dado]
    for i in faces_sorteadas:
        if i == 'C':
            print('🧠' '┊ Muito bem! Você comeu um cerebro!')
        elif i == 'E':
            print('🔫' '┊ Poxa você levou um tiro :(')
        else:
            print('👣' '┊ Vi algumas pegadas aqui, acho que sua vitima escapou!')
    print()
    return faces_sorteadas

d_green = {'Verde': ('C', 'C', 'C', 'E', 'P', 'P')}
d_yellow = {'Amarelo': ('C', 'C', 'E', 'E', 'P', 'P')}
d_red = {'Vermelho': ('C', 'E', 'E', 'E', 'P', 'P')}

# Definindo variaveis
jogadores = criar_jogadores()
copo_dados = encher_copo()
fim_do_jogo = False
placar_rodada = [{jogador: 0} for jogador in jogadores]

# Mostrando dados na mão do Jogador
def pegar_dados(copo_dados):
    dados_na_mao = []
    while len(dados_na_mao) < 3:
        if len(dados_na_mao) + len(copo_dados) >= 3:
            dados_na_mao.append(copo_dados.pop())
        else:
            copo_dados = encher_copo()
            print('🎲' ' ┊ Os dados forão devolvidos para o copo!')
    cor_dado = [cor for dado in dados_na_mao for cor in dado.keys()]
    print( '🎲' f'\n{jogador} está com os seguintes dados:\n\n {cor_dado[0]}\n {cor_dado[1]}\n {cor_dado[2]}!')
    return dados_na_mao, copo_dados


# Fim da Partida
while not fim_do_jogo:
    for i, jogador in enumerate(jogadores):
        print()
        print(f'Pontuação total atual: {placar_rodada}.')
        print()
        print(f'Turno do Jogador {jogador}.')
        score_atual = {'Cérebros': 0,  'Tiros': 0, 'Passos': 0}
        copo_dados = encher_copo()
        while True:
            if placar_rodada[i][jogador] >= 13:
                fim_do_jogo = True
                break
            else:
                print()
                input('🎲' f' ┊ {jogador}, para continuar a rodada pressione ENTER para pegar os dados do copo!')
                dados_na_mao, copo = pegar_dados(copo_dados)
                input('🎲' f' ┊ {jogador}, agora pressione ENTER novamente para jogar os dados.')
                print()
                faces_sorteadas = jogar_dados()
                score_atual = pontuar(faces_sorteadas)
                devolver_dados(faces_sorteadas, dados_na_mao)
                
                if score_atual['Tiros'] >= 3:
                    print('😕' f' ┊ Infelizmente,{jogador} tomou 3 tiros e perdeu todos os pontos do turno!')
                    break
                elif score_atual['Cérebros'] + placar_rodada[i][jogador] >= 4:
                    placar_rodada[i][jogador] += score_atual['Cérebros']
                    print('😅' f' ┊ {jogador} está a alguns passos de ganhar o jogo, o mesmo já passui pontuação suficiente!\n')
                    fim_do_jogo = True
                    break
                else:
                    continuar = str(input('🧠' f' ┊ Deseja continuar a partida? \n  (n = NÃO) (s = SIM)! ')).strip().upper()
                    if continuar == 'N':
                        placar_rodada[i][jogador] += score_atual['Cérebros']
                        break
print ('-' * 50)
print('🏆' f' ┊ VITORIA ┊ ' '🏆')
print('🧟‍♂️' f' ┊ PLACAR DA PARTIDA: {placar_rodada}. ┊ ''🧟‍♂️')
print('😄' f' ┊ Obrigado por ter jogado Zombie Dice, espero te ver novamente! ┊ ' '😄')
print ('-' * 50)

# Fim do Trabalho
