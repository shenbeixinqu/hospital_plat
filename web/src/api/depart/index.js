import request from "@/utils/request";


export function departList(params) {
  return request({
    url: "/departs",
    method: "GET",
    params
  });
}

export function departSelect() {
  return request({
    url: "/p/departs/pl",
    method: "GET",
  })
}

export function departAdd(data) {
  return request({
    url: "/departs",
    method: "POST",
    data
  })
}

export function departEdit(data, depart_id) {
  return request({
    url: "/departs/" + depart_id,
    method: "PUT",
    data
  })
}

export function departDel(depart_id) {
  return request({
    url: "/departs/" + depart_id,
    method: "DELETE",
  })
}