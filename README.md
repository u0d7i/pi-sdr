# Raspberry Pi SDR (Software Defined Radio) Station

## Setup

```
$ grep menu /etc/passwd
menu:x:1001:1001::/home/menu:/usr/local/bin/menu

$ sudo grep menu /etc/sudoers
menu ALL=(ALL) NOPASSWD: ALL

$ ls -al /etc/systemd/system/getty.target.wants/getty@tty1.service
lrwxrwxrwx 1 root root 43 Jun 24 12:37 /etc/systemd/system/getty.target.wants/getty@tty1.service -> /etc/systemd/system/autologin-menu@.service

$ grep menu /etc/systemd/system/autologin-menu@.service
ExecStart=-/sbin/agetty --autologin menu --noclear %I $TERM

$ diff -U 0 /etc/systemd/system/autologin@.service /etc/systemd/system/autologin-menu@.service
--- /etc/systemd/system/autologin@.service      2015-09-18 16:57:43.000000000 +0000
+++ /etc/systemd/system/autologin-menu@.service 2016-06-24 12:37:59.921237693 +0000
@@ -28 +28 @@
-ExecStart=-/sbin/agetty --autologin pi --noclear %I $TERM
+ExecStart=-/sbin/agetty --autologin menu --noclear %I $TERM
```
