def is_palindrome(string):
    left, right = 0, len(string) - 1
    
    while left < right:
        while left < right and not string[left].isalpha():
            left += 1
        while left < right and not string[right].isalpha():
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                     # False
print(is_palindrome("Aba"))                            # True (теперь регистр игнорируется)


#print(string == string[::-1])

