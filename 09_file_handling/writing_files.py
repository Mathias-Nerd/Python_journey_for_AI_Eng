with open("demofile.txt", "a") as f:
    print("Initial content:")
    f.write("I am an aspiring Tech Polymath")

m = open("demofile.txt", "r")     
print(m.read())

