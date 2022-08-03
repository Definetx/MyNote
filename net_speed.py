#!/usr/bin/python
#coding=utf-8
#针对业务监听的端口流量进行统计，忽略对随机端口流量统计
#若针对突然流量增大，找到其进程进行告警，可以不做统计，获取到流量进行判断，若大于多少阀值，则输出
import os
def change_unit(unit):
	if "Mb" in unit:
		flow = float(unit.strip("Mb")) * 1024
		return flow
	elif "Kb" in unit:
		flow = float(unit.strip("Kb"))
		return flow
	elif "b" in unit:
		flow = float(unit.strip("b")) / 1024
		return flow

def get_flow():
	#iftop参数：-t 使用不带ncurses的文本界面,-P显示主机以及端口信息,-N只显示连接端口号，不显示端口对应的服务名称,-n 将输出的主机信息都通过IP显示，不进行DNS解析,-s num  num秒后打印一次文本输出然后退出
	mes = os.popen("iftop -t -P -N -n -s 2 2>/dev/null |grep -A 1 -E '^   [0-9]'").read()
	#以换行符进行分割
	iftop_list = mes.split("\n")
	count = len(iftop_list)
	#定义字典 存放主机信息和进出流量
	flow_dict = {}
	#定义列表，存放主机信息
	host_ips = []

# 把主机加入数组，新的主机查询是否在列表里面，没有的话，把主机信息加入host_ips，并新组装一个字典值加入flow_dict字典，如果host_ips存在主机信息，则把字典值取出来，重新计算增加流量数值，再加入字典flow_dict
	#这里的 count/2 是iftop获取到的数据，是进出流量为一组，则有count/2 个流量连接，可执行os.popen 里面的iftop命令即可明白
	for i in range(int(count/2)):
		flow_msg = ""
		#获取发送的ip地址(本地ip地址)，端口(本地端口)，发送的流量,以换行符分割后，数据偶数位为本地发送流量信息
		location_li_s = iftop_list[i*2]
		send_flow_lists = location_li_s.split(" ")
		#去空元素
		while '' in send_flow_lists:
			send_flow_lists.remove('')
		host_ip = send_flow_lists[1]
		send_flow = send_flow_lists[3]
		send_flow_float = change_unit(send_flow)
		#print send_flow_lists
		#获取接收的流量
		location_li_r = iftop_list[i*2+1]
		rec_flow_lists = location_li_r.split(" ")
		while '' in rec_flow_lists:
			rec_flow_lists.remove('')
		rec_flow = rec_flow_lists[3]
		rec_flow_float = change_unit(rec_flow)	
		#去掉本地linux 大于10000的随机端口，因为公司业务应用无大于10000，也可把这里去掉
		port = host_ip.split(":")[1]
		if int(port) < 1000000:
		#主机信息若不存在列表则加入host_ips，若存在，则字典取值，对进出流量进行相加
			if host_ip not in host_ips:
					host_ips.append(host_ip)
					flow_msg = str(float('%2.f' % send_flow_float)) + ":" + str(float('%.2f' % rec_flow_float))
					flow_dict[host_ip]=flow_msg
			else:
				flow_dict_msg = flow_dict[host_ip]
				flow_dict_msg_li = flow_dict_msg.split(":")
				#获取字典里的发送接收流量
				flow_dict_msg_send = float(flow_dict_msg_li[0])
				flow_dict_msg_rec = float(flow_dict_msg_li[1])
				#字典里面的发送接收流量和获取到的新流量相加
				flow_add_send = flow_dict_msg_send + send_flow_float
				flow_add_rec = flow_dict_msg_rec + rec_flow_float
				#把新得出的结果，更新到字典
				flow_msg = str(float('%.2f' % flow_add_send)) + ":" + str(float('%.2f' % flow_add_rec))
				flow_dict[host_ip]=flow_msg
	for key in flow_dict:
		flow_li = flow_dict[key].split(":")
		#flow_li[0]为发送流量，flow_li[1]为接收流量，单位是Kb
		print("%24s | %8s | %8s" % (key, flow_li[0], flow_li[1]))

get_flow()
