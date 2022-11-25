# 一个为v2ex写的抽奖脚本

 抽奖的原理：
  根据回复的用户头像+用户 id 计算 md5 值，抽奖当天收盘时的上证、深证和创业板指数计算 md5 值，两值之差的绝对值进行排序，越小排名越前，选择前者作为获奖用户；
  由于md5哈希算法本身的特点，即使存在轻微的干扰，最后的结果差异也会很大。选择大盘指数的哈希值可以最大程度保证抽奖的公平性
  
  特别感谢，来自 https://zhuanlan.zhihu.com/p/49227337
  
