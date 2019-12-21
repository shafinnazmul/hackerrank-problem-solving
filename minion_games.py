def all_vowels():
    return "AEIOU"


def count_substr_by_pos(pos, length):
    return length - pos


def sum_cum_count_substr(positions, length):
    cum_sum = 0
    for pos in positions:
        cum_sum += count_substr_by_pos(pos, length)
    return cum_sum


def get_vowel_positions(mystr):
    my_vowel_positions = []
    for i in range(len(mystr)):
        if mystr[i] in all_vowels():
            my_vowel_positions.append(i)
    return my_vowel_positions


def get_consonant_positions(mystr):
    const_positions=set(range(len(mystr))).difference(set(get_vowel_positions(mystr)))
    return list(const_positions)

# calculate value for stuart
def get_const_prefixed_sub_str_count(mystr):
    my_consonant_positions=get_consonant_positions(mystr)
    c_count = sum_cum_count_substr(my_consonant_positions, len(mystr))
    return c_count

def get_vowel_prefixed_sub_str_count(mystr):
    my_vowel_positions = get_vowel_positions(mystr)
    v_count = sum_cum_count_substr(my_vowel_positions,len(mystr))
    return v_count


def minion_game(string):
    vowel_prefixed_str_count = get_vowel_prefixed_sub_str_count(mystr=string)
    const_prefixed_str_count = get_const_prefixed_sub_str_count(mystr=string)
    print("Stuart",const_prefixed_str_count) if const_prefixed_str_count>vowel_prefixed_str_count else print("Kevin", vowel_prefixed_str_count) if vowel_prefixed_str_count>const_prefixed_str_count else print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
