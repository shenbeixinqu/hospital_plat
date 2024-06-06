import request from "@/utils/request";

export function powerList(params) {
  return request({
    url: "/powers",
    method: "GET",
    params
  });
}