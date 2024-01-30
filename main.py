def get_flames_count(first_name, second_name):
    common_words_array = []
    counter = 0
    for ch in first_name:
        if ch == ' ':
            continue
        if not ch in second_name:
            counter+=1
        else:
            if not ch in common_words_array:
                common_words_array.append(ch)
    
    for ch in second_name:
        if ch == ' ':
            continue
        if not ch in first_name:
            counter+=1
        else:
            if not ch in common_words_array:
                common_words_array.append(ch)

    index = flames_calculate(counter)
    
    flames_str = ''
    if index == 1:
        flames_str = 'Friends'
    elif index == 2:
        flames_str = 'Lovers'
    elif index == 3:
        flames_str = 'Affectionate'
    elif index == 4:
        flames_str = 'Marry'
    elif index == 5:
        flames_str = 'Enemy'
    else:
        flames_str = 'Siblings'
    return flames_str
    


def loop_flames(iter_loop):
    final_array = []
    for num in range(1,iter_loop):
        flames = [1,2,3,4,5,6]
        index = 0
        while(True):
            #print(f'index: {index}, num {num}')
            index = (index + num-1)%len(flames)
            flames.pop(index)
            if len(flames)==1:
                break
        final_array.append(flames[0])
        iter_loop-=1
    print(final_array)

def flames_calculate(num):
    flames = [1,2,3,4,5,6]
    index = 0
    while(True):
        #print(f'index: {index}, num {num}')
        index = (index + num-1)%len(flames)
        flames.pop(index)
        if len(flames)==1:
            break
    return flames[0]

first_name = input('Enter First Name: ')
second_name = input('Enter Ssecond Name: ')
flames_string = get_flames_count(first_name.lower(), second_name.lower())
print('The FLAMES Result is:', flames_string)