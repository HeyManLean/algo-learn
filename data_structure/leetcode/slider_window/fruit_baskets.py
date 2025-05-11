# coding=utf-8


def fruit_buckets(tree: list):
    """
    在一排树中，第 i 棵树产生 tree[i] 型的水果。
    你可以从你选择的任何树开始，然后重复执行以下步骤：

    把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
    移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
    请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

    你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。
    用这个程序你能收集的水果总量是多少？
    链接：https://leetcode-cn.com/problems/fruit-into-baskets
    """
    tmap = {}
    n = len(tree)
    left = 0
    res = 0

    for i in range(n):
        tmap[tree[i]] = i

        while len(tmap) > 2:
            if tmap[tree[left]] == left:
                tmap.pop(tree[left])

            left += 1

        res = max(res, i - left + 1)

    return res
