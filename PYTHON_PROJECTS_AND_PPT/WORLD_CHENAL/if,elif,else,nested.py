print("Exam Result !")
marks = int(input("Enter marks :"))
if 35 <= marks <=100:
    print("This exam pass !")
    if 35 >=marks >= 45:
        print(marks,"D")
    elif 46 >= marks <=60:
        print(marks,"C")
    elif 61<= marks <= 79:
        print(marks,"B")
    elif 80>= marks <= 100:
        print(marks,"A")
elif marks<=34:
    print("This a exam faild")
else:
    print("invald ")

# ---------------------------------------------------------------------------------------------------------------------------------------------------






