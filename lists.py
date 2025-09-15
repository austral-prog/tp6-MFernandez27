def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 1:
        del list_to_remove_elements [0]
        del list_to_remove_elements [3:5]

    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,"Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

def is_empty(list_to_check):
    if list_to_check == []:
        answer = True
    else:
        answer = False
    return answer

def check_lists(list_to_compare1, list_to_compare2):
    if (len(list_to_compare1) >= 3) and (len(list_to_compare2) >= 3):
        if list_to_compare1[2] == list_to_compare2[2]:
            answer = True
        else:
            answer = False
    elif (len(list_to_compare1) < 3) or (len(list_to_compare2) < 3):
        answer = False
    return answer

def list_of_lists(list_of_lists_to_modify):
    result = []
    if len(list_of_lists_to_modify) > 0:
        result.append(list_of_lists_to_modify[0][:2])
    if len(list_of_lists_to_modify) > 1:
        result.append(list_of_lists_to_modify[1][1:4])
    if len(list_of_lists_to_modify) > 2:
        result.append(list_of_lists_to_modify[2][-2:])
    return result
