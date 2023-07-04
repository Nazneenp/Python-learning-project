def check_password_strength(password):
    char_lengh= len(password)>=8
    char_uppercase = False
    char_lowercase = False
    char_digits = False
    char_special = False

    if char_lengh:
        for char in password :
            if char.isupper():
                char_uppercase = True
            elif  char.islower():
                char_lowercase = True
            elif char.isdigit():
                char_digits = True
            elif not(char.isalnum()):
                char_special = True 

        result = [char_lengh,char_uppercase,char_lowercase,char_digits,char_special]
        if all(result):
            return 'strong password'
        elif char_lengh and (char_uppercase or char_lowercase ) and char_digits:
            return ' medium password'
        else:
            return 'weak password'
    else:
        return 'password lenght is less than 8'
password = input('Enter a password: ')
result = check_password_strength(password)
print('password strenght:',result)
    
    
         
    
