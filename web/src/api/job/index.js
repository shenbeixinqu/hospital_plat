import request from "@/utils/request";


export function jobList(params) {
  return request({
    url: "/jobs",
    method: "GET",
    params
  });
}

export function jobAdd(data) {
  return request({
    url: "/jobs",
    method: "POST",
    data
  })
}

export function jobEdit(data, job_id) {
  return request({
    url: "/jobs/" + job_id,
    method: "PUT",
    data
  })
}