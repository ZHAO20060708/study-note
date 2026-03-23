### 假设条件

假设：
1.  $A(n) \in O(f(n))$
2.  $B(n) \in O(g(n))$

根据定义，这意味着：
*   存在常数 $C_1 > 0$ 和 $n_1 \ge 0$，使得对于所有 $n \ge n_1$，有：
    $$|A(n)| \le C_1 \cdot |f(n)| \quad \text{......(1)}$$
*   存在常数 $C_2 > 0$ 和 $n_2 \ge 0$，使得对于所有 $n \ge n_2$，有：
    $$|B(n)| \le C_2 \cdot |g(n)| \quad \text{......(2)}$$

### 推导过程

我们需要证明 $A(n) \cdot B(n) \in O(f(n) \cdot g(n))$。也就是说，我们需要找到新的常数 $C_3 > 0$ 和 $n_3 \ge 0$，使得对于所有 $n \ge n_3$，满足：
$$|A(n) \cdot B(n)| \le C_3 \cdot |f(n) \cdot g(n)|$$

**步骤 1：确定 $n_3$**
为了让不等式 (1) 和 (2) 同时成立，我们需要 $n$ 同时大于等于 $n_1$ 和 $n_2$。因此，我们取：
$$n_3 = \max(n_1, n_2)$$
这样，当 $n \ge n_3$ 时，(1) 和 (2) 均成立。

**步骤 2：确定 $C_3$ 并相乘**
当 $n \ge n_3$ 时，我们可以将不等式 (1) 和 (2) 的两边分别相乘（因为绝对值均为非负数，不等号方向不变）：
$$|A(n)| \cdot |B(n)| \le (C_1 \cdot |f(n)|) \cdot (C_2 \cdot |g(n)|)$$

利用绝对值的性质 $|x| \cdot |y| = |xy|$，整理得：
$$|A(n) \cdot B(n)| \le (C_1 \cdot C_2) \cdot |f(n) \cdot g(n)|$$

令 $C_3 = C_1 \cdot C_2$。因为 $C_1 > 0$ 且 $C_2 > 0$，所以 $C_3 > 0$。

于是我们得到：
$$|A(n) \cdot B(n)| \le C_3 \cdot |f(n) \cdot g(n)|，\quad \forall n \ge n_3$$

### 结论

根据大 $O$ 符号的定义，上述不等式表明：
$$A(n) \cdot B(n) \in O(f(n) \cdot g(n))$$

因此，我们证明了：
$$O(f(n)) \cdot O(g(n)) \subseteq O(f(n) \cdot g(n))$$

在算法复杂度的语境下，这通常被记作等式，即：
$$O(f(n)) \cdot O(g(n)) = O(f(n) \cdot g(n))$$

**证毕。**