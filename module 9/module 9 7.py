def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print('Составное число')
                    return result
                else:
                    print('Простое число')
                    return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


print(sum_three(2, 3, 6))
print(sum_three(7, 8, 9))
print(sum_three(11, 13, 17))
