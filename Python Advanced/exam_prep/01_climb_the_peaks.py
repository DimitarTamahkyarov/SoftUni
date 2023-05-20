from collections import deque

food_portions = deque([int(num) for num in input().split(", ")])
daily_stamina = deque([int(num) for num in input().split(", ")])

mountain_peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

conquered_peaks = []

for peak, diff in mountain_peaks.items():
    try:
        energy = food_portions.pop() + daily_stamina.popleft()
    except IndexError:
        energy = 0

    if energy >= diff:
        conquered_peaks.append(peak)
    else:
        while energy < diff and food_portions and daily_stamina:
            energy = food_portions.pop() + daily_stamina.popleft()

            if energy >= diff:
                conquered_peaks.append(peak)

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)