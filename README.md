## **Kivy Python C Extension Template**
For Detailed Breakdown see, [Documentation](https://kivy-python-c-extension.readthedocs.io/en/latest/)

 **TL;DR**
 
 1. *[A simple C Extension](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/custom_lib/custom_lib/custom_module.c) to return a string*
 2. ***Build** it using [setup.py](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/custom_lib/setup.py) / [setup.cfg](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/custom_lib/setup.cfg)*
 3. [**Import** C Extension](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/main.py#L4) in Kivy / Python
 4. ***Create** a simple Recipe for Compiled Component for Buildozer / P4A*
 5. **Edit** Buildozer :
	

	> #In [Requirements](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/buildozer.spec#L39) make sure to mention the **C Extension Module**<br>
	> `requirements = python3,kivy,custom_lib`<br><br>
	> #Specify the path for the [setup.py](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/custom_lib/setup.py) / [setup.cfg](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/custom_lib/setup.cfg) for **local C Extension Module**<br>
	> `requirements.source.custom_lib = ./custom_lib/`<br><br>
	> #Specify the path for [Recipe](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/python-for-android/recipe/custom_lib/__init__.py) for **local C Extension Module**<br>
	> `p4a.local_recipes = ./python-for-android/recipe`
	
	are the main ones to edit based on the paths in buildozer.spec
	

 6. [**Build**](https://github.com/VICTORVICKIE/Kivy_Python_C_Extension_Demo/blob/main/bin/Py_C_Extension_Demo.apk) with `buildozer android debug deploy run logcat`
 

&nbsp;&nbsp;&nbsp;&nbsp;****Note : I've used custom ndk, sdk paths in spec file****
