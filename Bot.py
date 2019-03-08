import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import colorsys
import sys
import subprocess
import os
import json
import traceback
import random
import request
from discord.utils import find





bot = commands.Bot(command_prefix='ns!')
bot.remove_command('help')




@bot.event
async def on_ready():
    print ("Bot FF • DW On")
    print ("quem ta falando é o " + bot.user.name)
    print ("Meu numero do ZipZop: " + bot.user.id)
    while True:
    	await bot.change_presence(game=discord.Game(name='Fui criado pelo Mateusᴱʳʸᵏᵃʰ#6548| ns!ajuda'.format(len(bot.servers)), type=2))
    	await asyncio.sleep(10)
    	await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members())))+ ' Pessoas que Não Fazem Silencio 🔇!', type=3))
    	await asyncio.sleep(20)
    	await bot.change_presence(game=discord.Game(name='Parabéns [𝑮𝒉𝒐𝒖𝒍] [̲̅S̲̅α̲̅и̲̅s̲̅]#4183, Namorado Da Barbie! 🎉'))
    	await asyncio.sleep(10)




    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def votar(ctx, *, mensagem: str= None):
	if not mensagem:
		return await bot.say('Você precisa falar algo para votar')
	else:
			vote = await bot.say(embed=discord.Embed(color=0xff0000, description=mensagem))
			await bot.add_reaction(vote, "✅")
			await bot.add_reaction(vote, "❌")
	print('comando votar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

	
		
			
					
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member=None):
	user = user or ctx.message.author
	embed = discord.Embed(title="informações de {}".format(user.name), color=0x00ff00)
	embed.add_field(name="Nome", value=user.name, inline=True)
	embed.add_field(name="ID do usuário", value=user.id, inline=True)
	embed.add_field(name="Status do usuário", value=user.status, inline=True)
	embed.add_field(name="Melhor cargo", value=user.top_role)
	embed.add_field(name="entrou no servidor", value=user.joined_at)
	embed.set_footer(text ='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
	await bot.say(embed=embed)
	print('comando attlogs digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, motivo: str = None):
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``ns!ban <@usuário> <motivo>``')
	else:
		await bot.ban(member)
		embed = discord.Embed(title='usuário banido!', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário banido', value=member.name)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Você foi banido!'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Autor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que foi banido', value=ctx.message.server.name)
		embedpv.add_field(name='Motivo', value=motivo)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(member, embed=embedpv)
		print('comando ban digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
							



@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, motivo: str = None):
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``ns!kick <@usuário> <motivo>``')
	else:
		await bot.kick(user)
		embed = discord.Embed(title='usuário expulso!', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário banido', value=member.name)
		embed.add_field(name='Id', value=member.id)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Você foi expulso!'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Autor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que foi expulso', value=ctx.message.server.name)
		embedpv.add_field(name='Motivo', value=motivo)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(member, embed=embedpv)
	print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
			
@bot.command(pass_context=True)
async def serverinfo(ctx):
	embed = discord.Embed(name="{}' serverinfo".format(ctx.message.server.name), description="ns!ajuda para ver meus comandos!.", color=0x00fA00)
	embed.add_field(name="📄Nome do servidor", value=ctx.message.server.name, inline=True)
	embed.add_field(name = '👑 Dono', value = str(ctx.message.server.owner) + '\n' + ctx.message.server.owner.id);
	embed.add_field(name="💻ID do servidor", value=ctx.message.server.id, inline=True)
	embed.add_field(name="🎓Total de roles", value=len(ctx.message.server.roles), inline=True)
	embed.add_field(name="👥Total de Membros", value=len(ctx.message.server.members))
	embed.add_field(name='🌎 Região', value=ctx.message.server.region)
	embed.add_field(name='👮Role Top1', value=ctx.message.server.role_hierarchy[0])
	embed.set_footer(text ='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)
	print('comando serverinfo digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def jornal(ctx, *, msg: str=None):
	if not msg:
		return await bot.say('You Burro Men fala uma noticia ai ne ;-; Ex: ``ns!jornal <noticia>``')
	else:
		server = ctx.message.server
		jornalista = ctx.message.author
		horario = datetime.datetime.now().strftime("%H:%M | %d/%m/%y")
		canal = bot.get_channel("543836283169013760")
		jornal = discord.Embed(title='Olaaa Pessoa que não faz silencio Você Esta Assistindo o Not News!', color=0xAB00FF)
		jornal.set_author(name='Not News!')
		jornal.add_field(name='Jornalista', value=jornalista.mention)
		jornal.add_field(name='Noticia', value=msg)
	
		jornal.set_footer(text="Jornal Trasmitido Em {}".format(horario))
		await bot.send_message(canal, content="@everyone", embed=jornal)
		await bot.say('{} noticia enviada com sucesso!'.format(jornalista.mention))


@bot.command(pass_context=True)
async def f(ctx, member: discord.User):
		role = discord.utils.get(member.server.roles, name="❲🔱❳彡Founder ❰★★★★★★★★★★❱")
		await bot.remove_roles(member, role)

@bot.command(pass_context=True)
async def fn(ctx, member: discord.User):
		role = discord.utils.get(member.server.roles, name="❲🔱❳彡Founder ❰★★★★★★★★★★❱")
		await bot.remove_roles(member, role)

@bot.command(pass_context=True)
async def unmute(ctx, member: discord.User):
		role = discord.utils.get(member.server.roles, name="Silenciado")
		await bot.remove_roles(member, role)
		embed = discord.Embed(title='usuário aprendeu a falar novamente!', color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário', value=member.name)
		embed.add_field(name='Id', value=member.id)
		embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Você aprendeu a falar novamente!'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Autor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que aprendeu a falar', value=ctx.message.server.name)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(member, embed=embedpv)
		print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))


@bot.command(pass_context=True)
async def ship(ctx, user1: discord.User, user2: discord.User):
	voce = ctx.message.author.mention
	porcentagem = random.randint(10,100)
	embed = discord.Embed(title = 'Sera que essa "Shippada" vai ser o futuro?', description='"**O(A) {} Shippou {} com {}! \n Chance De Ser Verdade {}**'.format(voce, user1.mention, user2.mention))
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def mute(ctx, member: discord.User, motivo: str=None):
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``ns!mute <@usuário> <motivo>``')
	else:
		role = discord.utils.get(member.server.roles, name="Silenciado")
		await bot.add_roles(member, role)
		embed = discord.Embed(title='usuário mutado!', description='{} usuário mutado com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
	embed.add_field(name='Autor', value=ctx.message.author)
	embed.add_field(name='usuário', value=member.name)
	embed.add_field(name='Id', value=member.id)
	embed.add_field(name='Motivo', value=motivo)
	embed.set_footer(text='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
	await bot.say(embed=embed)
	embedpv = discord.Embed(title='Você foi mutado!'.format(ctx.message.author.mention), color=0xff0Ab)
	embedpv.add_field(name='Autor', value=ctx.message.author)
	embedpv.add_field(name='servidor em que foi mutado', value=ctx.message.server.name)
	embedpv.add_field(name='Motivo', value=motivo)
	embedpv.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.send_message(member, embed=embedpv)
	print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User=None):
	user = user or ctx.message.author
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando avatar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

			
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def avisar(ctx, member: discord.Member, *, content: str):
	embed = discord.Embed(description='{} foi avisado com sucesso! por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
	embedpv = discord.Embed(title='Aviso', color=0x00AB70)
	embedpv.add_field(name='Aviso Do servidor', value=ctx.message.server.name)
	embedpv.add_field(name='Autor', value=ctx.message.author)
	embedpv.add_field(name='Motivo', value=content)
	embedpv.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.send_message(member, embed=embedpv)
	
	await bot.say(embed=embed)  
	print('comando avisar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def setcargo(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.add_roles(member, role)
    embed = discord.Embed(description=' ✅Role Adicionada com sucesso!', color=0x00ff00)
    await bot.say(embed=embed)
    print('comando addrole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	


@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removecargo(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.remove_roles(member, role)
    embed = discord.Embed(description=' 👮Role removida com sucesso', color=0xff0000)
    await bot.say(embed=embed)
    print('comando removerole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))			

									
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voicemute(ctx, member: discord.Member):
    await bot.server_voice_state(member,mute=True)
    emb = discord.Embed(title='Usuário mutado voz', description='{} foi mutado com sucesso.'.format(member.mention), color=0xE57373)
    emb.set_footer(text ='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
    await bot.say(embed=emb)
    
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int=None):
	if not limit:
		return await bot.say('{} Você não definiu a quantia de mensagens para apagar'.format(ctx.message.author.mention))
	else:
		async for msg in bot.logs_from(ctx.message.channel, limit=limit):
			try:
				await bot.delete_message (msg)
			except:
				pass
				embed = discord.Embed(description="Chat Limpo por {} :smile:".format(ctx.message.author.mention), color=0x00ff00)
				embed.set_footer(text ='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))    																															
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voiceunmute(ctx, member: discord.Member):
    await bot.server_voice_state(member,mute=False)
    emb = discord.Embed(title='Usuário desmutado voz', description='{} foi desmutado com sucesso.'.format(member.mention), color=0xE57373)
    emb.set_footer(text ='Comando Realizado Por: {}| Bot Oficial и๏† - No Silent ★'.format(ctx.message.author.name))
    await bot.say(embed=emb)
    

@bot.command(pass_context = True)
async def ajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Meus Comandos')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'ns!kick ',value ='como usar ``ns!kick @usuário <motivo>`` Expulsa o usuário marcado, e notifica no privado',inline = False)
    embed.add_field(name = 'ns!mute ',value ='como usar ``ns!mute @usuário <motivo>`` Muta o usuário marcado, e notifica no privado',inline = False)
    embed.add_field(name = 'ns!serverinfo ',value ='como usar ``ns!serverinfo`` Veja As Informações do servidor atual',inline = False)
                
    embed.add_field(name = 'ns!avatar ',value ='como usar ``ns!avatar @usuário`` Veja o avatar do usuário marcado',inline = False)
    embed.add_field(name = 'ns!voicemute ',value ='como usar ``ns!voicemute @usuário`` Silencia a voz do usuário marcado',inline = False)    
                            
    embed.add_field(name = 'ns!voiceunmute ',value ='como usar ``ns!voiceunmute @usuário`` desmuta a voz do usuário marcado',inline = False)
    embed.add_field(name ='ns!unmute ',value ='como usar ``ns!unmute @usuário`` Desmuta o Usuário Marcado',inline = False)  
            
    embed.add_field(name = 'ns!ban ',value ='Como usar ``ns!ban @usuário <motivo>`` bane o usuário marcado, e notifica no privado',inline = False)
    embed.add_field(name = 'ns!setcargo ',value ='Como usar ``ns!setcargo @cargo @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = 'ns!removecargo',value ='Como usar ``ns!removecargo @cargo @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = 'ns!clear',value ='Como usar ``ns!clear`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = 'ns!avisar',value ='Como usar ``ns!avisar @usuário`` avisa um usuário no PV ',inline = False)
    embed.add_field(name = 'ns!jornal',value ='Como usar ``ns!jornal <noticia>`` De uma noticia ao servidor **Necessita de permissões** ',inline = False)

    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando help digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Meus Comandos')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'ns!kick ',value ='como usar ``ns!kick @usuário <motivo>`` Expulsa o usuário marcado, e notifica no privado',inline = False)
    embed.add_field(name = 'ns!mute ',value ='como usar ``ns!mute @usuário <motivo>`` Muta o usuário marcado, e notifica no privado',inline = False)
    embed.add_field(name = 'ns!serverinfo ',value ='como usar ``ns!serverinfo`` Veja As Informações do servidor atual',inline = False)
   
                
    embed.add_field(name = 'ns!avatar ',value ='como usar ``ns!avatar @usuário`` Veja o avatar do usuário marcado',inline = False)
    embed.add_field(name = 'ns!voicemute ',value ='como usar ``ns!voicemute @usuário`` Silencia a voz do usuário marcado',inline = False)    
                            
    embed.add_field(name = 'ns!voiceunmute ',value ='como usar ``ns!voiceunmute @usuário`` desmuta a voz do usuário marcado',inline = False)
    embed.add_field(name ='ns!unmute ',value ='como usar ``ns!unmute @usuário`` Desmuta o Usuário Marcado',inline = False)  
            
    embed.add_field(name = 'ns!ban ',value ='Como usar ``ns!ban @usuário <motivo>`` bane o usuário marcado, e notifica no privado',inline = False)
    embed.add_field(name = 'ns!setcargo ',value ='Como usar ``ns!setcargo @cargo @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = 'ns!removecargo',value ='Como usar ``ns!removecargo @cargo @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = 'ns!clear',value ='Como usar ``ns!clear`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = 'ns!avisar',value ='Como usar ``ns!avisar @usuário`` avisa um usuário no PV ',inline = False)
    embed.add_field(name = 'ns!jornal',value ='Como usar ``ns!jornal <noticia>`` De uma noticia ao servidor **Necessita de permissões** ',inline = False)

    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando help digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))        
    

bot.run(str(os.environ.get('BOT_TOKEN')))
