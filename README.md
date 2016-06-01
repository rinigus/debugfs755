# debugfs755
Helper package that sets DebugFS mounting permissions to 0755 in systemd systems

This is a convenience package for users who want to mount debugFS with relaxed permissions and is mainly targeted towards Sailfish OS phones/tablets.

The newer Linux kernels mount DebugFS with 0700 permissions, starting from the commit https://github.com/torvalds/linux/commit/82aceae4f0d42f03d9ad7d1e90389e731153898f . If the user desires to change permissions to world-readable, debugFS has to be remounted or its mount command altered on system boot. This package adds configuration file at /etc/systemd/system/sys-kernel-debug.mount.d to change mount options of systemd debugFS mount script. 

Here is a bit of reading regarding DebugFS and some discussions around it:

https://lwn.net/Articles/429321/

and the current Readme in kernel source:

https://www.kernel.org/doc/Documentation/filesystems/debugfs.txt
