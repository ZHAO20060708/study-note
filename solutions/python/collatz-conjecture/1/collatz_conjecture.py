def steps(number):
    steps_count = 0
    if number <=0:
        raise ValueError("Only positive integers are allowed")
    else:
        if number == 1:
            return 0
        if number % 2 == 0:
            steps_count = steps_count + 1
            return 1 + steps(number // 2)
        else:
            steps_count = steps_count + 1
            return 1 + steps(3 * number + 1)
