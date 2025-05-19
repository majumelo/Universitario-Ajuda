from inter import mapeamentoB
from operacoesbd import *

con = criarConexao('localhost', 'root', '12345', 'mapeamento')

while True:

    if con is None:
     print("Falha ao conectar ao banco de dados.")
     exit()

    bloco = input("Digite a Sala: ").lower()
    mapeamentoA = {"a101": 1, "a102": 2, "a103": 3,"a104": 4,"a105": 5, "a106": 6, "a107": 7,"a108": 8,"a109": 9, "a110": 10,
                  "a111": 11,"a112": 12,"a113": 13,"a114": 14,"a115": 15,"a116": 16,"a117": 17, "a118":18,"a119": 19,"a201": 20,
                  "a202": 21, "a203": 22,"a204": 23,"a205": 24,"a206": 25,"a207": 26,"a208": 27,"a209": 28,"a210": 29,"a211": 30,
                  "a212": 31,"gestão": 32,"dep.física": 33,"dep.química": 34,"dep.computação": 35,"dep.engenharia sanitaria": 36,
                  "dep.matemática": 37,"dep.estatistica": 38,"centro academico quimica industrial": 39,"centro academico computação": 40,
                  "ctica": 41,"banheiro térreo": 42,"banheiros 1° andar": 43,"direção do cct": 44}

    valorA = mapeamentoA.get(bloco)

    if valorA is not None:
        sql = "SELECT IdBlocoA, BlocoA FROM mapeamento WHERE IdBlocoA = {};".format(valorA)
        manifestacoesA = buscarSala(con, sql)
        print(manifestacoesA[1])
    else:
        def naoencontrado():
            print(f"Sala '{bloco}' não encontrada no Bloco A.")
            return None
        naoencontrado()


    mapeamentoB = {"b101": 45,"b102": 46,"b103": 47,"b104": 48,"b105": 49,"banheiros bloco b": 50,"b107": 51,"b108": 52,"b109": 52,"b110": 53,
                   "b112": 54,"laboratório pedagógico de matematica": 55,"laboratório de informática de matemática": 56,"b114": 57,"b115": 58,
                   "banheiros 1° andar bloco b ": 59, "b201": 60,"b202": 61,"b203": 62,"b204": 63,"b205": 64,"b206": 65,"b207": 66,"b208": 67,
                   "b209": 68,"b210": 69,"cetic b": 70,}
    valor2 = mapeamentoB.get(bloco)

    if valor2 is not None:
        sql = "SELECT IdBlocoB, BlocoB FROM mapeamento WHERE IdBlocoB = {};".format(valor2)
        manifestacoesB = buscarSala(con, sql)
        print(manifestacoesB[1])

    mapeamentoC = {"c101":71,"c102":72,"c103":73,"c104":74,"centro academico de eng. sanitaria e ambiental ":75,"c106":76,"c107":77,"c108":78,
                   "c109":79,"c110":80,"c201":81,"c202":82,"c203":83,"c204":84,"c205":85,"c206":86,"c207":87,"c208":88,"c209":89,"c210":90,
                   "c301":91,"c302":92,"c303":93,"c304":94,"c305":95,"c306":96,"c307":97,"c308":98,"c309":99,"c310":100,"centro academico de física":101,
                   "cetic c":102,"banheiros terreo bloco":103,"banheiros 1 ° andar bloco c":104,"banheiros 2° andar bloco c":105}
    valor2 = mapeamentoC.get(bloco)

    if valor2 is not None:
        sql = "SELECT IdBlocoC, BlocoC FROM mapeamento WHERE IdBlocoC = {};".format(valor2)
        manifestacoesC = buscarSala(con, sql)
        print(manifestacoesC[1])

