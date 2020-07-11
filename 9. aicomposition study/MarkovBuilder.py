
import random

class MarkovBuilder:

    # 초기함수, 빈 리스트 생성, 인덱스 부여.
    def __init__(self, value_list):
        self._values_added = 0
        self._reverse_value_lookup = value_list
        self._value_lookup = {}
        for i in range(0, len(value_list)):
            self._value_lookup[value_list[i]] = i
        #Initialize our adjacency matrix with the initial
        #probabilities for note transitions.
        self._matrix=[[0 for x in range(0,len(value_list))] for i in range(0,len(value_list))]

    #주어진 음악을 학습하면서 마르코프 체인 매트릭스를 채워가는 함수
    def add(self, from_value, to_value):
        """Add a path from a note to another note. Re-adding a path between notes will increase the associated weight."""
        value = self._value_lookup
        self._matrix[value[from_value]][value[to_value]] += 1
        self._values_added = self._values_added + 1
        
    # 다음에 올 음계를 넘겨주는 함수 
    def next_value(self, from_value):
        value = self._value_lookup[from_value]
        value_counts = self._matrix[value]
        value_index = self.randomly_choose(value_counts)
        if(value_index < 0):
            raise RuntimeError("Non-existent value selected.")
        else:
            return self._reverse_value_lookup[value_index]

    # 채워진 마르코프 체인 리스트를 통해서 다음에 올 음계를 랜덤하게 추출해내는 함수.
    def randomly_choose(self, choice_counts):
        """Given an array of counts, returns the index that was randomly chosen"""
        counted_sum = 0
        count_sum = sum(choice_counts)

        if count_sum == 0:
            return random.randint(0, len(choice_counts)-1)
        else:
            selected_count = random.randrange(1, count_sum + 1)
            for index in range(0, len(choice_counts)):
                counted_sum += choice_counts[index]
                if(counted_sum >= selected_count):
                    return index
        raise RuntimeError("Impossible value selection made. BAD!")