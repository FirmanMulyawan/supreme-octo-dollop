# data = [8, 4, 10, 12, 2, 0]

# def bubbleSort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(bubbleSort(data))


def correct(string):
  result = ''
  for index in string:
    if index =='1':
      result = result +'I'
    elif index == '5':
      result = result + 'S'
    elif index == '0':
      result = result + 'O'
    else:
      result = result + index 
  return result

correct("51NGAP0RE")