Input= ["ai", "ml", "python", "ml", "dl", "ai"]
Input_b= set(Input)
for i in Input_b:
    if Input.count(i) > 1:
        print(i)