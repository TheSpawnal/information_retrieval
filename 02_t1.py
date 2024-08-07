def merge_AND(list1, list2):
    pointer1 = 0
    pointer2 = 0
    result = []
    while pointer1 < len(sorted_list1) and pointer2 <len(sorted_list2):
        if sorted_list1[pointer1] == sorted_list2[pointer2]:
            result.append(sorted_list1[pointer1])
            pointer1 ++
            pointer2 ++
        else if sorted_list1[pointer1] < sorted_list2[pointer2]:
            pointer1 ++
        else:
            pointer2 ++
    return result


list_a = [3,5,8,10]
list_b = [5,7,8,12]

display(merge_AND(list_a, list_b))