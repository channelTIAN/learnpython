# -*- conding: utf-8 -*-

def SayHello(name):
	print("hello,", name)
	print("this is your first git program\nWelcome!!")
	
def Congratulate(name):
	print(name, "Congratulation, you start you first step, Come on!!")

if __name__ == "__main__":
	print("Please input your name:")
	name = input()
	print("\n")
	SayHello(name)
	Congratulate(name)