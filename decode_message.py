def test_dp(data, k, memo):
    if k == 0:
        return 1
    s = data.length - k
    if data[s] == '0':
        return 0
    if memo[k] != null:
        return memo[k]
    result = test_dp(data, k-1, memo)
    if k>=2 and int(data[s:s+2]) <= 26:
        result += test_dp(data, k-2, memo)
    memo[k] = result
    return result
def num_ways_dp(data):
    memo = new int[data.length +1]
    return test_dp(data, data.length, memo)