def max_rocks(requests_length, requests, probes_length, probes):
    requests_completed = 0
    requests = sorted(requests)
    probes = sorted(probes)
    request_index = requests_length - 1

    probe_index = probes_length - 1
    while request_index >= 0 and probe_index >= 0:
        if requests[request_index] <= probes[probe_index]:
            requests_completed += 1
            probe_index -= 1
        request_index -= 1
    return requests_completed


if __name__ == '__main__':
    requests_length = int(input())
    requests = list(map(int, input().split(' ')))
    probes_length = int(input())
    probes = list(map(int, input().split(' ')))
    print(str(max_rocks(
        requests_length,
        requests,
        probes_length,
        probes)))

