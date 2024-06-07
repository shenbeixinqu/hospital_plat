import request from "@/utils/request";

export function powerList(params) {
  return request({
    url: "/p/powers",
    method: "GET",
    params
  });
}