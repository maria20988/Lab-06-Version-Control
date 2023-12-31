# Made by Maria Fernandez
def decoder(number):
    hi = list(number)
    num_list = ""
    for i in range(len(hi)):
        hi[i] = int(hi[i])-3
        if hi[i] <= 0:
            hi[i] = 10 - hi[i]
        num_list += str(hi[i])
    return num_list

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
            decoded_password = decoder(encode_option)
            print('The encoded password is', encode_option, ', and the original password is', decoded_password, '.')
        elif option == 3:
            menu_continue = False




