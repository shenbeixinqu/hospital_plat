import request from "@/utils/request";


export function monthReportData() {
  return request({
    url: "/month_report_data",
    method: "GET",
  });
}


export function monthReportApply(data) {
  return request({
    url: "/month_report_apply",
    method: "POST",
    data
  })
}

export function yearReportData() {
  return request({
    url: "/year_report_data",
    method: "GET",
  });
}


export function yearReportApply(data) {
  return request({
    url: "/year_report_apply",
    method: "POST",
    data
  })
}