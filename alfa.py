import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get('TOKEN')  # Pega do Railway
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    nome = message.from_user.first_name
    bot.send_message(message.chat.id, f"Hola {nome}!")
    
    try:
        bot.send_video(message.chat.id, open('1.mp4', 'rb'), 
                       caption="EN EL MERCADO, LA EMOCIÓN NO DEBE GUIAR TU DECISIÓN. ACTÚA CON ESTRATEGIA, NO CON IMPULSO.")
    except:
        pass  # Se não achar o vídeo, pula
    
    try:
        bot.send_photo(message.chat.id, open('2.jpg', 'rb'), 
                       caption="¡Hola! Soy Ezi Magalhães, Trader Profesional._🚀
Ayudo a personas como tú a generar ingresos diarios seguros con Alfa Trader, nuestra IA que te envía señales precisas para operar 📈🤖

💰 Muchos ya están ganando entre 20 y 30 dólares al día... ¡sin experiencia previa!
📲 ¿Quieres unirte?
1. Entra en alfatrader.online
2. Espera 3 segundos y Ve a ACCESO INMEDIATO
3. Confirma tu Activación!
¡Listo! Estás con nosotros 📈

Desarrollé una IA para mejorar nuestras operaciones y buscar rentabilidad. Sé que es difícil lograrla, pero estamos aquí para ayudarte... 🤝")
    except:
        pass  # Se não achar a foto, pula
    
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("🔥 INICIAR AHORA 🔥", url="https://wa.me/556792353335?text=Quiero%20ser%20un%20ALFA%20Trader"),
        InlineKeyboardButton("📲 SEGUIR EN INSTAGRAM", url="https://www.instagram.com/alfa.trader/")
    )
    
    texto = """Te invito cordialmente a seguir nuestras plataformas oficiales donde compartimos contenido sobre trading, resultados reales y mucho más 📊💰

🔗 Síguenos en nuestro segundo canal de WhatsApp:
👉https://whatsapp.com/channel/0029Vb3es2MHbFVD3hBjkw44
¡Es 100% gratis y te mantiene al día con todo lo que hacemos! ⚡

📸 También sígueme en Instagram:
👉https://www.instagram.com/ezimagalhaes_trader?igsh=bTR4YmwzNTc5dWJm
Ahí mostramos resultados, tips, estrategias y mucho más 🔥

¡Te espero por allá para seguir creciendo juntos! 💪🚀"""
    
    bot.send_message(message.chat.id, texto, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    if "como funciona" in texto or "funciona" in texto or "trading" in texto:
        bot.reply_to(message, """📊 ¿Qué es el trading?
Es la compra y venta de activos financieros como divisas, acciones, criptomonedas o materias primas, con el objetivo de obtener ganancias a corto plazo.

🔍 ¿El problema?
Hacer análisis de mercado por tu cuenta puede llevar horas y requiere experiencia... 😔

🤖 ¿La solución?
Nuestra IA Alfa Trader lo hace por ti: analiza los mercados en tiempo real, detecta oportunidades y te envía señales listas para aprovechar. Así, tú solo ejecutas las operaciones con mayor precisión y sin complicaciones.

⚠️ Importante entender esto:
El uso de la IA es mensual [30 días] 13$, pero para poder operar necesitas hacer tu propio depósito en la plataforma Pocket que te dejamos el Link.

Nosotros facilitamos la herramienta, pero no podemos aportar el capital de cada usuario. ¡Eso ya depende de ti!

🎁 Usa el código: 50START al hacer tu primer depósito y obtendrás un 50% extra en capital si depositas a partir de 50 USD.

💡 Ejemplo:
Si depositas $80, recibirás $40 extra, empezando con $120 en total. Más capital = mayor rentabilidad diaria 🤑

📲 ¿Con cuánto deseas empezar para enviarte tu plan de trading personalizado? 💰🔥""")
        
    elif "precio" in texto or "cuesta" in texto or "valor" in texto or "13" in texto:
        bot.reply_to(message, """💵 El acceso a la IA Alfa Trader cuesta solo 13$ USD mensuales [30 días].

Incluye señales diarias + soporte + actualizaciones.

⚠️ Recuerda: Ese valor es solo por la herramienta. Para operar necesitas hacer tu propio depósito en la plataforma. ¡El capital depende de ti!""")
        
    elif "pagar" in texto or "pago" in texto or "binance" in texto or "tarjeta" in texto:
        bot.reply_to(message, """💳 Formas de pago aceptadas:

✅ Binance Pay / USDT
✅ Tarjeta de crédito/débito

Rápido, seguro y sin complicaciones 🚀

¿Listo para activar? Escríbeme: https://wa.me/556792353335?text=Quiero%20activar%20ALFA""")
        
    elif "país" in texto or "pais" in texto or "argentina" in texto or "mexico" in texto or "colombia" in texto:
        bot.reply_to(message, """🌎 ¡SÍ! Funciona en TODOS los países.

🇦🇷🇲🇽🇨🇴🇨🇱🇵🇪🇧🇷🇺🇾🇵🇾🇪🇨🇻🇪🇧🇴

Donde haya internet, Alfa Trader llega. 
Solo necesitas tu celular y una cuenta en Pocket Option.""")
        
    elif "experiencia" in texto or "saber" in texto:
        bot.reply_to(message, """❌ NO necesitas experiencia en trading.

✅ Solo necesitas:
1️⃣ Seguir el plan al pie de la letra
2️⃣ Tener disciplina 
3️⃣ No operar con emoción

La IA hace el análisis por ti. Tú solo copias y pegas la señal 📲""")
        
    elif "dinero" in texto or "capital" in texto or "empezar" in texto or "50" in texto or "100" in texto:
        bot.reply_to(message, """💰 La mayoría de los Alfas empiezan con 50 a 100 USD por día.

🎁 BONUS: Usa el código 50START en tu primer depósito en Pocket y gana 50% extra si depositas desde 50 USD.""")
        
    elif "señales" in texto or "cuantas" in texto:
        bot.reply_to(message, """📈 Enviamos 8 señales por día en promedio.

Solo las de MAYOR probabilidad. Calidad > Cantidad 🎯

No te vamos a saturar con 50 señales malas.""")
        
    elif "horario" in texto or "hora" in texto or "cuando" in texto:
        bot.reply_to(message, """⏰ Las señales llegan de acuerdo al movimiento del mercado.

La IA monitorea 24/7 y te avisa cuando hay oportunidad REAL.

Activa las notificaciones del Telegram 🔔 para no perder ninguna.""")
        
    else:
        bot.reply_to(message, """No entendí bien 🤔

Escríbeme directo al WhatsApp que te respondo en persona:
https://wa.me/595983981838?text=Tengo%20una%20duda

O usa /start para ver el menú principal.""")

print("ALFA EZI ONLINE...")
bot.infinity_polling()
