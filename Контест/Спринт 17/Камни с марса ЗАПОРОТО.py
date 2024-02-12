def calculate():
    n = int(input())
    order_weights = list(map(int, input().split()))
    m = int(input())
    sample_weights = list(map(int, input().split()))

    counter = 0
    for sample_weight in sample_weights:
        if sample_weight in order_weights:
            counter += 1
            sample_weights.remove(sample_weight)
            order_weights.remove(sample_weight)

    def max_counter(sample_weights, order_weights, counter):
        flag = False
        if len(sample_weights) == 0 or len(order_weights) == 0:
            return counter
        if max(sample_weights) >= max(order_weights):
            # counter += 1 
            flag = True
            sample_weights.remove(max(sample_weights))
        order_weights.remove(max(order_weights))
        if flag:
            counter = 1 + max_counter(sample_weights, order_weights, counter)
        else:
            counter = max_counter(sample_weights, order_weights, counter)
        return counter
    
    # def max_counter(sample_weights, order_weights, counter):
    #     if len(sample_weights) == 0 or len(order_weights) == 0:
    #         return counter
    #     if max(sample_weights) >= max(order_weights):
    #         counter += 1 
    #         sample_weights.remove(max(sample_weights))
    #     order_weights.remove(max(order_weights))
    #     max_counter(sample_weights, order_weights, counter)
    #     return counter
                 
    counter = max_counter(sample_weights, order_weights, counter)
    print(counter)

if __name__ == '__main__':
    calculate()

