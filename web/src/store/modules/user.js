import { getRoleInfo, login, logout } from "@/api/user.js";
import { getToken, setToken, removeToken } from "@/utils/token";
import { isArray, isString } from "lodash";
import { resetRouter } from "@/router";

const state = () => ({
  token: getToken(),
  username: "",
  dep_name: "",
  role_name: "",
  userid: "",
  avatar: "https://i.gtimg.cn/club/item/face/img/2/15922_100.gif",
});

const getters = {
  token: (state) => state.token,
  avatar: (state) => state.avatar,
  userid: (state) => state.userid,
  username: (state) => state.username,
  dep_name: (state) => state.dep_name,
  role_name: (state) => state.role_name,
};

const mutations = {
  /**
   * @description 设置token
   */

  setToken(state, token) {
    state.token = token;
    // 写入本地缓存
    setToken(token);
  },
  /**
   * @description 设置用户名
   * @param {*} state
   * @param {*} username
   */
  setUsername(state, username) {
    state.username = username;
  },
  /**
   * @description 设置用户id
   * @param {*} state
   * @param {*} userid
   */
  setUserid(state, userid) {
    state.userid = userid
  },
  /**
   * @description 设置头像
   * @param {*} state
   * @param {*} avatar
   */
  setAvatar(state, avatar) {
    state.avatar = avatar;
  },
  /**
   * @description 设置科室
   * @param {*} state
   * @param {*} dep_name
   */
  setDepName(state, dep_name) {
    state.dep_name = dep_name
  },
   /**
   * @description 设置角色
   * @param {*} state
   * @param {*} role_name
   */
  setRoleName(state, role_name) {
    state.role_name = role_name
  },
};

const actions = {
  /**
   * @description 登录
   * @param {*} { commit }
   * @param {*} userInfo
   */
  async login({ commit }, userInfo) {
    const {
      datas: { token, status },
    } = await login(userInfo);
      commit("setToken", token);
      return status
  },
  /**
   * @description 退出
   * @param {*} { dispatch }
   */
  async logout({ dispatch }) {
    await logout();
    await dispatch("resetAll");
  },
  /**
   * @description 用户接口信息
   * @param {*} { commit dispatch state}
   */
  async getUserInfo({ commit, dispatch }) {
    const searchData = { token_value: localStorage.getItem("pro-token") };
    const {
      datas: { name, id, menu, dep_name, role_name, ability, avatar },
    } = await getRoleInfo(searchData);
    // 检查返回数据是否正确 无对应参数 使用默认值
    if (
      (name && !isString(name)) ||
      (avatar && !isString(avatar)) ||
      (menu && !isArray(menu)) ||
      (ability && !isArray(ability))
    ) {
      const err = "接口异常,请检查返回JSON格式是否正确";
      throw err;
    } else {
      localStorage.setItem("pro-token", `${name}-token`);
      if (name) commit("setUsername", name);
      if (id) commit("setUserid", id);
      if (avatar) commit("setAvatar", avatar);
      if (dep_name) commit("setDepName", dep_name);
      if (role_name) commit("setRoleName", role_name);
      if (menu) dispatch("acl/setRole", menu, { root: true });
      if (ability) dispatch("acl/setAbility", ability, { root: true });
    }
  },
  /**
   * @description 重置token roles router tabsBar等
   * @params {*} { commit, dispatch }
   */
  async resetAll({ commit, dispatch }) {
    commit("setUsername", "游客");
    commit(
      "setAvatar",
      "https://i.gtimg.cn/club/item/face/img/2/15922_100.gif"
    );
    commit('routes/setRoutes', [], { root: true })

    await dispatch("setToken", "");
    await dispatch('acl/setFull', false, { root: true })
    await dispatch('acl/setRole', [], { root: true })
    await dispatch('acl/setAbility', [], { root: true })
    await dispatch('tabs/delAllVisitedRoutes', null, { root: true })
    await resetRouter();
    removeToken();
  },
  setToken({ commit }, token) {
    commit("setToken", token);
  },
};

export default { state, getters, mutations, actions };
