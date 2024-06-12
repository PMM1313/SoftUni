def validate_password(password):
    def has_sufficient_length(password):
        return 6 <= len(password) <= 10

    def has_only_letters_and_digits(password):
        return password.isalnum()

    def has_at_least_two_digits(password):
        digit_count = sum(1 for char in password if char.isdigit())
        return digit_count >= 2

    if not has_sufficient_length(password):
        print("Password must be between 6 and 10 characters")

    if not has_only_letters_and_digits(password):
        print("Password must consist only of letters and digits")

    if not has_at_least_two_digits(password):
        print("Password must have at least 2 digits")

    if (has_sufficient_length(password) and
            has_only_letters_and_digits(password) and
            has_at_least_two_digits(password)):
        print("Password is valid")


password = input()
validate_password(password)