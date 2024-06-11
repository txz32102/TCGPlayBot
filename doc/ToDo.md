# 某群友
```txt
EPIC：ai算法&训练
user story：
1. 确认算法和所需数据结构
2. 根据现有模拟器制作match.json和step.json两个数据结构，用于ai和模拟器通信（可参考lpism的model分支的model文件夹中的实现）
3. 对接模拟器和算法，初步进行训练

EPIC：数据对接
user story：
1.一个能全量描述牌局当前状态的match.json，需要考虑信息对ai是否可见（对方手牌，牌库等信息）
2.一个能描述牌局进行的step.json，描述包括双方牌局的所有行动
3.保证基于初始界面的match.json和牌局的step.json，可以完整且唯一复现牌局进程

EPIC：数据采集
user story：
1. 研究下目前已发布的记牌器代码，实现直接读取并生成match以及step list
2. 联系下记牌器老哥，愿不愿意一起搞，弄个联网上传牌谱到服务器，可以使用记牌器用户的对局记录
3. 收集数据并处理数据，后续扔进ai搞监督学习
```