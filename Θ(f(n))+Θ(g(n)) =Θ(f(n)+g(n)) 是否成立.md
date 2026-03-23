结论是：**成立**。

即等式 $\Theta(f(n)) + \Theta(g(n)) = \Theta(f(n) + g(n))$ 是成立的（假设 $f(n)$ 和 $g(n)$ 是渐近非负函数）。

下面给出详细证明。为了证明两个集合相等，我们需要证明互相包含，即：
1.  $\Theta(f(n)) + \Theta(g(n)) \subseteq \Theta(f(n) + g(n))$
2.  $\Theta(f(n) + g(n)) \subseteq \Theta(f(n)) + \Theta(g(n))$

---

### 证明第一部分：$\Theta(f(n)) + \Theta(g(n)) \subseteq \Theta(f(n) + g(n))$

**证明：**
任取函数 $h(n) \in \Theta(f(n)) + \Theta(g(n))$。
根据定义，存在 $h_1(n) \in \Theta(f(n))$ 和 $h_2(n) \in \Theta(g(n))$，使得 $h(n) = h_1(n) + h_2(n)$。

由 $h_1(n) \in \Theta(f(n))$ 可知，存在常数 $a_1, a_2, n_1 > 0$，当 $n \ge n_1$ 时：
$$a_1 f(n) \le h_1(n) \le a_2 f(n)$$

由 $h_2(n) \in \Theta(g(n))$ 可知，存在常数 $b_1, b_2, n_2 > 0$，当 $n \ge n_2$ 时：
$$b_1 g(n) \le h_2(n) \le b_2 g(n)$$

取 $n_0 = \max(n_1, n_2)$。当 $n \ge n_0$ 时，将上述两个不等式相加：
$$a_1 f(n) + b_1 g(n) \le h_1(n) + h_2(n) \le a_2 f(n) + b_2 g(n)$$
即：
$$a_1 f(n) + b_1 g(n) \le h(n) \le a_2 f(n) + b_2 g(n)$$

令 $c_{min} = \min(a_1, b_1)$，$c_{max} = \max(a_2, b_2)$。
由于 $f(n), g(n)$ 渐近非负，我们有：
$$c_{min}(f(n) + g(n)) \le a_1 f(n) + b_1 g(n)$$
$$a_2 f(n) + b_2 g(n) \le c_{max}(f(n) + g(n))$$

因此：
$$c_{min}(f(n) + g(n)) \le h(n) \le c_{max}(f(n) + g(n))$$

根据 $\Theta$ 的定义，这意味着 $h(n) \in \Theta(f(n) + g(n))$。
故 $\Theta(f(n)) + \Theta(g(n)) \subseteq \Theta(f(n) + g(n))$ 得证。

---

### 证明第二部分：$\Theta(f(n) + g(n)) \subseteq \Theta(f(n)) + \Theta(g(n))$

**证明：**
任取函数 $h(n) \in \Theta(f(n) + g(n))$。
根据定义，存在常数 $k_1, k_2, n_0 > 0$，当 $n \ge n_0$ 时：
$$k_1 (f(n) + g(n)) \le h(n) \le k_2 (f(n) + g(n))$$

我们需要构造两个函数 $h_1(n)$ 和 $h_2(n)$，使得 $h_1 \in \Theta(f(n))$，$h_2 \in \Theta(g(n))$，且 $h = h_1 + h_2$。
（假设对于足够大的 $n$，$f(n) + g(n) > 0$）

构造如下：
$$h_1(n) = \frac{f(n)}{f(n) + g(n)} h(n)$$
$$h_2(n) = \frac{g(n)}{f(n) + g(n)} h(n)$$

显然 $h_1(n) + h_2(n) = \frac{f(n) + g(n)}{f(n) + g(n)} h(n) = h(n)$。

接下来验证 $h_1(n) \in \Theta(f(n))$：
将 $h(n)$ 的界限代入 $h_1(n)$ 的表达式：
$$h_1(n) \ge \frac{f(n)}{f(n) + g(n)} \cdot k_1 (f(n) + g(n)) = k_1 f(n)$$
$$h_1(n) \le \frac{f(n)}{f(n) + g(n)} \cdot k_2 (f(n) + g(n)) = k_2 f(n)$$
即 $k_1 f(n) \le h_1(n) \le k_2 f(n)$，所以 $h_1(n) \in \Theta(f(n))$。

同理可证 $h_2(n) \in \Theta(g(n))$：
$$h_2(n) \ge \frac{g(n)}{f(n) + g(n)} \cdot k_1 (f(n) + g(n)) = k_1 g(n)$$
$$h_2(n) \le \frac{g(n)}{f(n) + g(n)} \cdot k_2 (f(n) + g(n)) = k_2 g(n)$$
即 $k_1 g(n) \le h_2(n) \le k_2 g(n)$，所以 $h_2(n) \in \Theta(g(n))$。

因为 $h(n)$ 可以表示为一个 $\Theta(f(n))$ 中的函数与一个 $\Theta(g(n))$ 中的函数之和，所以 $h(n) \in \Theta(f(n)) + \Theta(g(n))$。
故 $\Theta(f(n) + g(n)) \subseteq \Theta(f(n)) + \Theta(g(n))$ 得证。

---

### 总结
综上所述，两个集合互相包含，因此等式成立：
$$\Theta(f(n)) + \Theta(g(n)) = \Theta(f(n) + g(n))$$
