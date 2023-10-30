days_for_checkups = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, days_for_checkups + 1):
    patients_for_the_day = int(input())
    untreated_patients_today = 0

    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1

    if patients_for_the_day <= doctors:
        treated_patients += patients_for_the_day
    else:
        treated_patients += doctors
        untreated_patients += (patients_for_the_day - doctors)


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
