# -*- conding: utf-8 -*-

def SayHello(name):
	print("hello,", name)
	print("this is your first git program\nWelcome!!")
	
def Congratulate(name):
	print(name, "Congratulate!!")

if __name__ == "__main__":
	print("Please input your name:")
	name = input()
	SayHello(name)
	Congratulate(name)