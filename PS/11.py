# codewars - String ends with?
def solution(string, ending):
        if len(string) < len(ending):
            return False
        if ending in string[len(string)-len(ending):len(string)+1]:
            return True
        return False

print(solution('abc', 'bc')) # returns true
print(solution('abc', 'd')) # returns false
print(solution('bc', 'bcbc'))
print(solution('samurai', 'ai'))
print(solution('abc', 'abcd'))