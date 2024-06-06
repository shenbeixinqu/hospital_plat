import request from "@/utils/request";


export function roleList(params) {
  return request({
    url: "/roles",
    method: "GET",
    params
  });
}


export function roleAdd(data) {
  return request({
    url: "/roles",
    method: "POST",
    data
  })
}

export function roleEdit(data, role_id) {
  return request({
    url: "/roles/" + role_id,
    method: "PUT",
    data
  })
}

export function roleDel(role_id) {
  return request({
    url: "/roles/" + role_id,
    method: "DELETE",
  })
}

export function roleObtain(role_id) {
  return request({
    url: "/roles/info/" + role_id,
    method: "GET",
  });
}


export function roleAssign(data, role_id) {
  return request({
    url: "/roles/power/" + role_id,
    method: "PUT",
    data
  })
}


