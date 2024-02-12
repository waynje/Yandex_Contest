def sort_with_template(arr, template, arr_len, template_len):
    sorted_arr = []
    for num in template:
        if num in arr:
            sorted_arr.extend([num] * arr.count(num))
            arr = [x for x in arr if x != num]
    if arr_len > template_len:
        sorted_arr.extend(sorted(arr))
    return sorted_arr



arr = list(map(int, input().split()))
template = list(map(int, input().split()))
arr_len = int(input())
template_len = int(input())

sorted_arr = sort_with_template(arr, template, arr_len, template_len)
print(*sorted_arr)