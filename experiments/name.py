def check_word(Name):
    if Name.isalpha() and Name.isupper():
        print(Name,"Is correct")
    else:
        print(Name,"Is wrong")

check_word("Hello")
check_word("Example")
check_word("@mahesh")
check_word("amahd%")
check_word("Mahesh")
check_word("mahesh")
check_word("Mahesh")
check_word("mahesH")
check_word("MAHESH")