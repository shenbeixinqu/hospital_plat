import request from "@/utils/request";


export function userList(params) {
  return request({
    url: "/users",
    method: "GET",
    params
  });
}