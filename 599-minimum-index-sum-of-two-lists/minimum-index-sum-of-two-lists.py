class Solution:
    def findRestaurant(self, list1, list2):
        positions = {}
        for i in range(len(list1)):
            positions[list1[i]] = i

        answer = []
        min_index_sum = float("inf")

        for j in range(len(list2)):
            restaurant = list2[j]
            if restaurant in positions:
                index_sum = positions[restaurant] + j
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    answer = [restaurant]
                elif index_sum == min_index_sum:
                    answer.append(restaurant)

        return answer