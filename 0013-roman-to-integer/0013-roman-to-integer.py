class Solution:
    def romanToInt(self, s: str) -> int:
        roman = list(s)
        roman.reverse()

        dictionary = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000} 

        def value_of(letter):
            return dictionary.get(letter)


        result = value_of(roman[0])

        for i in range(len(roman)-1):
            if value_of(roman[i]) > value_of(roman[i+1]):
                result -= value_of(roman[i+1])
            else :
                result += value_of(roman[i+1])

        return result
                 


        