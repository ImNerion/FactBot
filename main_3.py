import discord
from discord.ext import commands
import pyttsx3
import random

# -----------------------------------
# CONFIGURACIÓN DEL BOT
# -----------------------------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="?", intents=intents)


# -----------------------------------
# DATOS CURIOSOS
# -----------------------------------

facts = {
    "ciencia": [
        "El cuerpo humano tiene aproximadamente 37 billones de células.",
        "La luz del Sol tarda aproximadamente ocho minutos en llegar a la Tierra.",
        "El agua puede existir en tres estados: sólido, líquido y gaseoso.",
        "Los pulpos tienen tres corazones.",
        "El sonido no puede viajar por el vacío."
    ],

    "historia": [
        "Cleopatra vivió más cerca de la llegada del ser humano a la Luna que de la construcción de las pirámides de Guiza.",
        "La Universidad de Oxford es más antigua que el Imperio azteca.",
        "La Revolución francesa comenzó en 1789.",
        "La imprenta de Gutenberg ayudó a expandir la producción de libros en Europa.",
        "El Imperio romano llegó a controlar territorios de tres continentes."
    ],

    "animales": [
        "Los cuervos pueden resolver problemas y utilizar herramientas.",
        "Las jirafas tienen siete vértebras cervicales, igual que los seres humanos.",
        "Los delfines utilizan sonidos para comunicarse y orientarse.",
        "Los elefantes pueden reconocerse frente a un espejo.",
        "Algunas especies de pingüinos forman parejas durante largos períodos."
    ],

    "espacio": [
        "Júpiter es el planeta más grande del sistema solar.",
        "Un día en Venus dura más que un año en Venus.",
        "La Luna se está alejando lentamente de la Tierra.",
        "Saturno tiene anillos formados principalmente por hielo y roca.",
        "En Marte se encuentra Olympus Mons, uno de los volcanes más grandes conocidos del sistema solar."
    ],

    "tecnologia": [
        "El primer mensaje enviado mediante ARPANET fue en 1969.",
        "El primer teléfono móvil comercial fue lanzado en 1983.",
        "El lenguaje Python fue creado por Guido van Rossum.",
        "El código QR fue desarrollado originalmente para la industria automotriz japonesa.",
        "Bluetooth recibe su nombre de Harald Bluetooth, un rey de Dinamarca."
    ]
}


# -----------------------------------
# FUNCIÓN PARA EL TTS
# -----------------------------------

def speak(text):
    # Crear un nuevo motor cada vez
    engine = pyttsx3.init()

    # Hacer que hable más despacio
    engine.setProperty("rate", 150)

    # Hablar
    engine.say(text)
    engine.runAndWait()

    # Cerrar el motor
    engine.stop()


# -----------------------------------
# CUANDO EL BOT SE CONECTA
# -----------------------------------

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


# -----------------------------------
# COMANDO !START
# -----------------------------------

@bot.command()
async def start(ctx):
    mensaje = (
        "¡Hola! 👋 Soy FactBot.\n\n"
        "Puedo darte datos curiosos de diferentes temáticas.\n\n"
        "📚 **Temáticas disponibles:**\n"
        "🔬 Ciencia\n"
        "🏛️ Historia\n"
        "🐾 Animales\n"
        "🚀 Espacio\n"
        "💻 Tecnología\n\n"
        "Para recibir un dato, escribe:\n"
        "`!fact [temática]`\n\n"
        "Por ejemplo: `!fact espacio`"
    )

    await ctx.send(mensaje)

    speak(
        "¡Hola! Soy FactBot. "
        "Puedo darte datos curiosos de ciencia, historia, animales, espacio y tecnología."
    )


# -----------------------------------
# COMANDO !FACT
# -----------------------------------

@bot.command()
async def fact(ctx, categoria=None):

    if categoria is None:
        await ctx.send(
            "❌ Debes elegir una temática.\n\n"
            "🔬 `!fact ciencia`\n"
            "🏛️ `!fact historia`\n"
            "🐾 `!fact animales`\n"
            "🚀 `!fact espacio`\n"
            "💻 `!fact tecnologia`"
        )
        return

    categoria = categoria.lower()

    if categoria not in facts:
        await ctx.send(
            "❌ Esa temática no existe.\n\n"
            "Las temáticas disponibles son:\n"
            "🔬 Ciencia\n"
            "🏛️ Historia\n"
            "🐾 Animales\n"
            "🚀 Espacio\n"
            "💻 Tecnología"
        )
        return

    # Elegir un dato aleatorio
    dato = random.choice(facts[categoria])

    # Enviar el dato
    await ctx.send(
        f"🧠 **Dato curioso de {categoria.capitalize()}:**\n{dato}"
    )

    # Reproducir el dato con TTS
    speak(dato)


# -----------------------------------
# INICIAR BOT
# -----------------------------------

bot.run("")