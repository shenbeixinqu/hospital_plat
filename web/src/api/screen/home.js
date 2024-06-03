import request from "@/utils/request";

export function chartLeftTopOne() {
  return request({
    url: "/chart_left_top_one",
    method: "GET",
  });
}

export function chartLeftTopTwo() {
  return request({
    url: "/chart_left_top_two",
    method: "GET",
  });
}

export function chartLeftTopThree() {
  return request({
    url: "/chart_left_top_three",
    method: "GET",
  });
}

export function chartRightTopOne() {
  return request({
    url: "/chart_right_top_one",
    method: "GET",
  });
}

export function chartRightTopTwo() {
  return request({
    url: "/chart_right_top_two",
    method: "GET",
  });
}

export function chartLeftBottom() {
  return request({
    url: "/chart_left_bottom",
    method: "GET",
  });
}

export function chartCenterBottom() {
  return request({
    url: "/chart_center_bottom",
    method: "GET",
  });
}

export function chartRightBottom() {
  return request({
    url: "/chart_right_bottom",
    method: "GET",
  });
}