def conditions_func(data):
    if all(data):
        return "yes"
    elif not any(data):
        return "no"
    else:
        return "I don't Know"

values=[True,False,True,False]
print(conditions_func(values))