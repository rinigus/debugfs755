Name: debugfs755

Summary:    Mount debugFS with 0755 mode
Version:    0.1
Release:    1
Group:      Config
License:    MIT
BuildArch:  noarch
URL:        https://github.com/rinigus/debugfs755
Source:     %{name}-%{version}.tar.bz2
Requires:   systemd

%description
Helper package that sets DebugFS mounting permissions to 0755 in systemd systems

%prep
exit 0

%build
exit 0

%clean
exit 0

%install
rm -rf %{buildroot}
%{__install} -Dp -m 0755 src/debugfs755.conf %{buildroot}%{_sysconfdir}/systemd/system/sys-kernel-debug.mount.d/debugfs755.conf

%post
systemctl daemon-reload
systemctl restart sys-kernel-debug.mount

%postun
systemctl daemon-reload
systemctl restart sys-kernel-debug.mount


%files
%config(noreplace) %{_sysconfdir}/systemd/system/sys-kernel-debug.mount.d/debugfs755.conf
