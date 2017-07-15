from Projeto_de_Banco_de_Dados.persistencia import DataBase as dao

def Buscar(nome):
    resultado = dao.Busca_SQL("SELECT * FROM MARCA WHERE NOME = '"+nome+"'")
    if len(resultado)==0:
        return False
    return True
