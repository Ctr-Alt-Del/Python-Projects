def age_converter():
    age = input("Enter your age in years: ")
    age_seconds = int(age) * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")
age_converter()