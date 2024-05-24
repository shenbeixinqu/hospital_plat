import request from "@/utils/request";

export function login(data) {
  return request({
    url: "/login",
    method: "POST",
    data,
  });
}

export function register(data) {
  return request({
    url: "/register",
    method: "POST",
    data,
  });
}

export function logout(data) {
  return request({
    url: "/logout",
    method: "POST",
    data,
  });
}

export function getRoleInfo(params) {
  return request({
    url: "/userInfo",
    method: "get",
    params,
  });
}
