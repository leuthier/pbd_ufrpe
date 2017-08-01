# -*- coding: utf-8 -*-
import pymysql

#cria o esquema VouDeQue caso nao exista e se conecta a ele
def ConectarBanco():
    servidor, usuario, senha, esquema = '127.0.0.1', 'root', '', 'voudeque'
    try:
        db = pymysql.connect(servidor, usuario, senha, esquema, use_unicode=True)
        cursor = db.cursor()

        return cursor, db
    except:
        db = pymysql.connect(servidor, usuario, senha, '')
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE if not exists voudeque DEFAULT CHARACTER SET utf8")

        db = pymysql.connect(servidor, usuario, senha, esquema)
        cursor = db.cursor()

        return cursor, db

cursor,db = ConectarBanco()

def Executa_SQL(pSQL):
    try:
        cursor.execute(pSQL)
        db.commit()
        return True
    except:
        print("Error: Não foi possível executar o SQL")
        db.rollback()

def Busca_SQL(pSQL):
    try:
        cursor.execute(pSQL)
        results = cursor.fetchall()
        return results
    except:
        print("Error: Não foi possível buscar os dados")
        return False