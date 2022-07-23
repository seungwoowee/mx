# mutable 한 객체 (리스트)
print('=' * 50)

arr1 = [[1, 2, 3, 4, 5, 6],[1, 2, 3, 4, 5, 6]]
arr2 = arr1[:]     # '=' 복사

print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

arr2.append(99)  # arr2 에 값 추가

print('\narr2.append(99)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')
