import request from "@/utils/request";


export function userAllList(params) {
  return request({
    url: "/p/users",
    method: "GET",
    params
  });
}