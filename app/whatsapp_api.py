

def send_message(numero: str, mensagem: str):
    """
    Simula envio de mensagem para WhatsApp.
    Em um projeto real, aqui entraria a chamada à API oficial.
    """
    print(f"[SIMULAÇÃO] Enviando para {numero}: {mensagem}")
    return {
        "status": "simulado",
        "numero": numero,
        "mensagem": mensagem
    }
