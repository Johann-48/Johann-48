print('SORTER')
t = int(input('How many numbers to sort: '))
c = 0
num = 0
nums = []
while c < t:
    num = int(input('Number: '))
    nums.append(num)
    c = c + 1
s = sorted(nums)
print('Your number are', nums)
print('Your numbers sorted are', s)