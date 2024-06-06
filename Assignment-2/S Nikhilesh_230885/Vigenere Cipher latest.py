import collections

ciphertext = 0xF96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794
str_ciphertext = "F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"

# Determining key length
char_list = []
str_iter = 0
square_sum = 0
check_value = 0
max_value = 0
possible_length = 0
n = 0
for check_length in range(1, 12):
    char_list.clear()
    str_iter = 0
    square_sum = 0
    check_value = 0
    n = 0
    while str_iter < len(str_ciphertext):
        char_list.append(int(str_ciphertext[str_iter] + str_ciphertext[str_iter + 1], 16))
        str_iter += 2*check_length
    n = len(char_list)
    count_dict = collections.Counter(char_list)
    count_dict = dict(count_dict)
    for i in list(count_dict.values()):
        square_sum += i*i
    check_value = square_sum / (n*n)
    if check_value > max_value:
        max_value = check_value
        possible_length = check_length

key_length = possible_length
print(f"Key length is : {key_length}", end='\n\n')

# Determining the key
Key = ""
flag = 1
new_list = []
sigma = 0
max_sigma = 0
max_test = 0
m = 0
char_value = ""
const_dict = {97: 8.2, 98: 1.5, 99: 2.8, 100: 4.3, 101: 12.7, 102: 2.2, 103: 2.0, 104: 6.1, 105: 7.0, 106: 0.2, 107: 0.8, 108: 4.0, 109: 2.4, 110: 6.7, 111: 1.5, 112: 1.9, 113: 0.1, 114: 6.0, 115: 6.3, 116: 9.1, 117: 2.8, 118: 1.0, 119: 2.4, 120: 0.2, 121: 2.0, 122: 0.1}
for num in range(0, key_length):
    char_list.clear()
    str_iter = 2*num
    char_value = ""
    max_test = 0
    max_sigma = 0
    sigma = 0
    m = 0
    flag = 1
    new_list.clear()
    while str_iter < len(str_ciphertext):
        char_list.append(int(str_ciphertext[str_iter] + str_ciphertext[str_iter + 1], 16))
        str_iter += 2*key_length
    for test in range(0, 256):
        flag = 1
        sigma = 0
        m = 0
        for char in char_list:
            temp = char ^ test
            if temp not in range(32, 128):
                flag = 0
                break
            if temp in range(48, 58):
                flag = 0
                break
            elif temp in range(65, 91) or temp in range(97, 123):
                m += 1
        if flag == 0:
            continue
        new_list.clear()
        new_list = [ord((chr(let ^ test)).lower()) for let in char_list]
        freq_dict = collections.Counter(new_list)
        freq_dict = dict(freq_dict)
        for j in range(97, 123):
            try:
                sigma += (freq_dict[j] * const_dict[j]) / (m * 100)
            except KeyError:
                sigma += 0
        if sigma > max_sigma:
            max_sigma = sigma
            max_test = test
            char_value = (str(hex(test)))[2:]
    Key += char_value

print(f"The Key is {Key}", end='\n\n\n')


# Decrypting the Ciphertext
message = ""
digit = 0
while digit < len(str_ciphertext):
    letter = str_ciphertext[digit] + str_ciphertext[digit + 1]
    temp_num = digit % (2*key_length)
    actual_letter = chr(int(letter, 16) ^ int(Key[temp_num] + Key[temp_num + 1], 16))
    message += actual_letter
    digit += 2

print(message)
