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

export function logout(params) {
  return request({
    url: "/logout",
    method: "GET",
    params,
  });
}

export function getRoleInfo(params) {
  return request({
    url: "/user/info",
    method: "get",
    params,
  });
}
