/**
 * @description: 封装通知
 * @author: sinvon
 * @create 2024年11月26日02:04:34
 */
import { ElNotification } from "element-plus";

// 全局样式定义
const styleElement = document.createElement("style");
styleElement.innerHTML = `
  .custom-notification {
    transition: width 0.3s, font-size 0.3s; /* 添加过渡效果 */
  }
`;
document.head.appendChild(styleElement);

/**
 * 显示通知
 * @param {string} title - 通知标题
 * @param {string} message - 通知内容
 * @param {'success' | 'warning' | 'info' | 'error'} [type='info'] - 通知类型
 * @param {'top-right' | 'top-left' | 'bottom-right' | 'bottom-left'} [position='top-right'] - 通知位置
 * @param {number} [width=300] - 通知框宽度（单位：px）
 * @param {number} [fontSize=14] - 字体大小（单位：px）
 * @param {number} [duration=3000] - 通知持续时间（单位：毫秒，设为 0 则永久显示）
 */
export const showNotification = (
    title,
    message,
    type = "info",
    position = "top-right",
    width = 300,
    fontSize = 14,
    duration = 3000
) => {
  // 动态生成唯一类名
  const customClass = `custom-notification-${Date.now()}`;

  // 更新或创建特定的通知样式
  const notificationStyle = document.querySelector(`.${customClass}`);
  if (notificationStyle) {
    notificationStyle.innerHTML = `
      .${customClass} {
        width: ${width}px !important;
        font-size: ${fontSize}px !important;
      }
    `;
  } else {
    const newStyle = document.createElement("style");
    newStyle.className = customClass;
    newStyle.innerHTML = `
      .${customClass} {
        width: ${width}px !important;
        font-size: ${fontSize}px !important;
      }
    `;
    document.head.appendChild(newStyle);
  }

  // 显示通知
  ElNotification({
    title,
    message,
    type,
    position,
    duration,
    customClass,
    onClose: () => {
      setTimeout(() => {
        const toRemove = document.querySelector(`.${customClass}`);
        if (toRemove) {
          toRemove.remove();
        }
      }, 350); // 确保过渡动画完成后再移除样式
    },
  });
};
/**
 使用示例：
import { showNotification } from './path/to/your/notificationService'; // 根据实际情况调整路径
// 成功类型的通知
showNotification('操作成功', '您的请求已成功处理！', 'success');

// 警告类型的通知
setTimeout(() => {
  showNotification('警告', '请检查您的输入信息是否正确。', 'warning', 'top-left', 350, 16);
}, 2000);

// 信息类型的通知
setTimeout(() => {
  showNotification('提示', '这是一个信息通知。', 'info', 'bottom-right', 400, 18, 5000);
}, 4000);

// 错误类型的通知
setTimeout(() => {
  showNotification('错误', '发生了一个错误，请稍后重试或联系管理员。', 'error', 'bottom-left', 500, 20, 0);
}, 6000);
*/
