import discord;
import os;
from decouple import config

client = discord.Client()


if not os.environ['BOT_TOKEN']:
    print('could not find BOT_TOKEN')
    quit()
else: 
    print('found env variable')

rawbotToken = os.environ['BOT_TOKEN']
botToken = rawbotToken.replace('"','')


async def playAudio(voiceChannel, absAudioRoute):
        voiceClient =  await voiceChannel.connect() #connects to the sender voice chanel, and instance a discord.VoiceChannel
        source = discord.FFmpegPCMAudio(absAudioRoute)
        voiceClient.play(source)
        counter = 0
        while voiceClient.is_playing():
            counter += 1
        print('Audio ending after ', counter ,' cycles, disconnecting from voice channel now...\n')
        await voiceClient.disconnect()

#async def findAudio(senderMessage):
    
    

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    

    if message.author == client.user:
        return
    
    print('message recieved\n')

    #if message.content.startswith('$Hola BotardoBuenardo'):
     #   await message.channel.send('Hola! si estas hablando conmigo sos un topo. Y si sos un topo sos un capo.\n Salvo que seas manu. En ese caso sos un nepe.')

    
    """ 
    if message.content.startswith('$Hola BotardoBuenardo soy Rami'):
        await message.channel.send('Que acelga rami, sale rust? lol? o ese? o todas juntas? :wink: ')

     
    if message.content.startswith('$BotardoBuenardo te drogas?'):
        await message.channel.send('Obvio pa! vamo a mechar eso brodilovi')

    if message.content.startswith('$BotardoBuenardo sale ese?'):
        await message.channel.send('Obvio pa! vamo a mechar eso brodilovi') """

    if message.content.startswith('$BotardoBuenardo help'):
        await message.channel.send('Todavía no se configuró el help\nTodos los comandos empiezan con $BotardoBuenardo\n Si querés saber que audios hay preguntale al gordo.') 

    if message.content.startswith('$BotardoBuenardo pasate el audio de stepbro'):
       await playAudio(message.author.voice.channel,'./audioFiles/stepbro.mp3')
    
    if message.content.startswith('$BotardoBuenardo fail clip'):
       await playAudio(message.author.voice.channel,'./audioFiles/directedByclip.mp3')

    if message.content.startswith('$BotardoBuenardo pasate el audio de im stuck'):
       await playAudio(message.author.voice.channel,'./audioFiles/imstuck.wav')

    if message.content.startswith('$BotardoBuenardo no god please no'):
       await playAudio(message.author.voice.channel,'./audioFiles/nogodpleaseno.mp3')

    if message.content.startswith('$BotardoBuenardo la concha de tu madre'):
       await playAudio(message.author.voice.channel,'./audioFiles/conchatumadre.mp3')
    

    if message.content.startswith('$BotardoBuenardo ahí lo tenes al pelotudo'):
       await playAudio(message.author.voice.channel,'./audioFiles/ahilotenes.mp3')
    
    if message.content.startswith('$BotardoBuenardo aguante boke pato'):
       await playAudio(message.author.voice.channel,'./audioFiles/aguanteboke.mp3')

    #if message.content.startswith('$ '):
        #await message.channel.send('La verdad que no te entendí pedazo de gato. Por ahora solo me podes decir "$Hola BotardoBuenardo soy Rami" o "$Buenas BotardoBuenardo"')

client.run(botToken)


#Discord-Basic-Bot\audiotest.mp3s