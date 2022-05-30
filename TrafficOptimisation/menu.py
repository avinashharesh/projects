print("Traffic Optimisation\n1.Constant\n2.Dynamic\n3.70%")
ch = input("Enter the choice:")
if ch == '1':
    exec(open('constant.py').read())
elif ch == '2':
    exec(open('dynamic.py').read())
elif ch=='3':
    exec(open('70%.py').read())
else:
    print("Invalid Choice")
