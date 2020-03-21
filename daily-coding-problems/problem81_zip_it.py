
# O(mn^2)
def all_possible(mapping, digit_string):
    results = list(mapping[digit_string[-1]])
    digit_list = list(digit_string)
    digit_list.pop()
    print(results)
    print(digit_list)
    
    while digit_list: # O(n)
        digit = digit_list[-1]
        mapped_letters = mapping[digit]
        results *= len(mapped_letters)
        for i, digit in enumerate(results): # O(n*m)
            results[i] = mapped_letters[i%len(mapped_letters)] + results[i]

        digit_list.pop() # O(n)

    return results

if __name__== "__main__":
    mapping = {
        "2" : ["a", "b", "c"],
        "3" : ["d", "e", "f"],
        "4" : ["Y", "Z"]
    }
    print(all_possible(mapping, "234"))