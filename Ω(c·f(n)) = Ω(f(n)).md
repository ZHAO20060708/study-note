我们将集合 $A = \Omega(c \cdot f(n))$ 和集合 $B = \Omega(f(n))$。要证明 $A = B$，我们需要证明 $A \subseteq B$ 且 $B \subseteq A$。

---

### 证明 $\Omega(c \cdot f(n)) \subseteq \Omega(f(n))$

**假设：** 任取函数 $g(n) \in \Omega(c \cdot f(n))$。

**推导：**
根据定义，存在正常数 $n_1$ 和 $k_1$，使得对于所有 $n \ge n_1$，有：
$$g(n) \ge k_1 \cdot (c \cdot f(n))$$

利用乘法结合律，我们可以将其重写为：
$$g(n) \ge (k_1 \cdot c) \cdot f(n)$$

令 $k_2 = k_1 \cdot c$。
因为 $k_1 > 0$ 且 $c > 0$，所以 $k_2 > 0$ 也是一个正常数。

因此，存在正常数 $n_1$ 和 $k_2$，使得对于所有 $n \ge n_1$，有：
$$g(n) \ge k_2 \cdot f(n)$$

**结论：**
根据 $\Omega$ 的定义，这意味着 $g(n) \in \Omega(f(n))$。
所以，$\Omega(c \cdot f(n)) \subseteq \Omega(f(n))$。

---

### 证明 $\Omega(f(n)) \subseteq \Omega(c \cdot f(n))$

**假设：** 任取函数 $g(n) \in \Omega(f(n))$。

**推导：**
根据定义，存在正常数 $n_2$ 和 $k_3$，使得对于所有 $n \ge n_2$，有：
$$g(n) \ge k_3 \cdot f(n)$$

为了构造出 $c \cdot f(n)$ 的形式，我们将不等式右边乘以 $\frac{c}{c}$（因为 $c > 0$，所以 $\frac{c}{c} = 1$）：
$$g(n) \ge k_3 \cdot \frac{c}{c} \cdot f(n)$$
$$g(n) \ge \frac{k_3}{c} \cdot (c \cdot f(n))$$

令 $k_4 = \frac{k_3}{c}$。
因为 $k_3 > 0$ 且 $c > 0$，所以 $k_4 > 0$ 也是一个正常数。

因此，存在正常数 $n_2$ 和 $k_4$，使得对于所有 $n \ge n_2$，有：
$$g(n) \ge k_4 \cdot (c \cdot f(n))$$

**结论：**
根据 $\Omega$ 的定义，这意味着 $g(n) \in \Omega(c \cdot f(n))$。
所以，$\Omega(f(n)) \subseteq \Omega(c \cdot f(n))$。

---

### 总结

由上述两步证明可知：
1. $\Omega(c \cdot f(n)) \subseteq \Omega(f(n))$
2. $\Omega(f(n)) \subseteq \Omega(c \cdot f(n))$

根据集合相等的定义，我们可以得出结论：
$$\Omega(c \cdot f(n)) = \Omega(f(n))$$

**证毕。**