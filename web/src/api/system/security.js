import request from "@/utils/request";


export function stopLockData() {
  return request({
    url: "/stop_lock_data",
    method: "GET",
  });
}


export function stopLockApply(data) {
  return request({
    url: "/stop_lock_apply",
    method: "POST",
    data
  })
}

export function autoLogoutData() {
  return request({
    url: "/auto_logout_data",
    method: "GET",
  });
}


export function autoLogoutApply(data) {
  return request({
    url: "/auto_logout_apply",
    method: "POST",
    data
  })
}