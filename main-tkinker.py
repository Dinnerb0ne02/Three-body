import tkinter as tk

# 模拟参数设置
num_iterations = 114514  # 模拟的迭代次数 (可调)
dt = 0.1  # 时间步长

# 初始化位置和速度 (可调)
positions = [[300, 353], [100, 183], [300, 200]]
velocities = [[-0.1, -0.1], [0, 0.05], [-0.05, 0.1]]

# 创建窗口和画布
root = tk.Tk()
root.title("Three-body motion simulation")
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# 进行模拟
for _ in range(num_iterations):
    for i in range(3):
        acceleration = [0, 0]
        for j in range(3):
            if i != j:
                dx = positions[j][0] - positions[i][0]
                dy = positions[j][1] - positions[i][1]
                r = (dx ** 2 + dy ** 2) ** 1.5
                acceleration[0] += dx / r
                acceleration[1] += dy / r

        velocities[i][0] += acceleration[0] * dt
        velocities[i][1] += acceleration[1] * dt
        positions[i][0] += velocities[i][0] * dt
        positions[i][1] += velocities[i][1] * dt

    # 清空画布并重新绘制圆形
    canvas.delete("all")
    for i in range(3):
        x, y = positions[i]
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")

    # 更新画面
    root.update()

# 关闭窗口

# auther: Dinnerb0ne
# email: tomma_2022@outlook.com or tomma_20210919github@hotmail.com (Not commonly used)