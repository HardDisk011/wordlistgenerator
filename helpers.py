import random
import time

def genera_stringa(chars, length):
    return "".join(random.choice(chars) for _ in range(length))

def logo():
    chars = [
            " __    __              _ _ _     _                                     _              \n"
            "/ / /\ \ \___  _ __ __| | (_)___| |_    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ \n"
            "\ \/  \/ / _ \| '__/ _` | | / __| __|  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|\n"
            " \  /\  / (_) | | | (_| | | \__ \ |_  | (_| |  __/ | | |  __/ | | (_| | || (_) | |   \n"
            "  \/  \/ \___/|_|  \__,_|_|_|___/\__|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   \n"
            "                                       |___/                                         \n"
            "               Random password generator of different lengths V1.0\n"
            "                   Github: HardDisk011   Instagram: die_go.011\n"
    ]
    for row in chars:
        print(row)
        time.sleep(0.1)
