def generate_password(n):
    password = ""
    if n <= 10:
        i = 1
        j = n - 1
        while i <= j:
            password += str(i)
            if i != j:
                password += str(j)
            i += 1
            j -= 1
    else:
        for i in range(1, n // 2 + 1):
            password += str(i)
            password += str(n - i)
        if n % 2 != 0:
            password += str(n // 2 + 1)
    return password


for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - {result}")
