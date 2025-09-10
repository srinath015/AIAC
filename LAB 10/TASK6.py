def grade(score):
    return "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

print(grade(85))
print(grade(92))
print(grade(75))
print(grade(60))
print(grade(50))
print(grade(100))
