import re


def preprocess_string(s):
    clean_string = ''
    for ch in s:
        if ch in '01':
            clean_string += ch
    return clean_string


triads = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0], '100': [0, 0],
          '101': [0, 0], '110': [0, 0], '111': [0, 0]}


def calculate_dataset(string):
    for triad in triads:
        matches = [m.start() for m in re.finditer(f'(?={triad})', string[:-1])]
        for match in matches:
            number = string[match + 3]
            if number == '0':
                triads[triad][0] += 1
            else:
                triads[triad][1] += 1


final_string = ''
length = 100
print('Please give AI some data to learn...')
print(f'Current data length is {len(final_string)}, {length - len(final_string)} symbols left')
while len(final_string) < length:
    add = input('Print a random string containing 0 or 1:\n')
    final_string += preprocess_string(add)
    if len(final_string) < length:
        print(f'Current data length is {len(final_string)}, {length-len(final_string)} symbols left')

calculate_dataset(final_string)
print('Final data string:')
print(final_string)
capital = 100
print()
print(f'You have ${capital}. Every time the algorithm successfully predicts your next press, you lose $1. '
      'Otherwise, you earn $1. If you reach $200 you win. Print "enough" to leave the game. Let\'s go!')

print('Print a random string containing 0 or 1:')
test = input()

while test != 'enough' and capital > 0:
    test = preprocess_string(test)
    if test == '':
        print('Print a random string containing 0 or 1:')
        test = input()
        continue
    prediction = '101'
    correct_guesses = 0
    total_guesses = len(test)-3
    for i in range(len(test[:-3])):
        current_tri_index = i + 3
        current_tri = test[i:current_tri_index]
        current_tri_values = triads[current_tri]
        predicted_ch = str(current_tri_values.index(max(current_tri_values)))
        if predicted_ch == test[current_tri_index]:
            correct_guesses += 1
            capital -= 1
        else:
            capital += 1
        prediction += predicted_ch

    print('prediction: ')
    print(prediction)

    print(f'Computer guessed right {correct_guesses} out of {total_guesses}'
          f' symbols ({correct_guesses/total_guesses * 100: .2f} %)')
    print(f'Your capital is now ${capital}')
    if capital < 0:
        print('Game over!')
        break
    elif capital > 200:
        print('You Win!!')
        break
    calculate_dataset(test)
    print('Print a random string containing 0 or 1:')
    test = input()
