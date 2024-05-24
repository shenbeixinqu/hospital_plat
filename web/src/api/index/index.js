import request from "@/utils/request";


export function header_data(data) {
  return request({
    url: "/header_data",
    method: "POST",
    data,
  });
}


export function statistics_data(data) {
  return request({
    url: "/statistics_data",
    method: "POST",
    data
  })
}

export function rank_data() {
  return request({
    url: "/rank_data",
    method: "GET",
  })
}