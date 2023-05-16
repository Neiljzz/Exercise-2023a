# check_all_match_size(['lion', 'deer', 'bear'], 4)
# True
# check_all_match_size(['lion', 'deer', 'sheep'], 4)
# False

def check_all_match_size(words, size):
    for word in words:
        if len(word) == size:
            print(True)
        else:
            print(False)

check_all_match_size(['lion', 'deer', 'sheep'], 4)