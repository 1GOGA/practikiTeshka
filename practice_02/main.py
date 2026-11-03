def energy_per_day(kwh, days):
    if days == 0:
        return 'Нельзя делить'
    return kwh / days

assert energy_per_day(56,7) == 8
assert energy_per_day(56,0) == 'Нельзя делить'
assert energy_per_day(100,10) == 10
print(energy_per_day(56,7))


words = ["ход", "партия", "чемпионат"]
s_sortom = sorted(words, key= lambda word: len(word))
print(s_sortom)