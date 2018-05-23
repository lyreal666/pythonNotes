#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'LY'

import mailbox

'''
    所以，一封电子邮件的旅程就是：

    发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
    有了上述基本概念，要编写程序来发送和接收邮件，本质上就是：
    
    1.编写MUA把邮件发到MTA；
    
    2,编写MUA从MDA上收邮件。
'''

