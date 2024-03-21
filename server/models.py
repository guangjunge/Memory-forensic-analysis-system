#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pytz import unicode

from server import db, flask_bcrypt
from flask_sqlalchemy import SQLAlchemy
class clientstat(db.Model):
    __tablename__ = 'clientstat'
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    used = db.Column(db.Integer)
    free = db.Column(db.Integer)
    def __init__(self,total=0,used=0,free=0):
        self.total = total
        self.used = used
        self.free = free

class User(db.Model):
    __tablename__ = 'hit_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))
    email = db.Column(db.String(128))
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = flask_bcrypt.generate_password_hash(password)
        self.email = email
    def __repr__(self):
        return '<User %r>' % self.username
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)

class ramstat(db.Model):
    __tablename__ = 'current_ram'
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    used = db.Column(db.Integer)
    free = db.Column(db.Integer)
    def __init__(self,total=0,used=0,free=0):
        self.total = total
        self.used = used
        self.free = free
class ServerInfo(db.Model):
    __tablename__ = 'server_info'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(128))
    system = db.Column(db.String(128))
    runtime = db.Column(db.String(128))
    def __init__(self, ip=None, system=None, runtime=None):
        self.ip = ip
        self.system = system
        self.runtime = runtime
class TaskConfig(db.Model):
    __tablename__ = 'task_config'
    taskid = db.Column(db.Integer, primary_key=True) #任务ID
    userid = db.Column(db.Integer) #创建者ID
    ip = db.Column(db.String(128))
    mode = db.Column(db.Integer) #任务部署状态 0:指定时间执行 1:每月 2:每周 3:每天
    state = db.Column(db.Integer) #任务执行状态 0:未执行 1:已执行
    text = db.Column(db.String(1024)) #任务注释
    startime = db.Column(db.String(256))
    finishtime = db.Column(db.String(256))
    linux_pslist = db.Column(db.BLOB)
    linux_psaux = db.Column(db.BLOB)
    linux_pstree = db.Column(db.BLOB)
    linux_psxview = db.Column(db.BLOB)
    linux_lsof = db.Column(db.BLOB)
    linux_iomem = db.Column(db.BLOB)
    linux_mount = db.Column(db.BLOB)
    linux_dentry_cache = db.Column(db.BLOB)
    linux_dmesg = db.Column(db.BLOB)
    linux_check_afinfo = db.Column(db.BLOB)
    linux_check_tty = db.Column(db.BLOB)
    linux_check_creds = db.Column(db.BLOB)
    linux_check_fop = db.Column(db.BLOB)
    linux_check_syscall = db.Column(db.BLOB)
    linux_lsmod = db.Column(db.BLOB)
    linux_tmpfs = db.Column(db.BLOB)
    linux_arp = db.Column(db.BLOB)
    linux_ifconfig = db.Column(db.BLOB)
    linux_route_cache = db.Column(db.BLOB)
    linux_netstat = db.Column(db.BLOB)
    linux_proc_maps = db.Column(db.BLOB)
    linux_bash = db.Column(db.BLOB)
    linux_check_modules = db.Column(db.BLOB)

    def __init__(self, userid=None, ip=None, mode=None, startime=None, state=0, text=None):
        self.userid = userid
        self.ip = ip
        self.mode = mode
        self.state = state
        self.text = text
        self.startime = startime
