import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
)


# Criando o cursor (é ele quem executa os comandos SQL)
cursor = conexao.cursor()

# Criando banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS library_system")

# Seleciona o banco de dados onde vai ficar a tabela
cursor.execute("USE library_system")

cursor.execute("""
CREATE TABLE IF NOT EXISTS library (
               id INT AUTO_INCREMENT PRIMARY KEY,
               titulo VARCHAR(100),
               autor VARCHAR(100),
               genero VARCHAR(100),
               data_lancamento DATE,
               estatus VARCHAR(20),
               quantidade INT
               )


""")

def livros():
    cursor.execute("""SELECT * FROM  library""")
    livros = cursor.fetchall()
    print(livros[1][1])

    for conta in livros:
        id, titulo, autor, genero, data_lacamento, status, quantidade = conta
        print(f"""Id: {id}
        Titulo: {titulo}
        autor: {autor}
        genero: {genero}
        data de lançamento: {data_lacamento}
        status: {status}
        quantidade: {quantidade}

        """)
        print("\n")

    conexao.commit()

def devolver_livro():
    titulo_livro = input("Qual o titulo do livro ?\n")
    cursor.execute("SELECT * FROM library WHERE titulo = %s", (titulo_livro,))
    livro = cursor.fetchall()
    if not livro:
        adcionar_novo = input("O livro não existe em sistema deseja adicionar ?")
        if adcionar_novo == "s":
            autor = input("Qual o nome do autor ?\n")
            genero = input("Qual o genero do livro ?\n")
            data_lancamento = input("Qual data de lançamento do livro ?\n")
            quantidade = input("Quanto desse livro está devolvendo ?\n")
            
            cursor.execute("""INSERT INTO library
                   (titulo, autor, genero, data_lancamento, quantidade)
                   VALUES (%s, %s, %s, %s, %s)""", (titulo_livro, autor, genero, data_lancamento, quantidade))
            conexao.commit()

    else:
        quantidade_devolvida = int(input("Quantos livros estão sendo devolvidos? "))
        quantidade_atual = livro[0][6]
        nova_quantidade = quantidade_devolvida + quantidade_atual
        cursor.execute("UPDATE library SET quantidade = %s WHERE titulo = %s", (nova_quantidade, titulo_livro))
        if nova_quantidade > 0:
            cursor.execute("UPDATE library SET estatus = %s WHERE titulo = %s", ("Disponivel", titulo_livro))
        else:
            cursor.execute("UPDATE library SET estatus = %s WHERE titulo = %s", ("Indisponivel", titulo_livro))


    conexao.commit()
    
def empretismo_livro():
    titulo_livro = input("Qual nome do autor ")

def doar_livros():
    print("Agradecimento por está doando livro")

while True:
    print("""
    ==========BEM VINDO A BLIBIOTECA==========
          [0] Ver livros disponiveis
          [1] Emprestimo de livros
          [2] Devolver livro
          [3] Doar livro
          [4] Sair
""")
    menu = input("Escolha uma opção:")
 
    if menu == "0":
        livros()

    elif menu == "1":
        empretismo_livro()

    elif menu == "2":
        devolver_livro()

    elif menu == "3":
        doar_livros()

    elif menu == "4":
        break
