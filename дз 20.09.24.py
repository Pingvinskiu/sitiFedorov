def ASCII_dict():
    alphabet = {
        'А': '11000000', 'а': '11100000',
        'Б': '11000001', 'б': '11100001',
        'В': '11000010', 'в': '11100010',
        'Г': '11000011', 'г': '11100011',
        'Д': '11000100', 'д': '11100100',
        'Е': '11000101', 'е': '11100101',
        'Ж': '11000110', 'ж': '11100110',
        'З': '11000111', 'з': '11100111',
        'И': '11001000', 'и': '11101000',
        'Й': '11001001', 'й': '11101001',
        'К': '11001010', 'к': '11101010',
        'Л': '11001011', 'л': '11101011',    
        'М': '11001100', 'м': '11101100',
        'Н': '11001101', 'н': '11101101',
        'О': '11001110', 'о': '11101110',
        'П': '11001111', 'п': '11101111',
        'Р': '11010000', 'р': '11110000',
        'С': '11010001', 'с': '11110001',
        'Т': '11010010', 'т': '11110010',
        'У': '11010011', 'у': '11110011',
        'Ф': '11010100', 'ф': '11110100',
        'Х': '11010101', 'х': '11110101',
        'Ц': '11010110', 'ц': '11110110',
        'Ч': '11010111', 'ч': '11110111',
        'Ш': '11011000', 'ш': '11111000',
        'Щ': '11011001', 'щ': '11111001',
        'Ъ': '11011010', 'ъ': '11111010',
        'Ы': '11011011', 'ы': '11111011',
        'Ь': '11011100', 'ь': '11111100',
        'Э': '11011101', 'э': '11111101',
        'Ю': '11011110', 'ю': '11111110',
        'Я': '11011111', 'я': '11111111',
        ' ': '10100000', 
        ',': '10000010',
        '.': '10010101',
        '-': '10010110'
        }
        
def text_to_binary(text, alphabet):
    binary_codes = [alphabet[char] for char in text.upper() if char in alphabet]
    return ' '.join(binary_codes)
alphabet = ASCII_dict()

user_input = input("Введите слово: ")
binary_output = text_to_binary(user_input, alphabet)

print(binary_output)