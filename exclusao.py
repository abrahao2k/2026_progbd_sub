import mariadb
conexao = mariadb.connect(host="localhost",
       user="root",password="", database="escola")
cursor = conexao.cursor()

########################################
print("### EXCLUIR ALUNO ###")
cod = input("Código do aluno: ")

cursor.execute(
    "SELECT * FROM alunos WHERE codigo = " + cod)

if cursor.rowcount == 0 : # não achou o código
    print("Código não encontrado.\n")

else: # achou o código
    for linha in cursor:   # mostra o aluno
        print (linha)
    
    resp = input("Excluir? (s/n) ")
    if resp == "s" :
        cursor.execute(
        "DELETE FROM alunos WHERE codigo = " + cod)
        conexao.commit()
        print("Excluído com sucesso.\n")

cursor.close()        
conexao.close()