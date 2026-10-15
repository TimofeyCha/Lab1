from config import CSI, RESET, ZERO
import time
import os


BLACK = 40
WHITE_B = 47
WHITE_F = 37
RED_256 = 196
BLUE_256 = 21
WHITE_256 = 15


def draw_flag(RED, WHITE, BLUE, k):
    color_list = [BLUE, WHITE, RED]

    for line in range(2 * k):
        for part in range(len(color_list)):
            print(
                f"{CSI}48;5;{color_list[part]}m{' '*2*k}",
                end="", flush=True
            )

        print(RESET)


def draw_ornament(count_lines, count_columns):
    for line in range(count_lines):
        stroka = ""

        for column in range(count_columns):
            if line % 2 != 0:
                if column % 2 != 0:
                    stroka += f"{CSI}{BLACK}m  {RESET}"
                else:
                    stroka += f"{CSI}{WHITE_B}m  {RESET}"
            else:
                if column % 2 == 0:
                    stroka += f"{CSI}{BLACK}m  {RESET}"
                else:
                    stroka += f"{CSI}{WHITE_B}m  {RESET}"

        print(stroka)


def draw_rocket():
    SCREEN_HEIGHT = 20

    os.system("cls")

    y = -4
    rocket = [f" {CSI}{WHITE_F}mV{RESET} ", f"{CSI}{WHITE_B}m   {RESET}",
              f"{CSI}{WHITE_F}m\\{CSI}{WHITE_B}m {RESET}/{RESET}",
              f" {CSI}{WHITE_F}mV{RESET} "]

    while True:
        screen = ["   " for x in range(SCREEN_HEIGHT)]

        for i in range(len(rocket)):
            if 0 <= i + y < SCREEN_HEIGHT:
                screen[i + y] = rocket[i]

        print("\n".join(screen), end="", flush=True)
        print(f"{CSI}{SCREEN_HEIGHT}A{ZERO}", end="", flush=True)

        y += 1

        if y > SCREEN_HEIGHT:
            y = -len(rocket)

        time.sleep(0.1)


def draw_function(WIDTH=10):

    print('^')
    for y in range(WIDTH):
        print('|')
    print("0" + "--" * WIDTH + '>', end="")

    y = x = 0

    print(f"{ZERO}", end="")

    for x in range(1, 10):
        print(f"{CSI}1C", end="")
        if x**2 <= WIDTH:
            print(f"{CSI}{x**2}A*{CSI}{x**2}B{CSI}{1}D", end="", flush=True)


def draw_diagram():
    with open('lab1/sequence.txt') as seq:
        neg_nums = [float(x) for x in seq if float(x) < 0]
        seq.seek(0)
        pos_nums = [float(x) for x in seq if float(x) > 0]

    part_neg_nums = len(neg_nums)/(len(neg_nums) + len(pos_nums)) * 100
    part_pos_nums = len(pos_nums)/(len(neg_nums) + len(pos_nums)) * 100

    print(f"{CSI}48;5;{BLUE_256}m{' ' * int(len(neg_nums) / 5)}{RESET}",
          f"{part_neg_nums}% - числа < 0")
    print(f"{CSI}48;5;{RED_256}m{' ' * int(len(pos_nums) / 5)}{RESET}",
          f"{part_pos_nums}% - числа > 0")


# draw_flag(RED_256, WHITE_256, BLUE_256, 5)
# draw_ornament(50,100)
draw_rocket()
# draw_diagram()
# draw_function(16)
