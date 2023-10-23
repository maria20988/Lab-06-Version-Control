



def encode_password(password_encoded):
    pass_encoded = ""
    for digit in password_encoded:
        digit_int = int(digit)
        if digit_int == 7:
            new_digit = 0
            pass_encoded += str(new_digit)
        elif digit_int == 8:
            new_digit = 1
            pass_encoded += str(new_digit)
        elif digit_int == 9:
            new_digit = 2
            pass_encoded += str(new_digit)
        else:
            new_digit = digit_int
            new_digit += 3
            pass_encoded += str(new_digit)
    return pass_encoded

if __name__ == '__main__':
    menu_continue = True

    while menu_continue:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = int(input('Please enter an option: '))

        if option == 1:
            encode_option = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
        elif option == 2:
            encoded_password = encode_password(encode_option)
            print('The encoded password is', encoded_password, ', and the original password is', encode_option, '.')
        elif option == 3:
            menu_continue = False