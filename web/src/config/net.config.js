/**
 * @description 导出网络配置
 */

module.exports = {
  baseURL: "http://10.1.1.181:5006/back",
  // baseURL: "http://127.0.0.1:4523/m1/4471042-4117429-default",
  // baseURL: "http://10.1.1.181:6789",
  contentType: "application/json;charset=UTF-8",
  requestTimeout: 20000,
  // 操作code 支持String int
  successCode: [200, 0, "200", "0"],
  // 数组状态名称
  statusName: "code",
  // 状态信息的字段名称
  messageName: "msg",
};
