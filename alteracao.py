import mariadb
conexao = mariadb.connect(host="localhost",
       user="root",password="", database="escola")
cursor = conexao.cursor()

########################################
print("### ALTERAR DADOS DO ALUNO ###")
cod = input("Código do aluno: ")

cursor.execute(
    "SELECT * FROM alunos WHERE codigo = " + cod)

if cursor.rowcount == 0 : # não achou o código
    print("Código não encontrado.\n")

else: # achou o código
    for linha in cursor:   # mostra o aluno
        print (linha)
    
    resp = input("Alterar? (s/n) ")
    if resp == "s" :
        coluna = input(
            "Qual coluna? (nome/curso/serie) ")
        
        if coluna not in ('nome','curso','serie'):
            print("Coluna não existe.")
        
        else:
            valor = input("Novo valor: ")
            sql = f"""UPDATE alunos
                  SET {coluna} = '{valor}'
                  WHERE codigo = {cod} """
            cursor.execute(sql)
            conexao.commit()
            print("Alterado com sucesso.")

cursor.close()
conexao.close()