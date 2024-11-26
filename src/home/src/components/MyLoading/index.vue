<template>
  <div>
    <h1 class="loading">{{ loadingText }}</h1>
  </div>
</template>

<script lang="js" setup>
const props = defineProps({
  loadingText: {
    type: String,
    default: '加载中...',  // 如果父组件没有传递值，则使用默认值
  },
})
</script>

<style lang="less" scoped>
.loading {
  /* 基本样式 */
  text-align: center;
  font-size: 18px;
  color: #4a90e2; /* 初始颜色，渐变动画会覆盖它 */
  margin-top: 20px;
  position: relative;
  display: inline-block;
  font-weight: bold;
  white-space: nowrap;
  animation: waveEffect 1.5s infinite, colorChange 2s infinite,
    shake 0.5s infinite alternate;
}

/* 波纹扭曲效果 */
@keyframes waveEffect {
  0% {
    transform: skewX(0deg); /* 初始状态，文字不偏移 */
    text-shadow: 0 0 2px rgba(0, 0, 0, 0.1), 0 0 5px rgba(0, 0, 0, 0.1); /* 较轻的阴影 */
  }
  25% {
    transform: skewX(-5deg); /* 向左倾斜，模拟波纹 */
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgba(0, 0, 0, 0.1); /* 更柔和的阴影 */
  }
  50% {
    transform: skewX(0deg); /* 恢复水平 */
    text-shadow: 0 0 2px rgba(0, 0, 0, 0.1), 0 0 5px rgba(0, 0, 0, 0.1);
  }
  75% {
    transform: skewX(5deg); /* 向右倾斜，模拟波纹 */
    text-shadow: -1px -1px 2px rgba(0, 0, 0, 0.1), 0 0 8px rgba(0, 0, 0, 0.1);
  }
  100% {
    transform: skewX(0deg); /* 恢复水平 */
    text-shadow: 0 0 2px rgba(0, 0, 0, 0.1), 0 0 5px rgba(0, 0, 0, 0.1);
  }
}

/* 文字颜色渐变（七种低饱和度颜色） */
@keyframes colorChange {
  0% {
    color: #9a5e68; /* 淡粉色 */
  }
  14% {
    color: #a17951; /* 柔和橙色 */
  }
  28% {
    color: #9b9050; /* 柔和黄色 */
  }
  42% {
    color: #4e8d60; /* 清新绿色 */
  }
  57% {
    color: #43668c; /* 温和蓝色 */
  }
  71% {
    color: #6a5487; /* 暖紫色 */
  }
  85% {
    color: #865d5a; /* 柔和红色 */
  }
  100% {
    color: #8c545d; /* 返回到淡粉色 */
  }
}

/* 文字抖动效果 */
@keyframes shake {
  0% {
    transform: translateX(0); /* 初始位置 */
  }
  25% {
    transform: translateX(-3px); /* 更小的抖动 */
  }
  50% {
    transform: translateX(3px); /* 更小的抖动 */
  }
  75% {
    transform: translateX(-3px); /* 更小的抖动 */
  }
  100% {
    transform: translateX(0); /* 恢复位置 */
  }
}
</style>
