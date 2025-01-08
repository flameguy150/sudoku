import winsound

for i in range(2):
    winsound.Beep(262 * (i+1), 1000)
    winsound.Beep(330 * (i+1), 1000)
    winsound.Beep(392 * (i+1), 1000)
    winsound.Beep(494 * (i+1), 1000)

