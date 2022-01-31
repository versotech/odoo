# -*- coding: utf-8 -*-
from struct import pack  # , unpack
class User(object):

    def __init__(self, uid, name, privilege, password='', group_id='', user_id='', card=0):
        self.uid = uid
        self.name = name
        self.privilege = privilege
        self.password = password
        self.group_id = group_id
        self.user_id = user_id
        self.card = card  # 64 int to 40 bit int
    def repack29(self):  # with 02 for zk6 (size 29)
        return pack("<BHB5s8sIxBhI", 2, self.uid, self.privilege, self.password, self.name, self.card, int(self.group_id) if self.group_id else 0, 0, int(self.user_id))
    def repack73(self):  # with 02 for zk8 (size73)
        # password 6s + 0x00 + 0x77
        # 0,0 => 7sx group id, timezone?
        return pack("<BHB8s24sIB7sx24s", 2, self.uid, self.privilege, self.password, self.name, self.card, 1, self.group_id, self.user_id)
    def __str__(self):
        return u'<User>: [uid:{}, name:{} user_id:{}]'.format(self.uid, self.name, self.user_id)

    def __repr__(self):
        return u'<User>: [uid:{}, name:{} user_id:{}]'.format(self.uid, self.name, self.user_id)
