import discord
from discord.ext import commands
from room_checker import *
import random
import os
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

para=500
evcil_hayvan="-"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def room_check(ctx):
    await ctx.send("Odanın fotografını yolla!")
    await ctx.send('Algılama başladı!')

    if ctx.message.attachments:
        await ctx.send("Resim bulundu")

        for attachment in ctx.message.attachments:

            file_name = attachment.filename
            file_path = f"images/{file_name}"

            await attachment.save(file_path)
            await ctx.send("Resim kaydedildi")

            class_name,score = room_check("converted_keras\keras_model.h5", file_path, "converted_keras\labels.txt")

            if class_name == "messy room":
                await ctx.send("""Odan malesef temiz değil. Odanızı temizlemek için şunları yapabilirsin:
                                   
                                   -Yerde orada olmaması gereken şeyler gördüğünüzde onları oradan kaldırmaya üşenmeden kaldırmak.
                                   -Yatağınızın kullanmadığınız zamanlarda derli ve toplu olması.
                                   -Kendinizi kirli ve düzensiz değil, düzenli ve tertemiz bir odaya alıştırmak.
                                  
                                  Bu tavsiyelerle sağlığınızı ve odanızı iyileştirebilirsin!""")
            
            elif class_name == "non-messy room":
                await ctx.send("Temizlik konusunda çok iyisin!")

@bot.command()
async def info(ctx):
    await ctx.send("""Düzenli bir odada yaşamanın birçok faydası vardır, bu faydalardan bazıları:
                       -Düzenli bir odada daha rahat konsantre oluruz.
                       -Düzenli bir odada gözümüz daha az yorulur.
                       -Düzenli bir odada daha ferah hissederiz.
                       -Düzenli bir oda sağlığımızı korumamıza yardımcı olur.
                       
                       Düzenli bir oda ile çok daha rahat, temiz ve ferah bir yaşama sahip oluruz.    """)
    
    good_room_list=os.listdir("images")
    img_room=random.choice(good_room_list)
    with open(f"images/{img_room}", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def q1(ctx):
    with open(f"images_q\q1.jpg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

    @bot.command()
    async def a1(ctx,answer):
        if answer=="temiz" or "Temiz":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q2(ctx):
    with open(f"images_q\q2.jpeg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a2(ctx,answer):
        if answer=="pis" or "Pis":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q3(ctx):
    with open(f"images_q\q3.jpg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a3(ctx,answer):
        if answer=="pis" or "Pis":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q4(ctx):
    with open(f"images_q\q4.jpeg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a4(ctx,answer):
        if answer=="temiz" or "Temiz":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def q5(ctx):
    with open(f"images_q\q5.jpeg", "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
    @bot.command()
    async def a5(ctx,answer):
        if answer=="temiz" or "Temiz":
            await ctx.send("Doğru cevap!")
        else:
            await ctx.send("Yanlış cevap!")

@bot.command()
async def kumar(ctx):
    print("Kumar türünü seç.(mini[25p] / orta[50p] / buyuk[100p] / en_buyuk[300p])")
    
    @bot.command()
    async def mini(ctx,kumar):
        para -= 25
        number_1=random.randint(1,7)
        number_2=random.randint(1,7)
        number_3=random.randint(1,7)
        if number_1 != number_2 or number_1 != number_3:
            print(number_1, number_2, number_3)
            print("Kaybettin!")
        if number_1 == number_2 and number_1 == number_3:
            print(number_1, number_2, number_3)
            print("Kazandın! Harcadığın parayı iki katı olarak geri aldın!")
            para+=75
    
    @bot.command()
    async def orta(ctx,kumar):
        para-=50
        number_1=random.randint(1,7)
        number_2=random.randint(1,7)
        number_3=random.randint(1,7)
        if number_1 != number_2 or number_1 != number_3:
            print(number_1, number_2, number_3)
            print("Kaybettin!")
        if number_1 == number_2 and number_1 == number_3:
            print(number_1, number_2, number_3)
            print("Kazandın! Harcadığın parayı iki katı olarak geri aldın!")
            para+=150
    
    @bot.command()
    async def buyuk(ctx,kumar):
        para-=100
        number_1=random.randint(1,7)
        number_2=random.randint(1,7)
        number_3=random.randint(1,7)
        if number_1 != number_2 or number_1 != number_3:
            print(number_1, number_2, number_3)
            print("Kaybettin!")
        if number_1 == number_2 and number_1 == number_3:
            print(number_1, number_2, number_3)
            print("Kazandın! Harcadığın parayı iki katı olarak geri aldın!")
            para+=300
    @bot.command()
    async def en_buyuk(ctx,kumar):
        para-=300
        number_1=random.randint(1,7)
        number_2=random.randint(1,7)
        number_3=random.randint(1,7)
        if number_1 != number_2 or number_1 != number_3:
            print(number_1, number_2, number_3)
            print("Kaybettin!")
        if number_1 == number_2 and number_1 == number_3:
            print(number_1, number_2, number_3)
            print("Kazandın! Harcadığın parayı iki katı olarak geri aldın!")
            para+=150
@bot.command()
async def petshop(ctx):
    print("Dükkana hoş geldin! Ne satın almak istersin?(dog[75p] / cat[75p] / hamster[50p])")

    @bot.command()
    async def dog(ctx,petshop):
        para-=75
        print("Tebrikler! Artık bir köpeğiniz var.")
        evcil_hayvan="köpek"
    
    @bot.command()
    async def cat(ctx,petshop):
        para-=75
        print("Tebrikler! Artık bir kediniz var.")
        evcil_hayvan="kedi"
    @bot.command()
    async def hamster(ctx,petshop):
        para-=50
        print("Tebrikler! Artık bir hamsterınız var.")
        evcil_hayvan="hamster"

@bot.command()
async def pet_check(ctx):
    print(evcil_hayvan)

@bot.command()
async def para_check(ctx):
    print(para)

@bot.command()
async def tas_kagıt_makas(ctx):
    seninpuanin=0
bilgisayarpuani=0
while True:
    sen=input("Birini seçiniz taş, kağıt, makas: ")
    
    if sen=="taş" or sen=="makas" or sen=="kağıt":
        bilgisayar=random.randint(1,3)
        
        if bilgisayar ==1:
            bilgisayar="taş"
        
        elif bilgisayar==2:
            bilgisayar="kağıt"
        else:
            bilgisayar="makas"
        
        print("Taş, kağıt, makas")
        time.sleep(2)
        print("1")
        time.sleep(2)
        print("2")
        time.sleep(2)
        print("3")
        time.sleep(2)
        print("Bilgisayarın seçimi", bilgisayar)
        
        if bilgisayar==sen:
            print("Berabere")
        
        elif sen=="taş" and bilgisayar=="makas":
            print("Sen kazandın")
            seninpuanin=seninpuanin+1
        
        elif sen=="kağıt" and bilgisayar=="taş":
            print("Sen kazandın")
            seninpuanin=seninpuanin+1
        
        elif sen=="makas" and bilgisayar=="kağıt":
            print("Sen kazandın")
            seninpuanin=seninpuanin+1
        
        else:
            print("Kaybettin")
            bilgisayarpuani=bilgisayarpuani+1
        print("Şu anki puan durumu: Oyuncu ", seninpuanin, "Bilgisayar:", bilgisayarpuani)
    
    else:
        print("Böyle bir seçenek yok.Tekrar dene.")

bot.run("token")
