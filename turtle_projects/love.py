import qrcode 
data = '''Anjali !!! I love you not because you are the girl who impressed me but because you the girl who make me feel live daily and gives me a strength to become a good person daily. !!!
You the sweetest hello of my life and hardest goodbyee...I know sometimes i might sound boring and might not match the same vibe but one thing i can assure that no one else can love you the way i do and you complaint about me making you priority but if you were me then you have understood that special you are for me... !!!
I love you my sweet little cutu mouseyyy....Love you till death...'''
img =qrcode.make(data=data)
img.save("secret message.png")