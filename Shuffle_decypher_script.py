
def generating_matrix(rows, columns):
    matrix = []

    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(" ")
        matrix.append(row)
    return matrix


def inserting_values(text, rows, columns):
    matrix = generating_matrix(rows, columns)

    text_index = 0

    for x in range(rows):
        for y in range(columns):
            while text_index < len(text) and text[text_index] in ["\n", ".", ",", "!", "?"]:
                text_index += 1

            if text_index < len(text):
                matrix[y][x] = text[text_index]
                text_index += 1
            else:
                matrix[x][y] = " "
    return matrix


def decrypting_the_text(matrix, columns):
    encrypted_text = []
    for k in range(0, columns):
        for x in range(len(matrix)):
            value = matrix[k][x]
            if value not in ["\n", ".", ","]:
                encrypted_text.append(value)

    final_encrypted_text = ''.join(encrypted_text)
    return final_encrypted_text


def upload_the_file():
    file = 'shuffle_proprietary.txt'
    new_file = 'decoded.txt'
    rows = 94
    columns = 94

    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    matrix = inserting_values(text, rows, columns)

    encrypted_text = decrypting_the_text(matrix, columns)

    with open(new_file, 'w', encoding='utf-8') as f:
        final_encrypted_text = ''.join(encrypted_text)
        f.write(final_encrypted_text)

    return text


if __name__ == '__main__':
    upload_the_file()


# do sprawdzenia mozna uzyc strony: https://legacy.cryptool.org/en/cto/transposition
