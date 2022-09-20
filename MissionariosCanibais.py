class Estado():
    #estado com os seguintes atributos: qtd missionarios na direita(missionarios_dir), ]
    #qtd missionarios na esquerda(missionarios_esq), qtd canibais na direita(canibais_dir),
    #qtd canibais na esquerda(canibais_esq), lado que a canoa esta no rio(lado_canoa), noh pai(pai),
    #noh filho(filhos)

    def __init__(param, missionarios_esq, missionarios_dir, canibais_esq, canibais_dir, lado_canoa):
        param.missionarios_esq = missionarios_esq
        param.missionarios_dir = missionarios_dir
        param.canibais_esq = canibais_esq
        param.canibais_dir = canibais_dir
        param.lado_canoa = lado_canoa
        param.pai = None
        param.list_filhos = []

    def estado_valido(param):
        #Verificando estados validos = numero de missionarios em um lado do rio eh inferior ao numero de canibais nesse mesmo lado
        #Ou numero de missionarios == 0, ja que se um lado o numero de missionarios eh 0, no outro lado estao todos os missionarios
        return ((param.missionarios_esq >= param.canibais_esq or param.missionarios_esq == 0) and
                (param.missionarios_dir >= param.canibais_dir or param.missionarios_dir == 0))


    def estado_final(param):
        #Verifica se eh estado final, se todos ja atravessaram o rio
        resultado_esq = param.missionarios_esq == param.canibais_esq == 0
        resultado_dir = param.missionarios_dir == param.canibais_dir == 3
        return resultado_esq and resultado_dir

    def gerar_list_filhos(param):
        #Encontra o proximo lado da canoa no rio
        novo_lado_canoa = 'esq' if param.lado_canoa == 'dir' else 'dir'
        #possíveis movimentos
        movimentos = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 2},
        ]
        #Armazenar os possiveis estados na lista de filhos
        for movimento in movimentos:
            if param.lado_canoa == 'esq':
                canibais_esq = param.canibais_esq - movimento['canibais']
                canibais_dir = param.canibais_dir + movimento['canibais']
                missionarios_esq = param.missionarios_esq - movimento['missionarios']
                missionarios_dir = param.missionarios_dir + movimento['missionarios']
            else:
                canibais_dir = param.canibais_dir - movimento['canibais']
                canibais_esq = param.canibais_esq + movimento['canibais']
                missionarios_dir = param.missionarios_dir - movimento['missionarios']
                missionarios_esq = param.missionarios_esq + movimento['missionarios']
            #Cria novo estado do filho, se ele for valido, adiciona na lista de filhos
            filho = Estado(missionarios_esq, missionarios_dir, canibais_esq,
                           canibais_dir, novo_lado_canoa)
            filho.pai = param
            if filho.estado_valido():
                param.list_filhos.append(filho)

    def __str__(param):
        #representacao em string dos 2 lados do rio
        return 'Missionarios esq: {}\t| Missionarios dir: {}\nCanibais esq: {}\t\t| Canibais dir: {}'.format(param.missionarios_esq, param.missionarios_dir, param.canibais_esq, param.canibais_dir)

#todo
class MissionariosCanibais():
    def __init__(param):
       #comeca com uma raiz pre definida: 3 canibais e 3 missionarios na esq
        param.fila_execucao = [Estado(3, 0, 3, 0, 'esq')]
        param.solucao = None

    def gera_solucao_busca(param):
        # busca em largura
        for elemento in param.fila_execucao:
            if elemento.estado_final():
                param.solucao = [elemento]
                while elemento.pai:
                    param.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break;
            #caso elemento nao seja solucao, gera seus filhos
            elemento.gerar_list_filhos()
            param.fila_execucao.extend(elemento.list_filhos)


def main():
    problema = MissionariosCanibais()
    problema.gera_solucao_busca()

    for estado in problema.solucao:
        print(estado)
        print(36 * '-')

if __name__ == '__main__':
    main()