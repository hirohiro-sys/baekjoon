nums = input()
i = 0
while 1:
    i += 1
    num = str(i)
    while len(nums) > 0 and len(num) > 0:
        # 入力受けた数字が見つかるごとに削除
        if nums[0] == num[0]:
            nums = nums[1:]
        num = num[1:]
    # 全部見つかったら終了
    if nums=="":
        print(i)
        break

"""
https://www.acmicpc.net/problem/1515
"""
