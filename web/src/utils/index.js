/**
 * @description 格式化时间
 * @param dateString
 * @returns {string}
 */

export function formatDate(dateString) {
  // 使用 Date 对象解析日期时间字符串
  const date = new Date(dateString);

  // 获取年、月、日，并确保月和日是两位数字
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const day = date.getDate().toString().padStart(2, "0");

  // 返回格式化的日期字符串
  return `${year}-${month}-${day}`;
}