import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="escola")
cursor = conexao.cursor()

print("PESQUISA GERAL")
nome = input("Digite: ")

sql = f'''SELECT * FROM alunos WHERE nome LIKE '%{nome}%'
        OR curso LIKE '%{nome}%'
        OR serie = '{nome}' '''

cursor.execute(sql)

for linha in cursor:
    #print(linha)
    print("Código:\t", linha[0])
    print("Nome:\t",   linha[1])
    print("Curso:\t",  linha[2])
    print("Série:\t",  linha[3])
    print("----------------------")
    
cursor.close()
conexao.close()
