grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
list = ['Johnny','Bilbo','Steve','Khendrik','Aaron']
print(sorted(list))
grades1 = [5,3,3,5,4]
average1 = sum(grades1) / len(grades1)
grades2 = [2,2,2,3]
average2 = sum(grades2) / len(grades2)
grades3 = [4,5,5,2]
average3 = sum(grades3) / len(grades3)
grades4 = [4,4,3]
average4 = sum(grades4) / len(grades4)
grades5 = [5,5,5,4,5]
average5 = sum(grades5) / len(grades5) # print('The average is ', round(average5,2))
dictionary = {'Aaron':average1, 'Bilbo':average2, 'Johnny':average3, 'Khendrik':average4, 'Steve':average5}
print(dictionary)