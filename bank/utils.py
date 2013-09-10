def get_total_owed(list_1, list_2):
    new_list = []
    for idx, val in enumerate(list_1):
        val.amount = (val.w_amount or 0) - (list_2[idx].d_amount or 0)
        new_list.insert(idx, val)
    return new_list


def get_owed(item):
    return item.amount > 0
    
def get_owe(item):    
    return item.amount < 0