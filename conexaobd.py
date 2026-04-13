import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="escola")
cursor = conexao.cursor()
