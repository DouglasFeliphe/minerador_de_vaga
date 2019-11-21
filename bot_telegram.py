import telepot

def executar_bot(_group_id, mensagem):
    """Enviar uma mensagem em formato de String para o telegram"""
    bot = telepot.Bot("1044300292:AAFwvSV7g50-8-lpNxYqCdAXHJsLQCrjPZs")
    bot.sendMessage(_group_id, mensagem)
