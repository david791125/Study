from pyecharts import Map, Geo

value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr = ["China", "Canada", "Brazil", "Russia", "United States"]

# 省和直辖市
province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9,
                         '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3,
                         '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': 1,
                         '其他': 1}
provice = list(province_distribution.keys())
values = list(province_distribution.values())

# 城市 -- 指定省的城市 xx市
city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市', '信阳市', '新乡市','武汉市']
values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1,6.1]

# 区县 -- 具体城市内的区县  xx县
#quxian = ['咸宁市', '宜昌市', '利川市', '荆州市', '通山县', '通城县','黄冈市']
#values3 = [3, 5, 7, 8, 2, 4,1]

quxian = ['通羊镇', '南林镇', '横石镇']
values3 = [3, 5, 7]

#map0 = Map("世界地图示例", width=1200, height=600)
#map0.add("世界地图", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000')
#map0.render(path="04-00世界地图.html")


# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
#map = Map("中国地图",'中国地图', width=1200, height=600)
#map.add("", provice, values, visual_range=[0, 50],  maptype='china', is_visualmap=True,visual_text_color='#000')
#map.show_config()
#map.render(path="04-01中国地图.html")

#map2 = Map("湖北地图",'湖北', width=1200, height=600)
#map2.add('湖北', city, values2, visual_range=[1, 10], maptype='湖北', is_visualmap=True, visual_text_color='#000')
#map2.show_config()
#map2.render(path="04-02湖北地图.html")

#map3 = Map("咸宁地图",'咸宁', width=1200, height=600)
#map3.add("咸宁", quxian, values3, visual_range=[1, 10], maptype='咸宁', is_visualmap=True,visual_text_color='#000')
#map3.render(path="咸宁.html")

#indexs = ['上海', '北京', '合肥', '哈尔滨', '广州', '成都', '无锡', '杭州', '武汉', '深圳', '西安', '郑州', '重庆', '长沙','咸宁']
#values = [4.07, 1.85, 4.38, 2.21, 3.53, 4.37, 1.38, 4.29, 4.1, 1.31, 3.92, 4.47, 2.40, 3.60,5]

#geo = Geo("全国主要城市空气质量评分", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
#geo.add("空气质量评分", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[0, 5],visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
#geo.show_config()
#geo.render(path="04-05空气质量评分.html")

#map3 = Map("海淀区",'海淀区', width=1200, height=600)
#map3.add("海淀区", quxian, values3, visual_range=[1, 10], maptype='海淀区', is_visualmap=True,visual_text_color='#000')
#map3.render(path="海淀区.html")

map3 = Map("黄大仙区地图",'黄大仙区', width=1200, height=600)
map3.add("黄大仙区", quxian, values3, visual_range=[1, 10], maptype='黄大仙区', is_visualmap=True,visual_text_color='#000')
map3.render(path="黄大仙区.html")