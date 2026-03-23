import mariadb    # mysql.connector
conexao = mariadb.connect(
            host="localhost",
            user="root",
            password="",
            database="escola")

print("Conectou...")
cursor = conexao.cursor()

while True:
    print("=== CADASTRO DE ALUNO ===")
    nome = input("Nome : ")
    curso= input("Curso: ")
    serie= input("Série: ")
    sql = f'''INSERT INTO alunos VALUES(
            null, "{nome}", "{curso}",
            {serie}) '''
    cursor.execute(sql)
    conexao.commit()
    print("Gravado com sucesso.")
    
    resp = input("Cadastrar outro? (s/n)")
    if resp == "n" : break

cursor.close()   # fechar a conexão com o bd
conexao.close()
print("Conexão finalizada.")