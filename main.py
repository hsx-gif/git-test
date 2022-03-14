# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('world')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
s = input("请输入你的字符串\n")

result = []

for i in range(0,len(s),2):
    if i + 1 < len(s):
        result.append(s[i]+s[i+1])
    else:
        result.append(s[i])
for i in result:
    print(i,end=' ')

print()
print(len(s))