import request from "@/utils/request";


export function chartRightTopTwo() {
  return request({
    url: "/chart_right_top_two",
    method: "GET",
  });
}
