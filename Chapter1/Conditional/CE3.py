try:
    scoreg = float(input("Enter Score:"))
except:
    print("Bad Score")

if score>1.0 or score<0:
    print("Bad Score");
else:
    if score>=0.9:
        print("A");
    elif score>=0.8:
        print("B");
    elif score>=0.7:
        print("C");
    elif score>=0.6:
        print("D");
    else:
        print("F");
