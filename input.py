volume = int(input('Enter your volume: '))

def volFunc():
#volume = 57
	if volume < 20:
  	 print("It's kinda quiet.")
	elif 20 <= volume < 40:
   	 print("It's nice for background music")
	elif 40 <= volume < 60:
   	 print("Perfect, I can hear all the details")
	elif 60 <= volume < 80:
   	 print("Nice for parties")
	elif 80 <= volume < 100:
		print("Volume is " + str(volume))
	else:
   		print("My ears are hurting! Volume is " + str(volume) + " DB")

volFunc()

name = input('Enter your name: ')
def hi1(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')
girlz=name
hi1(name)

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You', girlz]
for name in girls:
    hi(name)
    print('Next girl')