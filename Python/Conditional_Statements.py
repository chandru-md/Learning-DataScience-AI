"""score = 95
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")"""

"""score = 50
submitted_project = False
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 50:
    print("E")
else:
    print("F")"""

'''score = 88
submitted_project = True
if score >= 90 and submitted_project:
        print("A+")
elif score >= 90:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")'''

'''score = 50
submitted_project = True

if score >=90:
    print("Highest Score")
else:
    print("Lowest Score")

if submitted_project:
    print("Project Submitted")
else:
    print("project not submitted.")


# inline if statement
score = 50
grade = "A" if score >=90 else "B" if score>=80 else 'F'
print(grade)

# simple logic = inline if statement
# complex logic = classix if statement

country = "India"
if country == "India":
    print("IN")
elif country == "USA":
    print("USA")
elif country == "United Kingdom":
    print("UK")
elif country == "Germany":
    print("DE")
else:
    print("Unknown Country")

match country:
    case "India" | "IND":
        print("IN")
    case "USA" | "United States":
        print("US")
    case "United Kingdom" | "UK":
        print("UK")
    case "Germany" | "DE":
        print("DE")
    case _:
        print("Unknown Country")


# task-email
email = input("Enter your email: ").strip().lower()
if email == "":
    print("Invalid email")
elif not ("@" in email and "." in email):
    print("Email must contain @ and .")
elif email.count('@')!=1:
    print("Email must contain only one @")
elif not email.endswith((".com",".org",".net")):
    print("Email must end with .org, .net or .com")
elif len(email) > 254:
    print("Email is too long")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with an alphanumeric character")
else:
    print("Email is valid")


# task-email
email = input("Enter your email: ").strip().lower()
valid = True
if email == "":
    print("Invalid email")
    valid = False
if not ("@" in email and "." in email):
    print("Email must contain @ and .")
    valid = False
if email.count('@')!=1:
    print("Email must contain only one @")
    valid = False
if not email.endswith((".com",".org",".net")):
    print("Email must end with .org, .net or .com")
    valid = False
if len(email) > 254:
    print("Email is too long")
    valid = False
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with an alphanumeric character")
    valid = False
if valid:
    print("Email is valid")
'''


def validate_password(password: str, email: str) -> bool:
    # 1. Must not be empty
    if password == "":
        return False
    else:
        # 2. Must be at least 8 characters
        if len(password) < 8:
            return False
        else:
            # 3. Must include at least 1 uppercase
            has_upper = False
            for ch in password:
                if ch.isupper():
                    has_upper = True
                    break
            if not has_upper:
                return False
            else:
                # 4. Must include at least 1 lowercase
                has_lower = False
                for ch in password:
                    if ch.islower():
                        has_lower = True
                        break
                if not has_lower:
                    return False
                else:
                    # 5. Must not be same as the email
                    if password == email:
                        return False
                    else:
                        # 6. Must not contain any spaces
                        has_space = False
                        for ch in password:
                            if ch == " ":
                                has_space = True
                                break
                        if has_space:
                            return False
                        else:
                            # 7. Must start and end with a letter or digit
                            if (password[0].isalnum() and password[-1].isalnum()):
                                return True
                            else:
                                return False
                            

validate_password("1547845298@#$kathirchandran", "chandrumd@gmail.com")