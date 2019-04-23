from pyecharts import Scatter, EffectScatter, Grid,Bar
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter(width=1200)
scatter.add("散点图示例", v1, v2, legend_pos="70%")
es = EffectScatter()
es.add(
    "动态散点图示例",
    [11, 11, 15, 13, 12, 13, 10],
    [1, -2, 2, 5, 3, 2, 0],
    effect_scale=6,
    legend_pos="20%",
)

grid = Grid()
grid.add(scatter, grid_left="60%")
grid.add(es, grid_right="60%")
grid.render("pic_grid.html")