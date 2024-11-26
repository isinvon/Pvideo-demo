/**
 * @description: 封装通知
 * @author: sinvon
 * @create 2024年11月26日02:04:34
 */
import { ElNotification } from "element-plus";

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
  const customClass = `custom-notification-${Date.now()}`; // 动态生成唯一类名

  // 创建样式
  const styleElement = document.createElement("style");
  styleElement.innerHTML = `
    .${customClass} {
      width: ${width}px !important;
      font-size: ${fontSize}px !important;
    }
  `;
  document.head.appendChild(styleElement);

  // 显示通知
  ElNotification({
    title,
    message,
    type,
    position,
    duration,
    customClass,
    onClose: () => {
      document.head.removeChild(styleElement); // 清理样式
    },
  });
};
