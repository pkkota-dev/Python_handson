import winreg

CONFIG_PATH = r'SOFTWARE\WOW6432Node\NVIDIA Corporation\Installed Products\Nsight\Visual Studio'

configured_config = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, CONFIG_PATH,0, winreg.KEY_READ)
config_value = winreg.QueryValueEx(configured_config, 'CurrentVersion')
print(config_value)

test_path= CONFIG_PATH + '\\'  + config_value[0]
get_test_key= winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, test_path, 0, winreg.KEY_WRITE)

dest_value = input('Please Enter the Value you wanted to update')
get_test_key_value =  winreg.SetValueEx(get_test_key,'Test',0, winreg.REG_SZ, dest_value)
print('Modified Registry Path',  test_path, end=" ")
print('Get/Set Registry value', get_test_key_value)
