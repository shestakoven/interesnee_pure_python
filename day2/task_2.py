def sort_lists(current_list, new_list):
    list1, list2 = map(list, [current_list, new_list])
    return sorted(list1 + list2)
