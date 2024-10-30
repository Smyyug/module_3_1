calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return
def  string_info(string):
    kor = len(string), string.upper(), string.lower()
    count_calls()
    return kor
def is_contains(string, list_to_search  ):
        nal = False
        for i in range(len(list_to_search)):
            list_to_search [i] = list_to_search [i].lower()
            i += 1
        count_calls()
        if string.lower() in list_to_search:
            nal = True
        return  nal
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)