import os
for root, dirs, files in os.walk("./Data/2021-04-01_235959", topdown=False):
   for name in files:
      print((os.path.join(root, name)))
   print("------------------")
   for name in dirs:
      print(os.path.join(root, name))