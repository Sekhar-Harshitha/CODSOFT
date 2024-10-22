import random
import string

def gen_password(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
        characters += digits
    if special_characters:
        characters+=special

    pwd=""

    while True:
        pwd=""
        meets_criteria=False
        has_number=False
        has_special=False

        while len(pwd)<min_length:
            new_char=random.choice(characters)
            pwd+=new_char

            if new_char in digits:
                has_number=True
            elif new_char in special:
                has_special=True

        meets_criteria =True
        if numbers:
            meets_criteria=has_number
        if special_characters:
            meets_criteria=meets_criteria and has_special

        return pwd
min_length=int(input("ENTER THE MINIMUM LENGTH: "))
while True:
    has_number_inp=input("DO YOU WANT TO INCLUDE NUMBERS (Y/N):").strip().lower()
    if has_number_inp in ['y','n']:
        has_number=has_number_inp=='y'
        break
    else:
        print("ENTER VALID INPUT (Y/N):")

while True:
    has_special_inp=input("DO YOU WANT TO INCLUDE SPECIAL CHARACTERS (Y/N):").strip().lower()
    if has_special_inp in ['y','n']:
        has_special=has_special_inp=='y'
        break
    else:
        print("ENTER VALID INPUT (Y/N):")

pwd=gen_password(min_length,has_number,has_special)
print("YOUR PASSWORD IS:",pwd)
