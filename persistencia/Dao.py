import persistencia.DataBase as dao

def Buscar(query):
    resultado = dao.Busca_SQL(query)
    print(resultado)
    if len(resultado)==0:
        return False
    return resultado


