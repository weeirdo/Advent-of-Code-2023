# advent of code day 6

import math

times = [47, 70, 75, 66]
distances = [282, 1079, 1147, 1062]

def etaisyys(latausaika: int, vertailuaika: int):
    aika_kaynnissa = vertailuaika - latausaika
    return aika_kaynnissa * latausaika

print(etaisyys(3, times[0]))

for distance in distances:
    for i in range(len(times)):
        mun = etaisyys(i, times)
        if distance < mun:
            print(f"voitto, {mun} vs {distance}")
        else:
            print(":()")
