print("Traffic Optimisation\n1.Constant\n2.Dynamic\n")
ch = input("Enter the choice:")
if ch == '1':
    exec(open('constant.py').read())
elif ch == '2':
    exec(open('dynamic.py').read())
else:
    print("Invalid Choice")
