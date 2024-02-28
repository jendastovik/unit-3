class palNum:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    def get_pal_list(self):
        ls = []
        for num in range(self.A, self.B + 1):
            rev = ""
            for i in str(num):
                rev = i + rev
            # if str(num) == str(num)[::-1]:
            #     ls.append(num)
            if str(num) == rev:
                ls.append(num)

        return ls

palindrome = palNum(1, 9)
palindrome2 = palNum(10, 199)

print(palindrome.get_pal_list())
print(palindrome2.get_pal_list())