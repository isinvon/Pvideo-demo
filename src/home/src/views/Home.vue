<template>
  <div class="container scroll-container">
    <!-- 左上角的1/4圆按钮 -->
    
    <a href="https://github.com/isinvon/Pvideo-demo" target="_blank" class="github-link">
      <button class="quarter-circle-btn">
        <span class="icon-container">
          <Icon icon="grommet-icons:github" />
        </span>
      </button>
    </a>

    <el-input
      v-model="searchQuery"
      placeholder="请输入要搜索的影片"
      class="search-input"
      clearable
    >
      <template #append>
        <el-button @click="searchMovies" class="search-button"> 🔍 </el-button>
      </template>
    </el-input>

    <!-- 加载动画 -->
     <MyLoading v-if="isLoading" :loadingText="loadingText"/>

    <el-table
      v-else-if="filteredMovies.length"
      :data="filteredMovies"
      :key="tableKey"
      class="movie-table"
      border
    >
      <!-- 资源名称列 -->
      <el-table-column label="资源名称" prop="资源名称" width="350">
        <template #default="scope">
          <span class="movie-title">{{ scope.row.资源名称 }}</span>
        </template>
      </el-table-column>

      <!-- 资源链接列 -->
      <el-table-column label="资源链接">
        <template #default="scope">
          <el-link
            v-for="(link, index) in splitAndParseLink(scope.row.资源链接)"
            :key="index"
            :href="link"
            target="_blank"
            class="movie-link"
          >
          <!-- 判断链接内容，显示不同的文本 -->
          <span v-if="link.includes('baidu')">百度云: {{ link }}</span>
          <span v-else-if="link.includes('xunlei')">迅雷: {{ link }}</span>
          <span v-else-if="link.includes('alispanan')">阿里云: {{ link }}</span>
          <span v-else-if="link.includes('quark')">夸克: {{ link }}</span>
          <span v-else-if="link.includes('m3u8') && index === 0">
            <p>复制链接到<a href="https://m3u8-player.com/" target="_blank" style="color: #4a90e2">https://m3u8-player.com/</a>输入框即可播放</p>
          </span>
            <span v-else-if="link.includes('m3u8') && index === 0">
            {{ link }}
          </span>
          <span v-else-if="link.includes('m3u8') && index !== 0">{{ link }}</span>
          <span v-else>其他: {{ link }}</span>
          </el-link>
        </template>
      </el-table-column>
    </el-table>

    <!-- 无数据提示 -->
    <div v-else>
      <el-empty description="未找到相关资源" />
      <!-- 免责声明 -->
      <DisclaimerCard class="disclaimer-card"/>
    </div>
  </div>
</template>

<script setup>
/**
 * @description: 主页
 * @author: sinvon
 * @create 2024年11月26日02:04:34
*/
import { onMounted, onUnmounted, ref } from "vue";
import { getMovieList } from "../service/getMovieList";
import { showNotification } from "../utils/notification.js";
import { Icon } from '@iconify/vue';

import DisclaimerCard from "../components/DisclaimerCard";
import MyLoading from "../components/MyLoading";

const searchQuery = ref(""); // 搜索框输入的内容
const filteredMovies = ref([]); // 存储过滤后的电影列表
const tableKey = ref(0); // 用于更新表格
const isLoading = ref(false); // 控制加载动画
const loadingText = ref("加载中"); // 动态加载文本
let loadingInterval = null; // 控制动态点的定时器
const isHovered = ref(false);// 定义悬浮状态

const searchMovies = async () => {
  const query = searchQuery.value.trim();
  if (query) {
    startLoading(); // 启动加载动画
    try {
      // 从后端调用MovieList
      const movieList = JSON.parse(await pywebview.api.showFinalList(name = query))
      filteredMovies.value = movieList; // 更新电影列表
      if (movieList.length === 0) {
        filteredMovies.value = []; // 没有匹配的电影时清空列表
        showNotification("", "未找到相关资源", "warning", "top-right", 200, 16, 2000);
      }else{
        showNotification("", `搜索到 ${movieList.length} 条资源`, "success", "top-right", 200, 16, 2000);
      }
    } catch (error) {
      console.error("获取电影列表失败:", error);
      filteredMovies.value = []; // 出错时清空
      showNotification("", `搜索失败, 报错${error}`, "error", "top-right", 200, 16, 3000);
    } finally {
      stopLoading(); // 停止加载动画
    }
  } else {
    filteredMovies.value = []; // 没有输入时清空列表
  }
};

