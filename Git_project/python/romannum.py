def roman_to_number(roman):
    roman = roman.upper()
    converts = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    sum = 0
    for i in range(len(roman) - 1):

        left = roman[i]
        right = roman[i + 1]

        if converts[left] < converts[right]:
            sum -= converts[left]

        else:
            sum += converts[left]

    sum += converts[roman[-1]]

    return sum


a = 'mdcxxv'

print(roman_to_number(a))