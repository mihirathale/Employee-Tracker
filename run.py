import subprocess
import os
import sys

networks = subprocess.check_output("ipconfig", shell=True) # Get the 'ifconfig' output

port = "8000" # Set the port as 8000 by default
if len(sys.argv) > 1:
	port = sys.argv[1]  # Or use the port number given as the argument

for net in networks:
        try:
                print('Hey')
                ip = str(net).strip().split('inet')[1].strip().split(' ')[0]
                # Extract the IP address
                        
                print ("* Trying to run server at http://%s:%s/\n" % (ip, port))
		os.system("python manage.py runserver %s:%s" % (ip, port))
		# Finally run the command to start the server
	except IndexError: 
		continue