const startLoading = () => {
  isLoading.value = true;
  loadingText.value = "加载中";
  let dots = 0;
  loadingInterval = setInterval(() => {
    dots = (dots + 1) % 4; // 循环控制点的数量
    loadingText.value = "加载中" + ".".repeat(dots);
  }, 500);
};

const stopLoading = () => {
  isLoading.value = false;
  clearInterval(loadingInterval);
  loadingInterval = null;
};

// 解析资源链接
const splitAndParseLink = (links) => {
  // 如果links是字符串
  if (typeof links === 'string') {
     // 使用正则表达式提取所有的 https 链接
    const regex = /https:\/\/[^\s]+/g;
    // 匹配所有符合条件的链接，并返回一个数组
    const result = links.match(regex);
    return result || []; // 如果没有找到有效链接，返回空数组
  }
  // 如果links是数组
  if (Array.isArray(links)) {
    // 遍历数组，提取每个链接
    return links.flatMap(link => {
      // 使用正则表达式提取所有的 https 链接
      const regex = /https:\/\/[^\s]+/g;
      // 匹配所有符合条件的链接，并返回一个数组
      return link.match(regex) || [];
    });
  }
  return [];
};

// 防止 ResizeObserver 警告
const updateTableKey = () => {
  tableKey.value++;
};

onMounted(() => {
  window.addEventListener("resize", updateTableKey);
});
onUnmounted(() => {
  window.removeEventListener("resize", updateTableKey);
});
</script>

<style lang="less" scoped>
.container {
  margin: 0 auto;
  padding: 20px;
  border-radius: 10px;
}

.search-input {
  margin-top: 10px;
  width: 100%;
  max-width: 500px;
  border-radius: 8px;
  background-color: #f7f7f7;
  color: #616161;
  border: 1px solid #e0e0e0;
  transition: background-color 0.3s ease;
}

.search-input:focus {
  background-color: #ffffff;
  border-color: #ccc;
}

.movie-table {
  margin-top: 20px;
  border-radius: 8px;
  overflow: hidden;
  background-color: #ffffff;
}

/* 表头 */
.movie-table .el-table__header {
  background-color: #f1f1f1;
  color: #4a4a4a;
  font-weight: bold;
  text-align: center;
}

/* 表格行 */
.movie-table .el-table__body {
  background-color: #ffffff;
  color: #4a4a4a;
}

.movie-table .el-table__row:hover {
  background-color: #f9f9f9;
}

.movie-title {
  color: #4a4a4a;
  font-weight: bold;
  text-transform: capitalize;
}

.movie-link {
  color: #616161;
  text-decoration: none;
  transition: color 0.3s ease;
  display: block; /* 每个链接独占一行 */
  margin-bottom: 5px;
}
.movie-link:hover {
  color: #58aecb;
}

/* 空状态样式 */
.el-empty {
  margin-top: 20px;
  color: #999;
  font-weight: bold;
}

.disclaimer-card {
  margin-top: -50px;
}

/* 左上角1/4圆形按钮样式 */
.quarter-circle-btn {
  position: absolute;
  top: -35px;  /* 向上移动半个直径 */
  left: -35px; /* 向左移动半个直径 */
  width: 70px; /* 圆的直径 */
  height: 70px; /* 圆的直径 */
  background-color: #aaaaaa60; /* 按钮背景颜色 */
  border: none;
  border-radius: 50%; /* 将按钮变成圆形 */
  clip-path: polygon(100% 50%, 50% 50%, 50% 100%, 100% 100%); /* 取右下角1/4圆 */
  cursor: pointer;
  transition: transform 0.3s ease, background-color 0.3s ease;
}

/* 按钮悬浮效果 */
.quarter-circle-btn:hover {
  transform: scale(1.5); /* 放大动画 */
  background-color: #c68de3; /* 悬浮时颜色变化 */
}

/* 图标容器样式 */
.icon-container {
  position: absolute;
  top: 38%; /* 垂直居中 */
  left: 35%; /* 水平居中 */
  transform: translate(16.8px, 16.8px); /* 调整到1/4圆的几何中心 */
}

/* 图标样式 */
.icon-container .icon {
  display: inline-block;
  color: white; /* 调整图标颜色 */
}
</style>
