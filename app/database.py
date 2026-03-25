import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname="chatbotdb",
        user="seu_usuario",
        password="sua_senha",
        host="localhost",
        port="5432"
    )
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS interacoes (
        id SERIAL PRIMARY KEY,
        numero TEXT,
        mensagem TEXT,
        intent TEXT,
        resposta TEXT,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id SERIAL PRIMARY KEY,
        numero TEXT,
        nome TEXT,
        orcamento TEXT,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

def salvar_interacao(numero, mensagem, intent, resposta):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO interacoes (numero, mensagem, intent, resposta) VALUES (%s, %s, %s, %s)",
        (numero, mensagem, intent, resposta)
    )
    conn.commit()
    cur.close()
    conn.close()
