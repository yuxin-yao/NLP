#!/usr/bin/python

class EditDistance():

    def __init__(self):
        """
        Do not change this
        """

    def calculateLevenshteinDistance(self, str1, str2):
        """
        TODO:
            take two strings and calculate their Levenshtein Distance for task 1
            return an integer which is the distance
        """

        n = len(str2)
        m = len(str1)
        str1_list = list(str1)
        str2_list = list(str2)

        dis_matrix = [0] * (n+1)
        for i in range(n+1):
            dis_matrix[i] = [0] * (m+1)

        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dis_matrix[i][j] = j
                elif j == 0:
                    dis_matrix[i][j] = i
                elif str1_list[j-1] == str2_list[i-1]:
                    dis_matrix[i][j] = dis_matrix[i-1][j-1]
                else:
                    dis_matrix[i][j] = 1 + min(dis_matrix[i][j-1], dis_matrix[i-1][j-1], dis_matrix[i-1][j])

        return dis_matrix[n][m]


    def calculateOSADistance(self, str1, str2):
        """
        TODO:
            take two strings and calculate their OSA Distance for task 2
            return an integer which is the distance
        """

        n = len(str2)
        m = len(str1)
        str1_list = list(str1)
        str2_list = list(str2)
        dis_matrix = [0] * (n + 1)
        for i in range(n + 1):
            dis_matrix[i] = [0] * (m + 1)

        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dis_matrix[i][j] = j
                elif j == 0:
                    dis_matrix[i][j] = i
                elif str1_list[j-1] == str2_list[i-1]:
                    dis_matrix[i][j] = dis_matrix[i-1][j-1]
                elif str1_list[j-1] == str2_list[i-2] and str1_list[j-2] == str2_list[i-1]:
                    dis_matrix[i][j] = 1 + min(dis_matrix[i][j-1], dis_matrix[i-1][j-1], dis_matrix[i-1][j], dis_matrix[i-2][j-2])
                else:
                    dis_matrix[i][j] = 1 + min(dis_matrix[i][j-1], dis_matrix[i-1][j-1], dis_matrix[i-1][j])

        return dis_matrix[n][m]


    def calculateDLDistance(self, str1, str2):
        """
        TODO:
            take two strings and calculate their DL Distance for task 3
            return an integer which is the distance
        """

        from collections import Counter

        n = len(str2)
        m = len(str1)
        str1_list = list(str1)
        str2_list = list(str2)
        alphabet_counter = Counter(str2_list+str1_list)



        da = {}
        for i, alph in enumerate(alphabet_counter.keys()):
            #da[alph] = i
            da[alph] = 0
        da_real = [0 for x in range(0, len(da))]
        dis_matrix = {}
        #maxdist = n + m + 1
        maxdist = n + m
        dis_matrix[(-1, -1)] = maxdist

        for i in range(n + 1):
            dis_matrix[(i, -1)] = maxdist
            dis_matrix[(i, 0)] = i
        for j in range(m + 1):
            dis_matrix[(-1, j)] = maxdist
            dis_matrix[(0, j)] = j
        for i in range(1, n+1, 1):
            db = 0
            for j in range(1, m + 1, 1):
                k = da[str1_list[j-1]]
                l = db
                if (str2_list[i-1] == str1_list[j-1]):
                    cost = 0
                    db = j
                else:
                    cost = 1
                dis_matrix[(i, j)] = min([dis_matrix[(i-1, j-1)]+cost,
                                          dis_matrix[(i, j-1)]+1,
                                          dis_matrix[(i-1, j)]+1,
                                          dis_matrix[k-1, l-1]+(i-k-1)+(j-l-1) + 1])
            da[str2_list[i-1]] = i


        return dis_matrix[(n, m)]
