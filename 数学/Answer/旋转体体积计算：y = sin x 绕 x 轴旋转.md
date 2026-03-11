## 一、问题描述

求函数 $y = \sin x$（$0 \le x \le \pi$）与 $x$ 轴所围区域绕 $x$ 轴旋转一周所得旋转体的体积。

---

## 二、圆盘法建立定积分

**核心思想**：在 $x$ 处取一微元薄片，其截面为圆盘，半径为 $y = \sin x$，厚度为 $dx$。

$$dV = \pi y^2 \, dx = \pi \sin^2 x \, dx$$

对 $x$ 从 $0$ 到 $\pi$ 积分，得体积的严格定积分表达式：

$$\boxed{V = \pi \int_0^{\pi} \sin^2 x \, dx}$$

---

## 三、积分计算

### 第一步：降幂公式（半角公式）

由三角恒等式：

$$\sin^2 x = \frac{1 - \cos 2x}{2}$$

代入积分：

$$V = \pi \int_0^{\pi} \frac{1 - \cos 2x}{2} \, dx$$

### 第二步：拆分积分

$$V = \frac{\pi}{2} \int_0^{\pi} (1 - \cos 2x) \, dx = \frac{\pi}{2} \left[ \int_0^{\pi} 1 \, dx - \int_0^{\pi} \cos 2x \, dx \right]$$

### 第三步：逐项计算

**第一项**：

$$\int_0^{\pi} 1 \, dx = \Big[ x \Big]_0^{\pi} = \pi - 0 = \pi$$

**第二项**：

$$\int_0^{\pi} \cos 2x \, dx = \left[ \frac{\sin 2x}{2} \right]_0^{\pi} = \frac{\sin 2\pi}{2} - \frac{\sin 0}{2} = \frac{0}{2} - \frac{0}{2} = 0$$

### 第四步：合并结果

$$V = \frac{\pi}{2} \left( \pi - 0 \right) = \frac{\pi^2}{2}$$

---

## 四、最终结果

$$\boxed{V = \dfrac{\pi^2}{2}}$$

---

## 五、直观验证与理解

| 对比项 | 圆柱（半径1，高$\pi$） | 本旋转体 |
| :--- | :--- | :--- |
| 体积 | $\pi r^2 h = \pi^2$ | $\dfrac{\pi^2}{2}$ |
| 比值 | $1$ | $\dfrac{1}{2}$ |

旋转体体积恰好是其外接圆柱体积的 **一半**，这与 $\sin^2 x$ 在 $[0, \pi]$ 上的平均值恰为 $\dfrac{1}{2}$ 完全吻合：

$$\frac{1}{\pi} \int_0^{\pi} \sin^2 x \, dx = \frac{1}{\pi} \cdot \frac{\pi}{2} = \frac{1}{2}$$

这提供了一个优美的几何直觉：**$\sin^2 x$ 的平均高度决定了旋转体占外接圆柱的比例**。$\blacksquare$