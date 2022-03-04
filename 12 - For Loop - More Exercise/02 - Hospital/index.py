period = int(input())

doctors = 7
revised_patients = 0
not_revised_patients = 0
count_days = 0

for i in range(period):
    patients = int(input())

    count_days += 1
    if count_days % 3 == 0:
        if not_revised_patients > revised_patients:
            doctors += 1

    diff = abs(patients - doctors)

    if patients <= doctors:
        revised_patients += patients
    elif patients > doctors:
        revised_patients += doctors
        not_revised_patients += diff

print(f"""Treated patients: {revised_patients}.
Untreated patients: {not_revised_patients}.""")