虽然 $\Omega(f(n)) + \Omega(g(n)) \subseteq \Omega(f(n))$ 是成立的，但两者并不相等（即 $\Omega(f(n)) \not\subseteq \Omega(f(n)) + \Omega(g(n))$）。

### 1. 反例

取 $f(n) = n$，$g(n) = n^2$。

**验证前提条件：**
$$g(n) = \Omega(f(n))$$
即 $n^2 = \Omega(n)$。
根据定义，存在常数 $c=1, n_0=1$，使得对于所有 $n \ge 1$，都有 $n^2 \ge 1 \cdot n$。前提条件满足。

**分析等式两边：**

*   **右边 (RHS)：** $\Omega(f(n)) = \Omega(n)$。
    显然，函数 $h(n) = n$ 属于 $\Omega(n)$。

*   **左边 (LHS)：** $\Omega(f(n)) + \Omega(g(n)) = \Omega(n) + \Omega(n^2)$。
    该集合中的任意函数 $H(n)$ 可以表示为 $H(n) = h_1(n) + h_2(n)$，其中 $h_1(n) \in \Omega(n)$，$h_2(n) \in \Omega(n^2)$。
    这意味着存在常数 $c_1, c_2 > 0$，使得当 $n$ 足够大时：
    $$h_1(n) \ge c_1 n$$
    $$h_2(n) \ge c_2 n^2$$
    因此，$H(n) \ge c_1 n + c_2 n^2 \ge c_2 n^2$。
    这说明左边集合中的函数渐近下界至少是 $n^2$ 的量级，即 $\Omega(n) + \Omega(n^2) = \Omega(n^2)$。

**矛盾点：**
函数 $h(n) = n$ 属于右边集合 $\Omega(n)$，但不属于左边集合 $\Omega(n^2)$（因为 $n$ 的增长速度慢于 $n^2$，不满足 $n \ge c \cdot n^2$）。

因此，左边集合 $\neq$ 右边集合，等式**不成立**。

### 2. 理论分析

在渐近记号的集合运算中，通常有以下性质：
$$\Omega(f(n)) + \Omega(g(n)) = \Omega(\max(f(n), g(n)))$$

已知前提 $g(n) = \Omega(f(n))$，这意味着 $g(n)$ 的渐近增长速度**至少**与 $f(n)$ 一样快（即 $g(n)$ 是主导项或两者同阶）。因此：
$$\max(f(n), g(n)) = \Theta(g(n))$$
所以左边实际上等于 $\Omega(g(n))$。

原命题等价于问：若 $g(n) = \Omega(f(n))$，是否一定有 $\Omega(g(n)) = \Omega(f(n))$？
*   由 $g(n) = \Omega(f(n))$ 可知 $\Omega(g(n)) \subseteq \Omega(f(n))$（左边是右边的子集）。
*   但要使集合相等，还需要 $f(n) = \Omega(g(n))$（即 $f(n) = \Theta(g(n))$）。

题目仅给出了 $g(n) = \Omega(f(n))$，并未排除 $g(n)$ 严格大于 $f(n)$ 的情况（如反例中的 $n^2$ 与 $n$）。当 $g(n)$ 严格大于 $f(n)$ 时，$\Omega(g(n))$ 是 $\Omega(f(n))$ 的**真子集**，等式自然不成立。

### 结论
**$\Omega(f(n))+\Omega(g(n))=\Omega(f(n))$ 不成立。** 只有当 $f(n) = \Theta(g(n))$ 时，该等式才成立。