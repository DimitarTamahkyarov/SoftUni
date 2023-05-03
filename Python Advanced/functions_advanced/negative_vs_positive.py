def sum_negative_and_positive(numbers):
    negative = 0
    positive = 0


    for num in numbers:
        negative += num if num < 0 else 0
        positive += num if num >= 0 else 0

    def bigger_sum(neg, pos):
        if abs(neg) >= abs(pos):
            return "The negatives are stronger than the positives"
        else:
            return "The positives are stronger than the negatives"
    result = bigger_sum(negative, positive)


    return f"{negative}\n{positive}\n{result}"


nums = [int(x) for x in input().split()]

print(sum_negative_and_positive(nums))
