

def validate_answer(instance):
    '''
    BOOLEAN = 1
    ONE_CORRECT = 2
    MORE_ONE_CORRECT = 3
    ALL_MUST_CORRECT = 4
    '''
    for item in instance:
        if item.question.question_type == 1:
            if item.bool_answer == item.question.bool_answer:
                item.approved = True
                item.score = item.question.score
                item.save()

        if item.question.question_type == 2:
            if item.one_answer == item.question.one_answer:
                item.approved = True
                item.score = item.question.score
                item.save()

        if item.question.question_type == 3:
            for value in item.multiple_answers:
                if value in item.question.multiple_answers:
                    item.approved = True
                    item.score = item.question.score
                    item.save()

        if item.question.question_type == 4:
            approved = False
            for value in item.question.multiple_answers:
                if value in item.multiple_answers:
                    approved = True
                else:
                    approved = False
            if approved:
                item.approved = True
                item.score = item.question.score
                item.save()
