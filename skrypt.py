print('Hello, Django girls!')
print('Hello, Dawidesz!')
print('Jest spoko!')
print('Jest SIŁA')
if 3 > 2:
	print('to działa!')
if 5 > 2:
	print('5 jest jednak większe od 2')
else:
	print ('5 nie jest większe od 2')
glosnoscstr = input('podaj glosnosc')
glosnosc = int(glosnoscstr)
if glosnosc < 20:
	print("Prawie nic nie słychać")
elif 20 <= glosnosc < 40:
	print("o, muzyka leci w tle")
elif 40 <= glosnosc < 60:
	print("jest okej, słyszę coś")
elif 60 <= glosnosc <80:
	print("dobre na imprezy")
elif 80 <= glosnosc <100:
	print("Za głośno!")
else:
	print ("moje uszy! Ała!!!:(")
def hej():
	print('Hej!')
	print('Jak się masz?')
hej()
	