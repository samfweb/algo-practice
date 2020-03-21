def get_key(item):
    return item[0]


def merge_overlap(interval_list):
    sorted_intervals = sorted(interval_list, key=get_key)
    print(sorted_intervals)


if __name__ == "__main__":
    sorted_intervals = 