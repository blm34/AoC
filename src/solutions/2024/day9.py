import heapq

import aoc_helper

DAY = 9
YEAR = 2024


def parse_input_p1(input_text):
    nums = map(int, input_text)
    disk = []
    file = True
    file_id = 0
    for num in nums:
        if file:
            disk.extend([file_id] * num)
            file_id += 1
        else:
            disk.extend([None] * num)
        file = not file
    return disk


def p1(input_text):
    disk = parse_input_p1(input_text)

    total = 0

    forwards_index = 0
    backwards_index = len(disk) - 1

    while forwards_index < backwards_index:
        while disk[backwards_index] is None:
            backwards_index -= 1
        while disk[forwards_index] is not None:
            total += forwards_index * disk[forwards_index]
            forwards_index += 1
        while forwards_index < backwards_index and disk[backwards_index] is not None and disk[forwards_index] is None:
            total += forwards_index * disk[backwards_index]
            forwards_index += 1
            backwards_index -= 1

    return total



def parse_input_p2(input_text):
    nums = map(int, input_text)

    files = []  # file[file_id] = [file_start_index, file_length]
    gaps = [[] for _ in range(10)]  # gaps[length] = heap of `gap_start_index` for gaps of length length

    file = True
    index = 0

    for num in nums:
        if file:
            files.append([index, num])
        elif num > 0:
            heapq.heappush(gaps[num], index)
        index += num
        file = not file

    return files, gaps


def p2(input_text):
    files, gaps = parse_input_p2(input_text)

    max_file_id = (len(input_text) - 1) // 2
    max_available_gap_length = 9

    for file_id in range(max_file_id, 0, -1):
        length = files[file_id][1]

        first_gap_index = files[file_id][0]
        first_gap_len = None
        for i in range(length, max_available_gap_length + 1):
             if gaps[i] and gaps[i][0] < first_gap_index:
                first_gap_index = gaps[i][0]
                first_gap_len = i

        if first_gap_len is None:
            max_available_gap_length = length - 1
            if max_available_gap_length == 0:
                break
        else:
            index = heapq.heappop(gaps[first_gap_len])
            files[file_id][0] = index
            if first_gap_len > length:
                heapq.heappush(gaps[first_gap_len - length], index + length)

    check_sum = 0
    for file_id, (start_index, file_length) in enumerate(files):
        check_sum += file_id * (2 * start_index + file_length - 1) * file_length // 2

    return check_sum


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
