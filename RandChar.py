import random
import string

def rand_char(num):
    def number_generator():
        # generating number
        numbers = []
        for i in range(0, 9):
            numbers.append(i)
        return numbers
    def alphabet_generator():
        # generating alphabet
        alphabets = list(string.ascii_lowercase)
        return alphabets

    number_list = number_generator()
    alphabet_list = alphabet_generator()
    # masukkan panjang password
    password_len = num

    if password_len <= 5:
        alpha_len = random.randint(2, password_len-1)
    elif password_len > 5:
        alpha_len = random.randint(password_len-6,password_len-1)

    num_len = password_len - alpha_len

    def alpha_randomizer():
        # mengacak alphabet dari list
        randomized_alpha = []
        for a in range(alpha_len):
            rand = random.randint(0, 25)
            randomizing_alpha = alphabet_list[rand]
            randomized_alpha.append(randomizing_alpha)
        return randomized_alpha
    def num_randomizer():
        # mengacak nomor dari list
        randomized_num = []
        for a in range(num_len):
            rand = random.randint(0, 8)
            randomizing_num = number_list[rand]
            randomized_num.append(randomizing_num)
        return randomized_num

    randomized_alphabet = alpha_randomizer()
    randomized_number = num_randomizer()


    password = []
    # menambah list password dengan jumlah yang ditentukan
    for i in range(password_len):
        u = ""
        password.append(u)

    # variable untuk melakukan cek index berapa yang ditempati karakter
    filled_index_bynumber = []
    filled_index_byalpha = []

    # mengaplikasikan anka yang telah diacak kedalam list password dengan index acak
    for f in randomized_number:
        rand = random.randint(0,password_len-1)
        for a in password:
            if password[rand] != '':
                rand = random.randint(0,password_len-1)
            else:
                pass
        password[rand] = str(f)
        filled_index_bynumber.append(rand)


    # mengaplikasikan huruf yang telah diacak kedalama list password dengan index acak dan index yang tersisa
    for f in randomized_alphabet:
        rand = random.randint(0,password_len-1)
        for a in password:
            if password[rand] != '':
                rand = random.randint(0,password_len-1)
            else:
                pass
        password[rand] = str(f)
        filled_index_byalpha.append(rand)


    # mengecek apakah password ada yang kosong indexnya dan menambahkannya dengan karakter lain
    for i in range(password_len):
        indx = 0
        if password[indx] == "":
            def al():
                return alphabet_list[random.randint(0, 25)]
            def num():
                return number_list[random.randint(0, 9)]
            random_method_picker = [al(), num()]
            password[indx] = random_method_picker[random.randint(0,2)]
            print('ada')
            indx += 1
        else:
            pass

    password_string = str("'" + str(password) + "'")
    result = password_string.replace("'", '').replace('[', '').replace(']', '').replace(', ', '')
    return result
