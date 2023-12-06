from input_data import input_data


def calc_race_distance(total_time, button_press: int) -> int:
    speed = button_press
    remaining_time = total_time - button_press
    return remaining_time * speed


def calc_won_races(total_time, winning_distance) -> int:
    won_races = 0
    for i in range(total_time + 1):
        if calc_race_distance(total_time, i) > winning_distance:
            won_races += 1
    return won_races


def task1():
    result = 1
    for dataset in input_data:
        total_time = dataset["time"]
        winning_distance = dataset["distance"]
        result *= calc_won_races(total_time, winning_distance)
    return result


print(task1())
print(calc_won_races(51926890, 222203111261225))
