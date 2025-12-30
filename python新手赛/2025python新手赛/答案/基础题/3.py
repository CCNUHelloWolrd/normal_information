letters = ['A', 'B', 'C', 'D', 'E']  # 直接定义为大写
result = []

# 五重循环遍历所有名次排列（i-j-m对应第1-5名）
for i in range(5):
    for j in range(5):
        if j == i:
            continue
        for k in range(5):
            if k == i or k == j:
                continue
            for l in range(5):
                if l == i or l == j or l == k:
                    continue
                for m in range(5):
                    if m == i or m == j or m == k or m == l:
                        continue
                    combo = (letters[i], letters[j], letters[k], letters[l], letters[m])

                    # 验证每位选手的预测（一对一错，异或判断）
                    e_ok = (combo[3] == 'E') ^ (combo[0] == 'A')
                    d_ok = (combo[4] == 'C') ^ (combo[2] == 'D')
                    c_ok = (combo[0] == 'C') ^ (combo[1] == 'D')
                    b_ok = (combo[1] == 'B') ^ (combo[3] == 'E')
                    a_ok = (combo[1] == 'B') ^ (combo[2] == 'A')

                    if e_ok and d_ok and c_ok and b_ok and a_ok:
                        result.append(''.join(combo))

# 输出结果
for valid in result:
    print(valid)