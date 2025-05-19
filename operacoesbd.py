import mysql.connector
from main import *
def criarConexao(endereco,usuario, senha, bancodedados):
      return mysql.connector.connect(
  host=endereco,user=usuario, password=senha,database=bancodedados)

def encerrarBancoDados(connection):
      connection.close()


def buscarSala(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchone()  # Obtém apenas uma linha do resultado
        cursor.close()
        return resultado
    except mysql.connector.Error as err:
        print(f"Erro ao buscar elemento: {err}")
        return None  # Retorne None se houver erro
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None  # Retorne None se houver erro
def naoencontrado():
    print(f"Sala '{valorA}' não encontrada no {bloco}.")
    return None