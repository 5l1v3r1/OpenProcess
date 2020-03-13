# opening a simple process handle with the windows api
# author: size_t

import ctypes

# getting a handle to kernel32.dll
k_handle = ctypes.WinDLL("Kernel32.dll") 

# handling access rights
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF ) 	

#setting up the parameters
dwDesiredAcess = PROCESS_ALL_ACCESS 	
bInheritHandle = False 		 
dwProcessId = 0x37E8 	#replace this with your own	process ID (use a decimal to hex converter)

# calling the windows api call
response = k_handle.OpenProcess(dwDesiredAcess, bInheritHandle, dwProcessId)  

# printing out the process handle to the cli 
print(response) 

# handling any errors (not enough permissions etc)
error = k_handle.GetLastError()		
if error != 0:
	print("error code: (0)".format(error))
	exit(1)
	
# printing cli response to see if we have a valid handle
if response <= 0: 							
	print("Handle was not created")
else: 
	print("Handle was created")