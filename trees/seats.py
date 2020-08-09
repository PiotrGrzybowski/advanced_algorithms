from typing import List


def find_biggest_distance(seats: List[int]) -> int:
    index = 0
    biggest_distance = 0

    while index < len(seats):
        if seats[index] == 0:
            candidate = index

            while candidate < len(seats) and seats[candidate] == 0:
                candidate += 1

            if index == 0 or candidate == len(seats):
                distance = candidate - index - 1
            else:
                distance = (candidate - index) // 2

            if distance > biggest_distance:
                biggest_distance = distance

            index = candidate

        else:
            index += 1

    return biggest_distance


if __name__ == '__main__':
    values = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]

    result = find_biggest_distance(values)
    print(result)
