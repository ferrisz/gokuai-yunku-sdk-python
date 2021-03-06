#!/usr/bin/env python
# coding=utf-8
# Created by Ferris on 2019/5/17
# 够快云盘SDK Python版

"""
settings 中配置
GOKUAI_SETTINGS = {
    "client_secret": "xxx",
    "client_id": "xxx",
    "host": "https://yk3.gokuai.com"
}
"""
import json
import time

import base64
import hashlib
import hmac
import requests

from django.conf import settings


class Gokuai:
    def gokuai_sign(self, **kwargs):
        """
        获取签名
        :param kwargs:
        :return:
        """
        if not kwargs.get("client_id"):
            kwargs["client_id"] = settings.GOKUAI_SETTINGS["client_id"]
        data = sorted(kwargs.items(), key=lambda d: d[0])
        data = [str(i[1]) for i in data]
        data = '\n'.join(data).encode('utf-8')
        return base64.b64encode(
            hmac.new(settings.GOKUAI_SETTINGS["client_secret"].encode('utf-8'), data, hashlib.sha1).digest())

    def validate_sign(self, postdata):
        """
        验证签名
        :param postdata:
        :return:
        """
        origin_sign = postdata["sign"].encode('utf-8')
        postdata = postdata.dict()
        postdata.pop("sign")
        data = sorted(postdata.items(), key=lambda d: d[0])
        data = [str(i[1]) for i in data]
        data = '\n'.join(data).encode('utf-8')
        true_sign = base64.b64encode(
            hmac.new(settings.GOKUAI_SETTINGS["client_secret"].encode('utf-8'), data, hashlib.sha1).digest())
        return origin_sign == true_sign

    def gokuai_reuquest(self, method="POST", url="", **kwargs):
        """
        发送请求
        :param method:
        :param url:
        :param kwargs:
        :return:
        """
        if method == "POST":
            req_url = settings.GOKUAI_SETTINGS["host"] + url
            t = time.time()
            kwargs["dateline"] = int(t)
            kwargs['sign'] = self.gokuai_sign(**kwargs)
            if not kwargs.get("client_id"):
                kwargs["client_id"] = settings.GOKUAI_SETTINGS["client_id"]
            r = requests.post(req_url, data=kwargs)
            return json.loads(r.text)

    def ent_add_sync_member(self, **kwargs):
        """
        添加或修改同步成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/add_sync_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_sync_member(self, **kwargs):
        """
        删除同步成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_sync_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_add_sync_group(self, **kwargs):
        """
        添加或修改同步部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/add_sync_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_sync_group(self, **kwargs):
        """
        删除同步部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_sync_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def add_sync_group_member(self, **kwargs):
        """
        添加同步部门的成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/add_sync_group_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_sync_group_member(self, **kwargs):
        """
        删除同步部门的成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_sync_group_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_sync_member_group(self, **kwargs):
        """
        删除同步成员的所属部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_sync_member_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_get_member_by_out_id(self, **kwargs):
        """
        通过外部帐号获取成员信息
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/get_member_by_out_id"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_add_sync_admin(self, **kwargs):
        """
        添加管理员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/add_sync_admin"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_add_member(self, **kwargs):
        """
        添加成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/add_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_set_member(self, **kwargs):
        """
        修改成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/set_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_member(self, **kwargs):
        """
        删除成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_add_group(self, **kwargs):
        """
        添加部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/add_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_set_group(self, **kwargs):
        """
        修改部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/set_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_group(self, **kwargs):
        """
        删除部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_add_group_member(self, **kwargs):
        """
        添加部门成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/add_group_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_group_member(self, **kwargs):
        """
        删除部门成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_group_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_del_member_group(self, **kwargs):
        """
        删除成员的所属部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/del_member_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_get_members(self, **kwargs):
        """
        成员列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/get_members"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_get_member(self, **kwargs):
        """
        成员信息
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/get_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_get_groups(self, **kwargs):
        """
        部门列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/get_groups"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_get_group_members(self, **kwargs):
        """
        部门中成员列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/get_group_members"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def ent_get_roles(self, **kwargs):
        """
        角色列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/ent/get_roles"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_create(self, **kwargs):
        """
        创建库
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/create"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_set(self, **kwargs):
        """
        修改库
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/set"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_bind(self, **kwargs):
        """
        获取库收取
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/bind"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_info(self, **kwargs):
        """
        库信息
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/info"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_info_by_member(self, **kwargs):
        """
        个人文件库信息
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/info_by_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_set_by_member(self, **kwargs):
        """
        设置个人文件库
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/set_by_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_ls(self, **kwargs):
        """
        获取库列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/ls"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_bind(self, **kwargs):
        """
        获取库收取
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/bind"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_unbind(self, **kwargs):
        """
        取消库授权
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/unbind"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_get_members(self, **kwargs):
        """
        获取库成员列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/get_members"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_get_member(self, **kwargs):
        """
        查询库成员信息
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/get_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_set_owner(self, **kwargs):
        """
        设置库拥有者
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/set_owner"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_add_member(self, **kwargs):
        """
        添加库成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/add_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_set_member_role(self, **kwargs):
        """
        修改库成员角色
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/set_member_role"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_del_member(self, **kwargs):
        """
        删除库成员
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/del_member"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_get_groups(self, **kwargs):
        """
        获取库的部门列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/get_groups"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_add_group(self, **kwargs):
        """
        库上添加部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/add_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_del_group(self, **kwargs):
        """
        删除库上的部门
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/del_group"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_set_group_role(self, **kwargs):
        """
        修改库上部门的角色
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/set_group_role"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_destroy(self, **kwargs):
        """
        删除库
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/destroy"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def org_log(self, **kwargs):
        """
        库日志
        :param kwargs:
        :return:
        """
        url = "/m-open/1/org/log"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)
    


class GokuaiFile:
    org_client_secret = ""
    org_client_id = ""

    def __init__(self, org_client_secret, org_client_id):
        self.org_client_secret = org_client_secret
        self.org_client_id = org_client_id

    def gokuai_sign(self, **kwargs):
        """
        获取签名
        :param kwargs:
        :return:
        """
        if not kwargs.get("org_client_id"):
            kwargs["org_client_id"] = self.org_client_id
        data = sorted(kwargs.items(), key=lambda d: d[0])
        data = [str(i[1]) for i in data]
        data = '\n'.join(data).encode('utf-8')
        return base64.b64encode(
            hmac.new(self.org_client_secret.encode('utf-8'), data, hashlib.sha1).digest())

    def validate_sign(self, postdata):
        """
        验证签名
        :param postdata:
        :return:
        """
        origin_sign = postdata["sign"].encode('utf-8')
        postdata = postdata.dict()
        postdata.pop("sign")
        data = sorted(postdata.items(), key=lambda d: d[0])
        data = [str(i[1]) for i in data]
        data = '\n'.join(data).encode('utf-8')
        true_sign = base64.b64encode(
            hmac.new(self.org_client_secret.encode('utf-8'), data, hashlib.sha1).digest())
        return origin_sign == true_sign

    def gokuai_reuquest(self, method="POST", url="", **kwargs):
        """
        发送请求
        :param method:
        :param url:
        :param kwargs:
        :return:
        """
        if method == "POST":
            req_url = settings.GOKUAI_SETTINGS["host"] + url
            t = time.time()
            kwargs["dateline"] = int(t)
            kwargs['sign'] = self.gokuai_sign(**kwargs)
            if not kwargs.get("org_client_id"):
                kwargs["org_client_id"] = self.org_client_id
            r = requests.post(req_url, data=kwargs)
            return json.loads(r.text)

    def file_ls(self, **kwargs):
        """
        文件列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/ls"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_updates(self, **kwargs):
        """
        文件最近更新列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/updates"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_updates_count(self, **kwargs):
        """
        文件更新数量
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/updates_count"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_download_url(self, **kwargs):
        """
        文件下载地址
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/download_url"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_preview_url(self, **kwargs):
        """
        文件预览地址
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/preview_url"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_info(self, **kwargs):
        """
        文件（夹）信息
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/info"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_search(self, **kwargs):
        """
        文件搜索
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/search"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_create_folder(self, **kwargs):
        """
        创建文件夹
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/create_folder"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_create_file(self, **kwargs):
        """
        上传文件 - 请求上传
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/create_file"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_upload_servers(self, **kwargs):
        """
        网页上传 - 获取上传服务器
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/upload_servers"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_copy(self, **kwargs):
        """
        复制文件（夹）
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/copy"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_mcopy(self, **kwargs):
        """
        高级复制文件（夹）
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/mcopy"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_del(self, **kwargs):
        """
        删除文件（夹）
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/del"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_recycle(self, **kwargs):
        """
        回收站
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/recycle"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_recover(self, **kwargs):
        """
        恢复已删除文件
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/recover"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_del_completely(self, **kwargs):
        """
        彻底删除文件（夹）
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/del_completely"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_move(self, **kwargs):
        """
        移动文件（夹）
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/move"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_history(self, **kwargs):
        """
        获取文件历史
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/history"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_link(self, **kwargs):
        """
        获取文件外链
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/link"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_link_close(self, **kwargs):
        """
        关闭文件外链
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/link_close"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_links(self, **kwargs):
        """
        获取开启外链的文件列表
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/links"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_get_all_permission(self, **kwargs):
        """
        获取文件夹所有权限
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/get_all_permission"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_file_permission(self, **kwargs):
        """
        修改文件夹权限
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/file_permission"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_get_permission(self, **kwargs):
        """
        获取用户在文件夹的权限
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/get_permission"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_add_tag(self, **kwargs):
        """
        添加标签
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/add_tag"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_del_tag(self, **kwargs):
        """
        删除标签
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/del_tag"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)

    def file_stat(self, **kwargs):
        """
        统计信息
        :param kwargs:
        :return:
        """
        url = "/m-open/1/file/stat"
        return self.gokuai_reuquest(method="POST", url=url, **kwargs)
