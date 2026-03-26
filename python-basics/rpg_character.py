full_dot = "●"
empty_dot = "○"


def create_character(char_name, strength, intelligence, charisma):
    sum = intelligence + strength + charisma
    if type(char_name) != str:
        return "The character name should be a string"
    elif char_name == "":
        return "The character should have a name"
    elif len(char_name) > 10:
        return "The character name is too long"
    elif char_name.count(" ") != 0:
        return "The character name should not contain spaces"
    elif type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    elif intelligence < 1 or strength < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif intelligence > 4 or strength > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif sum != 7:
        return "The character should start with 7 points"
    else:
        str_dot_amount = full_dot * strength
        int_dot_amount = full_dot * intelligence
        cha_dot_amount = full_dot * charisma

        str_empty_dot_amount = empty_dot * (10 - str_dot_amount.count("●"))
        int_empty_dot_amount = empty_dot * (10 - int_dot_amount.count("●"))
        cha_empty_dot_amount = empty_dot * (10 - cha_dot_amount.count("●"))

        return f"{char_name}\nSTR {str_dot_amount}{str_empty_dot_amount} \nINT {int_dot_amount}{int_empty_dot_amount}\nCHA {cha_dot_amount}{cha_empty_dot_amount}"


print(create_character("coolguy", 4, 2, 1))
