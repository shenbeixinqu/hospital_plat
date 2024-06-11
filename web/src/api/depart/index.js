import request from "@/utils/request";


export function departList(params) {
  return request({
    url: "/departs",
    method: "GET",
    params
  });
}
