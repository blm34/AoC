import aoc_helper

DAY = 9
YEAR = 2024


def check_sum(disk):
    return sum(pos * file_id for pos, file_id in enumerate(disk) if file_id is not None)


def parse_input_p1(input_text):
    nums = (int(num) for num in input_text)
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


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    disk = parse_input_p1(input_text)

    total = 0

    index_start = 0
    index_end = len(disk) - 1

    while index_start < index_end:
        while disk[index_end] is None:
            index_end -= 1
        while disk[index_start] is not None:
            total += index_start * disk[index_start]
            index_start += 1
        if index_start < index_end:
            total += index_start * disk[index_end]
            index_start += 1
            index_end -= 1

    return total



def parse_input_p2(input_text):
    nums = (int(num) for num in input_text)
    disk = []
    file = True
    file_id = 0
    for num in nums:
        if file:
            disk.append([file_id, num])
            file_id += 1
        else:
            disk.append([None, num])
        file = not file
    return disk


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    disk = parse_input_p2(input_text)

    earliest_gap = [None] * 10
    for index, item in enumerate(disk):
        if item[0] is None:
            for i in range(1, item[1]+1):
                if earliest_gap[i] is None:
                    earliest_gap[i] = index

    file_id = disk[-1][0] if disk[-1][0] is not None else disk[-2][0]
    index = len(disk) - 1

    while file_id > 0:
        while disk[index][0] != file_id:
            index -= 1

        length = disk[index][1]
        earliest_index = earliest_gap[length]

        if earliest_index is None:
            file_id -= 1
            continue
        moved = False
        for new_index in range(earliest_index, index):
            if disk[new_index][0] is None and disk[new_index][1] >= length:
                disk[new_index][1] -= length
                disk.insert(new_index, disk[index])
                disk[index+1] = [None, length]
                moved = True
                earliest_gap[length] = new_index + 1
                break
        if not moved:
            earliest_gap[length] = None
        file_id -= 1

    expanded_disk = []
    for item in disk:
        expanded_disk.extend([item[0]] * item[1])

    return check_sum(expanded_disk)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
