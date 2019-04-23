from pyecharts import Bar
data =[("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
data1 =[("海门", 1), ("鄂尔多斯", 2), ("招远", 3), ("舟山", 4), ("齐齐哈尔", 5), ("盐城", 6)]
bar = Bar("标记线和标记点示例")
attr, value  =bar.cast(data)
attr, value1 =bar.cast(data1)
bar.add("商家A", attr, value, mark_point=["average"])
bar.add("商家B", attr, value1, mark_line=["min", "max"])
bar.render()

from pyecharts import Bar
bar = Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, value)
bar.add("商家B", attr, value1, is_convert=True)
bar.render("pic_8.html")