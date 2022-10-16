import random

WIN_POINT = 100

# Ladder : Jump forward to some point
LADDER = {
    10: 31,
    20: 42,
    45: 78,
    70: 98
}
# Snake : Jump downward to some point
SNAKE = {
    30: 2,
    50: 21,
    68: 46,
    72: 55,
    89: 72
}


def check_snake(prev_pos, dice):
    new_pos = prev_pos + dice
    if new_pos <= WIN_POINT:
        snake = SNAKE.get(new_pos)
        if snake:
            print("you get a snake, so you have to move downward")
            return snake
        else:
            return new_pos
    return prev_pos


def check_ladder(prev_pos, dice_value):
    new_pos = prev_pos + dice_value
    if new_pos <= WIN_POINT:
        ladder = LADDER.get(new_pos)
        if ladder:
            print("you get a ladder, so you have to move forward")
            return ladder
        else:
            return new_pos
    return prev_pos


def check_win(new_pos):
    return new_pos == WIN_POINT


def play(prev_pos):
    dice = throw_dice()
    is_snake = check_snake(prev_pos, dice)
    if is_snake < prev_pos:  # if snake return snake value
        return is_snake
    is_ladder = check_ladder(prev_pos, dice)  # if snake do not check for ladder / if ladder return ladder value
    i_won = check_win(is_ladder)  # if snake or ladder is there a win call

    if i_won:
        return -1
    return is_ladder


def throw_dice():
    return random.randint(1, 6)


def main():
    player1 = 0
    player2 = 0

    while True:
        player1 = play(player1)
        if player1 == -1:
            print('player1 won')
            break
        player2 = play(player2)
        if player2 == -1:
            print('player2 won')
            break


print("Welcome to snake and ladder game!!!")
if __name__ == "__main__":
    main()
