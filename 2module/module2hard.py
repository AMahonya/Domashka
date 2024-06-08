def faind_result(n):
    result = []
    for i in range(1,n):
        for j in range(i+1,n):
            if n % ((i + j)) == 0:
                pas_n = str(i) + str(j)
                result.append(pas_n)
    return result

while True:

    n = int(input("Enter a number from 3 to 20"))
    if n == 0:
        break
    elif 3 <= n <= 20:
        res = (faind_result(n))
        print(f"{n} --> {''.join(res)}")
    else:
        print("Error: Enter a number from 3 to 20")
        print("-----------------------------------")
        print("Stop the program enter -0-")

