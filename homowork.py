right_answers = 0

def validate_answer(our_answer, valid_answer):
    global right_answers

    if our_answer == valid_answer:
        print('Right')
        right_answers += 1
    else:
        print('Wrong!')

# database = {
#     'What is 1': 'int',
#     ''
# }

# for questions , answer in database.items():
#     print(question, answer)

answer1 = input('What is 1? ')
validate_answer(answer1,'int')

answer2 = input('2+2 = ? ')
validate_answer(int(answer2),4)

answer3 = input('Capital of Russia? ')
validate_answer(answer3,'Moscow')

print('You gave {} right answers'.format(right_answers))