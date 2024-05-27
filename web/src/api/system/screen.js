import request from "@/utils/request";


export function distributedData() {
  return request({
    url: "/distributed_data",
    method: "GET",
  });
}


export function distributedApply(data) {
  return request({
    url: "/distributed_apply",
    method: "POST",
    data
  })
}

export function warningData() {
  return request({
    url: "/warning_data",
    method: "GET"
  })
}

export function warningApply(data) {
  return request({
    url: "/warning_apply",
    method: "POST",
    data
  })
}