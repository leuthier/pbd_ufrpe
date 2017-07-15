import pymysql

#cria o esquema VouDeQue caso nao exista e se conecta a ele
def ConectarBanco():
    servidor, usuario, senha, esquema = '127.0.0.1', 'root', '', 'VouDeQue'
    try:
        db = pymysql.connect(servidor, usuario, senha, esquema)
        cursor = db.cursor()
        return cursor, db, False
    except:
        db = pymysql.connect(servidor, usuario, senha, '')
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE VouDeQue DEFAULT CHARACTER SET utf8")

        db = pymysql.connect(servidor, usuario, senha, esquema)
        cursor = db.cursor()
        return cursor, db, True

cursor,db,boolean = ConectarBanco()

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

def CriaTabelas():
    '''
    tabelaClinica = "CREATE TABLE IF NOT EXISTS CLINICA (CODCLI INT NOT NULL AUTO_INCREMENT, NOMECLI VARCHAR(45) NULL, LOCALCLI VARCHAR(45) NULL, PRIMARY KEY (CODCLI) ) ENGINE=InnoDB"
    Executa_SQL(tabelaClinica)

    tabelaEspecialidade = "CREATE TABLE IF NOT EXISTS ESPECIALIDADE (CODESPECI INT NOT NULL AUTO_INCREMENT, NOME VARCHAR(45) NULL, CODESPECIGENERICA INT NULL, PRIMARY KEY (CODESPECI), INDEX CODESPECIGENERICA_IDX (CODESPECIGENERICA ASC), CONSTRAINT CODESPECIGENERICA FOREIGN KEY (CODESPECIGENERICA) REFERENCES ESPECIALIDADE (CODESPECI) ON DELETE SET NULL ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaEspecialidade)

    tabelaMedico = "CREATE TABLE IF NOT EXISTS MEDICO (CODMED INT NOT NULL AUTO_INCREMENT, NOMEMED VARCHAR(45) NULL, CODESPECI INT NULL, PRIMARY KEY (CODMED), INDEX CODESPECI_IDX (CODESPECI ASC), CONSTRAINT CODESPECI FOREIGN KEY (CODESPECI) REFERENCES ESPECIALIDADE (CODESPECI) ON DELETE SET NULL ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaMedico)

    tabelaClinicaMedico = "CREATE TABLE IF NOT EXISTS CLINICAMEDICO (CODCLI INT NOT NULL, CODMED INT NOT NULL, PRIMARY KEY (CODCLI, CODMED), INDEX CODMED_IDX (CODMED ASC), CONSTRAINT CODCLI FOREIGN KEY (CODCLI) REFERENCES CLINICA (CODCLI) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT CODMED FOREIGN KEY (CODMED) REFERENCES MEDICO (CODMED) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaClinicaMedico)

    tabelaAgendaConsulta = "CREATE TABLE IF NOT EXISTS AGENDACONSULTA (CODCLINICA INT NOT NULL, CODMEDICO INT NOT NULL, DATA DATE NOT NULL, HORA TIME NOT NULL, PRIMARY KEY (CODCLINICA, CODMEDICO, DATA, HORA), INDEX CODMEDICO_IDX (CODMEDICO ASC), CONSTRAINT CODCLINICA FOREIGN KEY (CODCLINICA) REFERENCES CLINICAMEDICO (CODCLI) ON DELETE CASCADE ON UPDATE CASCADE, CONSTRAINT CODMEDICO FOREIGN KEY (CODMEDICO) REFERENCES CLINICAMEDICO (CODMED) ON DELETE CASCADE ON UPDATE CASCADE) ENGINE=InnoDB"
    Executa_SQL(tabelaAgendaConsulta)'''

if boolean == True: # Banco estÃ¡ sendo criado
    CriaTabelas()