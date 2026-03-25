from fastapi import FastAPI, Request
from app.nlp import classify_intent
app = FastAPI()
@app.post("/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.json()
    mensagem = data.get ("mensagem", "")
    numero = data.get("numero" , "")
    intent = classify_intent(mensagem)
    resposta = gerar_resposta(intent)
    return {"numero": numero ,"mensagem": mensagem , "intent": intent , "resposta": resposta}
def gerar_resposta(intent):
    if intent == "faq_preco":
        return "Nossos planos começam em R$ 99/mês."
    elif intent == "faq_horario":
        return "Atendemos de segunda a sexta, das 9h às 18h."
    elif intent == "lead_qualificacao":
        return "Ótimo! Qual é o seu orçamento estimado?"
    elif intent == "smalltalk":
        return "Prazer falar com você!"
    else:
        return "Obrigado pelo contato! Em breve nossa equipe responde."