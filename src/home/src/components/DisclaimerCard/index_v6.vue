<template>
    <div>
      <el-card class="disclaimer-card" shadow="hover">
        <!-- 免责声明标题 -->
        <h2 class="disclaimer-title">⚠️ 免责声明</h2>
  
        <!-- 免责声明分隔线 -->
        <el-divider class="disclaimer-divider"></el-divider>
  
        <!-- 免责声明内容 -->
        <p class="disclaimer-text">• 本项目仅为技术展示和教育目的，所提供的影视资源爬取功能仅适用于合法的、公开可用的资源。我们不对任何非法内容的爬取或传播负责。用户应确保自己遵守相关法律法规，避免使用本工具进行侵犯版权的行为。</p>
        <p class="disclaimer-text">• 本项目不对爬取到的影视资源的可用性、准确性、完整性或合法性做出任何保证。用户使用本项目所爬取的资源时，应自行核实其合法性。本项目不承担任何因使用本工具所爑取的资源而导致的法律责任。</p>
        <p class="disclaimer-text">• 本项目不在任何服务器上存储用户的数据或爬取的资源。所有的爬取操作和数据处理都在本地进行。用户的个人信息、浏览记录等不被收集或存储。我们尊重用户隐私，并承诺不泄露用户数据。</p>
        <p class="disclaimer-text">• 本项目仅供个人学习和研究使用，严禁用于任何商业或违法活动。对于用户使用本软件过程中因操作不当、网络安全问题或其他原因导致的任何损失或法律责任，本项目作者不承担任何责任。</p>
        <p class="disclaimer-text">• 我们保留随时修改、更新本免责声明内容的权利，修改后的免责声明将会及时更新，并在本项目的官方网站或相关文档中公示。建议用户定期查看并遵守最新的免责声明内容。</p>
        <p class="disclaimer-text">• 用户在使用本项目时，必须遵守所在国家和地区的法律法规。如果您在使用过程中发现任何非法行为，请立即停止使用，并向相关机构报告。</p>
        <p class="disclaimer-text">• 本项目作者对于任何通过本工具爬取的资源或其使用所带来的任何形式的损失、法律责任、版权纠纷等不承担任何责任。</p>
      </el-card>
    </div>
  </template>
  
  <script lang="js" setup>
  const props = defineProps({})
  </script>
  
  <style lang="less" scoped>
  .disclaimer-card {
    // background-color: #fafafa;
    padding: 20px;
    border-radius: 10px;
    max-width: 600px;
    margin: 30px auto;
    position: relative;
    overflow: hidden; /* 防止悬浮时内容溢出 */
    transition: padding 0.5s cubic-bezier(0.4, 0, 0.2, 1), margin 0.5s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease-out;
    // box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 默认阴影 */
    // 隐藏边框
    border: none;
  }
  
  .disclaimer-title {
    font-size: 16px;
    font-weight: bold;
    color: #d66d66; /* 红色警告 */
    text-align: center;
    transition: opacity 0.3s ease;
  }
  
  /* 默认情况下隐藏分隔线和免责声明内容 */
  .disclaimer-divider,
  .disclaimer-text {
    opacity: 0;
    visibility: hidden;
    transform: translateY(20px); /* 初始位置稍微偏移 */
    transition: opacity 0.5s ease, visibility 0s 0.5s, transform 0.5s ease;
  }
  
  /* 鼠标悬浮时显示分隔线和免责声明内容 */
  .el-card:hover .disclaimer-divider,
  .el-card:hover .disclaimer-text {
    opacity: 1; /* 显示 */
    visibility: visible;
    transform: translateY(0); /* 恢复正常位置 */
    transition: opacity 0.5s ease, visibility 0s 0s, transform 0.5s ease; /* 鼠标悬浮时的过渡 */
  }
  
  /* 鼠标悬浮时卡片的尺寸变化 */
  .el-card:hover {
    padding-bottom: 50px; /* 调整卡片底部间距，给标题和分隔线空间 */
    margin-bottom: 40px; /* 增加底部外边距，使卡片内容向下展开 */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* 悬浮时增加阴影 */
    transition: padding-bottom 0.5s cubic-bezier(0.4, 0, 0.2, 1), margin-bottom 0.5s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease-out;
  }
  </style>
  