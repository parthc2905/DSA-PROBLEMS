class Solution:
    def findRestaurant(self, list1, list2):
        l = []
        m = 2000
        for i in range(len(list1)):
            j = list2.index(list1[i]) if list1[i] in list2 else False
            if (list1[i] in list2) and (len(list1[i])==len(list2[j])):
                if m>=i+j:
                    m = min(m,i+j)
                    l.append((i,j))
        list2.clear()
        for i,j in l:
            if i+j == m:
                list2.append(list1[i])

        return list2
