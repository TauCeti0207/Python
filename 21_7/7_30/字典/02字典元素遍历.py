# 开发时间:  2021/7/30 19:14
scores = {'张三': 100,
          '你是': 98,
          '求其': 99, }
for item in scores:
    print(item, scores[item], scores.get(item))
