import ctypes

user_handle = ctypes.WinDLL("User32.DLL") # Handle to User32.dll
k_handle = ctypes.WinDLL("Kernel32.dll") # Handle errors

hWnd = None #Not Used
lpText = "Hello World" 
lpCaption = "Hello Students" #if NONE, error message is shown
uType = 0x00000001 #type of buttons

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType) #variable for parameters

error = k_handle.GetLastError()
if error != 0:
    print("Error Code: (0)".format(error))
    exit(1)

if response == 1:
    print("User clicked ok!")
elif response == 2:
    print("User clicked cancel!")