def generate_password(n):
    result = ""


    for i in range(1, n):

        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += f"{i}{j}"

    return result


n = 13
password = generate_password(n)
print(f"Сгенерированный пароль для n = {n}: {password}")

