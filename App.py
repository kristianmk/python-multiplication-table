# Written by K. M. Knausgård 2021-09-23
import itertools
import random
import time
import phue as hue

max_number_of_exercises = 100

enable_hue = True
hue_bridge_ip = '10.0.0.169'
hue_light_name = 'Stue ved skyvedør høyre'


def input_integer_number(message):
    while True:
        try:
            return int(input(message))
        except:
            pass


# Color space conversion from phue github https://github.com/studioimaginaire/phue/blob/master/examples/rgb_colors.py
def rgb_to_xy(red, green, blue):
    """ conversion of RGB colors to CIE1931 XY colors
    Formulas implemented from: https://gist.github.com/popcorn245/30afa0f98eea1c2fd34d
    Args:
        red (float): a number between 0.0 and 1.0 representing red in the RGB space
        green (float): a number between 0.0 and 1.0 representing green in the RGB space
        blue (float): a number between 0.0 and 1.0 representing blue in the RGB space
    Returns:
        xy (list): x and y
    """

    # gamma correction
    red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
    green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
    blue = pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)

    # convert rgb to xyz
    x = red * 0.649926 + green * 0.103455 + blue * 0.197109
    y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    z = green * 0.053077 + blue * 1.035763

    # convert xyz to xy
    x = x / (x + y + z)
    y = y / (x + y + z)

    return [x, y]


def connect_hue_bridge():

    while True:
        try:
            hb = hue.Bridge(hue_bridge_ip)
            hb.connect()
            return hb
        except hue.PhueRegistrationException as pre:
            print("\nPlease connect to Philips Hue bridge before first use.")
            print("Set Hue Bridge IP address and light name for the light to be controlled.")
            print("Also put light in color-mode in your Hue-app.")
            print("\nIf this is OK, press the button on you Hue bridge now, and within 30 s hit ENTER.")
            print("\nNo Hue light available? Set enable_hue to False to get rid of this!")
            input("Press ENTER to continue...")
            print("\n")
        except Exception as e:
            print("Unknown error occurred..")
            print("\nNo Hue light available? Set enable_hue to False to get rid of this!")
            quit(0)


def main():
    print("Python Multiplication Table Learner 1.0\n")

    if enable_hue:
        hb = connect_hue_bridge()
        origxy = hb.get_light(hue_light_name, 'xy')

    message = "Select number of exercises, maximum {}:   ".format(max_number_of_exercises)

    number_of_exercises = min(input_integer_number(message), max_number_of_exercises)
    print("\n  Ready!")

    exercises = list(itertools.product(range(0, 10), repeat=2))
    random.shuffle(exercises)

    for ii, exercise in enumerate(exercises[:number_of_exercises]):
        print("\n  Exercise number {} of {}:".format(ii + 1, number_of_exercises))
        answer = input_integer_number("    {} x {} = ".format(exercise[0], exercise[1]))
        while answer != (exercise[0] * exercise[1]):
            # command = {'bri': 254, 'hue': 8042, 'sat': 174}
            hb.set_light(hue_light_name, 'xy', rgb_to_xy(1.0, 0, 0), transitiontime=5)
            print("    Wrong!")
            time.sleep(1)
            hb.set_light(hue_light_name, 'xy', origxy, transitiontime=50)
            answer = input_integer_number("    {} x {} = ".format(exercise[0], exercise[1]))
        hb.set_light(hue_light_name, 'xy', rgb_to_xy(0.0, 1.0, 0), transitiontime=5)
        print("    CORRECT!")
        time.sleep(1)
        hb.set_light(hue_light_name, 'xy', origxy, transitiontime=50)


if __name__ == "__main__":
    main()
