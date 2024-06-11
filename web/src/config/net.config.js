/**
 * @description 导出网络配置
 */

module.exports = {
  baseURL: process.env.VUE_APP_BASE_API,
  // baseURL: "http://172.18.3.160:9003/api",
  // baseURL: "http://10.1.1.181:5006/back",
  // baseURL: "http://10.1.1.46:9003/api",
  contentType: "application/json;charset=UTF-8",
  requestTimeout: 20000,
  // 操作code 支持String int
  successCode: [200, 0, "200", "0"],
  // 数组状态名称
  statusName: "code",
  // 状态信息的字段名称
  messageName: "msg",
};
