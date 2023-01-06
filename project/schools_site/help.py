def remove_double(data, index):
    """Функция удаляет повторы. Аргументы:
    data - QuerySet; index - название поля, по которому проверяются повторы"""
    new_data = []
    for i in data:
        title = get_title(i, index)
        flag = list(filter(lambda x: title == get_title(x.lower()) or " ".join(title) in " ".join(get_title(x.lower())) or\
                                     " ".join(get_title(x.lower())) in " ".join(title), new_data))
        if not flag:
            new_data.append(i[index])
        else:
            if len(flag[0]) > len(i[index]):
                new_data[new_data.index(flag[0])] = i[index]
    return new_data


def get_title(i, index=None):
    if index:
        i = i[index]
    if '"' in i:
        title = i.split('"')
        if len(title) > 2:
            title = title[1] + title[2]
        else:
            title = title[1]
    elif "«" in i:
        title = i.split('«')
        if len(title) > 2:
            title = title[1] + title[2]
        else:
            title = title[1]
        title = title.replace("»", "")
    else:
        title = i
    title = title.lower()
    title = title.replace(";", " ")
    title = title.replace(".", " ")
    title = title.replace(",", " ")
    title = title.replace("(", " ")
    title = title.replace(")", " ")
    title = title.replace("имени", "им")
    return title.split()