class VolemFeature(db.Model):
    __tablename__ = 'VolemFeature'
    taskid = db.Column(db.Integer, primary_key=True) #任务ID
    userid = db.Column(db.Integer) #创建者ID
    ip = db.Column(db.String(128))
    mode = db.Column(db.Integer) #任务部署状态 0:指定时间执行 1:每月 2:每周 3:每天
    state = db.Column(db.Integer) #任务执行状态 0:未执行 1:已执行
    text = db.Column(db.String(1024)) #任务注释
    startime = db.Column(db.String(256))
    finishtime = db.Column(db.String(256))
    pslist_nproc = db.Column(db.Float)  #进程总数
    pslist_nppid = db.Column(db.Float)
    pslist_avg_threads = db.Column(db.Float)
    pslist_nprocs64bit = db.Column(db.Float)
    pslist_avg_handlers = db.Column(db.Float)
    dllist_ndlls = db.Column(db.Float)
    dllist_avg_dlls_per_proc = db.Column(db.Float)
    handles_nhandles = db.Column(db.Float)
    handles_avg_handles_per_proc = db.Column(db.Float)
    handles_nport = db.Column(db.Float)
    handles_nfile = db.Column(db.Float)
    handles_nevent = db.Column(db.Float)
    handles_ndesktop = db.Column(db.Float)
    handles_nkey = db.Column(db.Float)
    handles_nthread = db.Column(db.Float)
    handles_ndirectory = db.Column(db.Float)
    handles_nsemaphore = db.Column(db.Float)
    handles_ntimer = db.Column(db.Float)
    handles_nsection = db.Column(db.Float)
    handles_nmutant = db.Column(db.Float)
    ldrmodules_not_in_load = db.Column(db.Float)
    ldrmodules_not_in_init = db.Column(db.Float)
    ldrmodules_not_in_mem = db.Column(db.Float)
    ldrmodules_not_in_load_avg = db.Column(db.Float)
    ldrmodules_not_in_init_avg = db.Column(db.Float)
    ldrmodules_not_in_mem_avg = db.Column(db.Float)
    malfind_ninjections = db.Column(db.Float)
    malfind_commitCharge = db.Column(db.Float)
    malfind_protection = db.Column(db.Float)

    malfind_uniqueInjections = db.Column(db.Float)
    psxview_not_in_pslist = db.Column(db.Float)
    psxview_not_in_eprocess_pool = db.Column(db.Float)
    psxview_not_in_ethread_pool = db.Column(db.Float)
    psxview_not_in_pspcid_list = db.Column(db.Float)
    psxview_not_in_csrss_handles = db.Column(db.Float)
    psxview_not_in_session = db.Column(db.Float)
    psxview_not_in_deskthrd = db.Column(db.Float)
    psxview_not_in_pslist_false_avg = db.Column(db.Float)

    psxview_not_in_eprocess_pool_false_avg = db.Column(db.Float)
    psxview_not_in_ethread_pool_false_avg = db.Column(db.Float)
    psxview_not_in_pspcid_list_false_avg = db.Column(db.Float)
    psxview_not_in_csrss_handles_false_avg = db.Column(db.Float)
    psxview_not_in_session_false_avg = db.Column(db.Float)
    psxview_not_in_deskthrd_false_avg = db.Column(db.Float)

    modules_nmodules = db.Column(db.Float)
    svcscan_nservices = db.Column(db.Float)
    svcscan_kernel_drivers = db.Column(db.Float)
    svcscan_fs_drivers = db.Column(db.Float)
    svcscan_process_services = db.Column(db.Float)
    svcscan_shared_process_services = db.Column(db.Float)
    svcscan_interactive_process_services = db.Column(db.Float)
    svcscan_nactive = db.Column(db.Float)
    callbacks_ncallbacks = db.Column(db.Float)
    callbacks_nanonymous = db.Column(db.Float)
    callbacks_ngeneric = db.Column(db.Float)

    def __init__(self, userid=None, ip=None, mode=None, startime=None, state=0, text=None):
        self.userid = userid
        self.ip = ip
        self.mode = mode
        self.state = state
        self.text = text
        self.startime = startime


class AnaResult(db.Model):
    __tablename__ = 'AnaResult'
    taskid = db.Column(db.Integer, primary_key=True)  # 任务ID
    userid = db.Column(db.Integer)  # 创建者ID
    ip = db.Column(db.String(128))
    mode = db.Column(db.Integer)  # 任务部署状态 0:指定时间执行 1:每月 2:每周 3:每天
    state = db.Column(db.Integer)  # 任务执行状态 0:未执行 1:已执行
    text = db.Column(db.String(1024))  # 任务注释
    startime = db.Column(db.String(256))
    finishtime = db.Column(db.String(256))
    Detect_result = db.Column(db.Integer)  # 检测结果
    Classify_result = db.Column(db.Integer)  # 分类结果
    Classify_type  = db.Column(db.String(512)) #分类类型

    def __init__(self, userid=None, ip=None, mode=None, startime=None, state=0, text=None):
        self.userid = userid
        self.ip = ip
        self.mode = mode
        self.state = state
        self.text = text
        self.startime = startime


