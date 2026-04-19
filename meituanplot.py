import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --------------------------
# 全局设置（中文不乱码）
# --------------------------
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (8, 4)
plt.rcParams['savefig.dpi'] = 300

# ==========================
# 图1：业务线订单占比 & ROI
# ==========================
def plot1_business_roi():
    business = ['外卖', '到餐', '酒店', '闪购', '乐生活']
    order_ratio = [54.9, 27.9, 8.6, 5.2, 3.4]
    roi = [2.8, 4.2, 3.5, 1.9, 1.5]

    fig, ax1 = plt.subplots()
    ax1.bar(business, order_ratio, color='#ff9f00', label='订单占比(%)')
    ax1.set_ylabel('订单占比(%)')
    ax2 = ax1.twinx()
    ax2.plot(business, roi, 'r-o', linewidth=3, label='ROI')
    ax2.set_ylabel('ROI')
    plt.title('图1 各业务线订单占比与ROI分布')
    plt.savefig('图1_业务订单占比_ROI.png', bbox_inches='tight')
    plt.show()

# ==========================
# 图2：时段订单占比 & 转化率
# ==========================
def plot2_time_distribution():
    time_slot = ['早间', '午间', '下午', '晚间', '深夜']
    order_ratio = [10.5, 18.7, 20.1, 42.5, 8.2]
    convert_rate = [18.5, 32.1, 35.6, 45.2, 12.1]

    plt.bar(time_slot, order_ratio, color='#2a9d8f', label='订单占比(%)')
    plt.plot(time_slot, convert_rate, 'r-o', linewidth=3, label='自然转化率(%)')
    plt.legend()
    plt.title('图2 各时段订单占比与自然转化率')
    plt.savefig('图2_时段分布_转化率.png', bbox_inches='tight')
    plt.show()

# ==========================
# 图3：城市价格敏感度
# ==========================
def plot3_city_sensitivity():
    city = ['北京', '上海', '广州', '深圳', '成都', '重庆']
    sensitive = [35, 32, 38, 40, 65, 68]
    order_cnt = [243, 226, 189, 171, 81, 78]

    plt.bar(city, sensitive, color='#e76f51')
    plt.title('图3 各城市价格敏感度(%)')
    plt.savefig('图3_城市价格敏感度.png', bbox_inches='tight')
    plt.show()

# ==========================
# 图4：券型核销率对比
# ==========================
def plot4_coupon_type():
    coupon = ['免费券', '付费券', '通用券']
    rate = [78.5, 62.3, 55.1]

    plt.bar(coupon, rate, color='#7209b7')
    plt.ylabel('核销率(%)')
    plt.title('图4 不同券型核销率对比')
    plt.savefig('图4_券型核销率.png', bbox_inches='tight')
    plt.show()

# ==========================
# 图5：转化漏斗
# ==========================
def plot5_funnel():
    steps = ['点击', '领券', '使用', '下单']
    values = [270, 156, 93, 42]

    plt.bar(steps, values, color='#023e8a')
    plt.title('图5 用户补贴触达转化漏斗')
    plt.savefig('图5_转化漏斗.png', bbox_inches='tight')
    plt.show()

# ==========================
# 图6：五维耦合热力图简化版
# ==========================
def plot6_couple_matrix():
    data = np.array([[90, 75, 65, 30],
                     [60, 85, 70, 40],
                     [50, 70, 68, 35]])
    plt.imshow(data, cmap='YlOrRd')
    plt.colorbar()
    plt.title('图6 行业-时间耦合热力图')
    plt.savefig('图6_耦合热力图.png', bbox_inches='tight')
    plt.show()

# ==========================
# 图7：优化前后指标对比
# ==========================
def plot7_before_after():
    indicators = ['ROI', '跨品类转化率', '核销率']
    before = [2.5, 18.2, 68.5]
    after = [3.8, 29.5, 82.1]

    x = np.arange(len(indicators))
    width = 0.35
    plt.bar(x - width/2, before, width, label='优化前', color='#999')
    plt.bar(x + width/2, after, width, label='优化后', color='#ff6b6b')
    plt.legend()
    plt.title('图7 预算优化前后核心指标对比')
    plt.savefig('图7_优化前后对比.png', bbox_inches='tight')
    plt.show()

# ==========================
# 一键生成所有图表
# ==========================
if __name__ == '__main__':
    plot1_business_roi()
    plot2_time_distribution()
    plot3_city_sensitivity()
    plot4_coupon_type()
    plot5_funnel()
    plot6_couple_matrix()
    plot7_before_after()