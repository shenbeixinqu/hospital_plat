import random

list2 = [
    {"time": "2024-03-30", "fk_count": 300, "ip_count": 386, "new_count": 671, "views": 541, "last_week": 316, "change": "26.65%", "last_month": "842", "change_two": "4.31%", "minute": "00:05:01"},
    {"time": "2024-03-29", "fk_count": 196, "ip_count": 187, "new_count": 135, "views": 572, "last_week": 876, "change": "22.65%", "last_month": "236", "change_two": "6.41%", "minute": "00:02:45"},
    {"time": "2024-03-28", "fk_count": 245, "ip_count": 278, "new_count": 247, "views": 671, "last_week": 642, "change": "25.13%", "last_month": "522", "change_two": "3.54%", "minute": "00:01:15"},
    {"time": "2024-03-27", "fk_count": 209, "ip_count": 147, "new_count": 246, "views": 713, "last_week": 547, "change": "21.71%", "last_month": "735", "change_two": "4.65%", "minute": "00:02:16"},
    {"time": "2024-03-26", "fk_count": 211, "ip_count": 235, "new_count": 128, "views": 356, "last_week": 631, "change": "27.12%", "last_month": "824", "change_two": "6.31%", "minute": "00:01:22"},
    {"time": "2024-03-25", "fk_count": 309, "ip_count": 471, "new_count": 263, "views": 315, "last_week": 135, "change": "21.31%", "last_month": "427", "change_two": "6.41%", "minute": "00:02:54"},
    {"time": "2024-03-24", "fk_count": 387, "ip_count": 462, "new_count": 613, "views": 681, "last_week": 876, "change": "21.13%", "last_month": "652", "change_two": "2.51%", "minute": "00:01:23"},
    {"time": "2024-03-23", "fk_count": 177, "ip_count": 157, "new_count": 135, "views": 471, "last_week": 143, "change": "26.20%", "last_month": "247", "change_two": "3.13%", "minute": "00:00:58"},
    {"time": "2024-03-22", "fk_count": 200, "ip_count": 223, "new_count": 713, "views": 462, "last_week": 312, "change": "28.75%", "last_month": "741", "change_two": "6.25%", "minute": "00:01:19"},
    {"time": "2024-03-21", "fk_count": 192, "ip_count": 268, "new_count": 511, "views": 651, "last_week": 764, "change": "27.54%", "last_month": "524", "change_two": "2.31%", "minute": "00:00:44"},
    {"time": "2024-03-20", "fk_count": 253, "ip_count": 567, "new_count": 265, "views": 246, "last_week": 572, "change": "26.20%", "last_month": "425", "change_two": "6.12%", "minute": "00:01:18"},
    {"time": "2024-03-19", "fk_count": 219, "ip_count": 123, "new_count": 713, "views": 724, "last_week": 247, "change": "21.75%", "last_month": "242", "change_two": "3.51%", "minute": "00:01:37"},
    {"time": "2024-03-18", "fk_count": 218, "ip_count": 268, "new_count": 256, "views": 136, "last_week": 734, "change": "27.41%", "last_month": "745", "change_two": "6.35%", "minute": "00:02:05"},
    {"time": "2024-03-17", "fk_count": 286, "ip_count": 274, "new_count": 168, "views": 741, "last_week": 546, "change": "29.11%", "last_month": "562", "change_two": "4.35%", "minute": "00:01:51"},
    {"time": "2024-03-16", "fk_count": 285, "ip_count": 451, "new_count": 213, "views": 654, "last_week": 316, "change": "28.37%", "last_month": "247", "change_two": "6.12%", "minute": "00:01:22"},
    {"time": "2024-03-15", "fk_count": 255, "ip_count": 211, "new_count": 246, "views": 867, "last_week": 136, "change": "26.10%", "last_month": "671", "change_two": "6.36%", "minute": "00:01:24"},
    {"time": "2024-03-14", "fk_count": 301, "ip_count": 266, "new_count": 132, "views": 617, "last_week": 684, "change": "25.25%", "last_month": "124", "change_two": "7.96%", "minute": "00:01:35"},
    {"time": "2024-03-13", "fk_count": 271, "ip_count": 268, "new_count": 512, "views": 651, "last_week": 687, "change": "21.35%", "last_month": "833", "change_two": "4.46%", "minute": "00:02:41"},
    {"time": "2024-03-12", "fk_count": 222, "ip_count": 299, "new_count": 354, "views": 683, "last_week": 316, "change": "16.25%", "last_month": "316", "change_two": "4.35%", "minute": "00:04:14"},
    {"time": "2024-03-11", "fk_count": 198, "ip_count": 301, "new_count": 765, "views": 675, "last_week": 651, "change": "34.13%", "last_month": "823", "change_two": "5.35%", "minute": "00:02:46"},
    {"time": "2024-03-10", "fk_count": 227, "ip_count": 192, "new_count": 461, "views": 712, "last_week": 547, "change": "31.26%", "last_month": "682", "change_two": "7.13%", "minute": "00:00:59"},
    {"time": "2024-03-09", "fk_count": 247, "ip_count": 157, "new_count": 562, "views": 836, "last_week": 371, "change": "12.35%", "last_month": "824", "change_two": "2.35%", "minute": "00:02:56"},
    {"time": "2024-03-08", "fk_count": 310, "ip_count": 212, "new_count": 621, "views": 356, "last_week": 713, "change": "23.46%", "last_month": "572", "change_two": "3.43%", "minute": "00:01:21"},
    {"time": "2024-03-07", "fk_count": 325, "ip_count": 271, "new_count": 876, "views": 427, "last_week": 541, "change": "21.35%", "last_month": "722", "change_two": "3.12%", "minute": "00:02:05"},
    {"time": "2024-03-06", "fk_count": 281, "ip_count": 356, "new_count": 346, "views": 671, "last_week": 731, "change": "31.61%", "last_month": "874", "change_two": "5.31%", "minute": "00:01:38"},
    {"time": "2024-03-05", "fk_count": 188, "ip_count": 126, "new_count": 613, "views": 368, "last_week": 436, "change": "35.56%", "last_month": "572", "change_two": "6.35%", "minute": "00:04:11"},
    {"time": "2024-03-04", "fk_count": 281, "ip_count": 274, "new_count": 754, "views": 625, "last_week": 136, "change": "31.65%", "last_month": "824", "change_two": "7.22%", "minute": "00:03:45"},
    {"time": "2024-03-03", "fk_count": 277, "ip_count": 247, "new_count": 431, "views": 471, "last_week": 752, "change": "21.65%", "last_month": "324", "change_two": "3.23%", "minute": "00:01:19"},
    {"time": "2024-03-02", "fk_count": 210, "ip_count": 213, "new_count": 631, "views": 713, "last_week": 246, "change": "22.64%", "last_month": "842", "change_two": "3.41%", "minute": "00:01:22"},
    {"time": "2024-03-01", "fk_count": 282, "ip_count": 314, "new_count": 346, "views": 461, "last_week": 731, "change": "19.41%", "last_month": "237", "change_two": "3.43%", "minute": "00:02:35"}
]

random.shuffle(list2)

# 打印打乱后的列表
print(list2)