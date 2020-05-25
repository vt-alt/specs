%def_enable selinux
# "setuid" or "none"
%define priv_mode setuid
%if %priv_mode == "setuid"
%def_enable userns
%endif

Name: bubblewrap
Version: 0.4.1
Release: alt2

Summary: Unprivileged sandboxing tool

Group: System/Base
License: LGPLv2+
Url: https://github.com/projectatomic/bubblewrap

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/projectatomic/bubblewrap/releases/download/v%version/bubblewrap-%version.tar.xz
# VCS: https://github.com/projectatomic/bubblewrap.git
Source: %name-%version.tar
#Source: https://github.com/projectatomic/%name/releases/download/v%version/%name-%version.tar.xz

Patch1: bubblewrap-fix-run-path.patch

%if %priv_mode == "none"
Requires(pre): libcap-utils
%endif

BuildRequires: gcc-c++ binutils-devel libelf-devel
BuildRequires: db2latex-xsl docbook-style-xsl libcap-devel xsltproc
%{?_enable_selinux:BuildRequires: libselinux-devel}

%description
Many container runtime tools like systemd-nspawn, docker, etc. focus on providing
infrastructure for system administrators and orchestration tools (e.g. Kubernetes) to run containers.

These tools are not suitable to give to unprivileged users,
because it is trivial to turn such access into to a fully privileged root shell on the host.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
	%{subst_enable selinux} \
	%{?_enable_userns:--enable-require-userns=yes}

%make_build

%install
%makeinstall_std

%if_enabled userns
mkdir -p %buildroot%_sysctldir
cat > %buildroot%_sysctldir/90-bwrap.conf << _EOF_
kernel.userns_restrict = 0
_EOF_
%endif

%if %priv_mode == "none"
%post
setcap -q "cap_sys_admin,cap_net_admin,cap_sys_chroot,cap_setuid,cap_setgid=ep" %_bindir/bwrap 2>/dev/null ||:
%endif

%files
%if %priv_mode == "setuid"
%attr(4511,root,root) %_bindir/bwrap
%else
%_bindir/bwrap
%endif
%{?_enable_userns:%_sysctldir/90-bwrap.conf}
%_man1dir/bwrap*
%_datadir/bash-completion/completions/bwrap

%changelog
* Wed May 20 2020 Ivan Razzhivin <underwit@altlinux.org> 0.4.1-alt2
- fix run path (Closes: 38163)

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Dec 03 2019 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri May 03 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- updated to v0.3.1-4-g8fc5a96

* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- updated to v0.3.0-1-gb3906bb
- enabled selinux support

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- new version 0.2.1 (with rpmrb script)

* Fri Oct 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- fixed permissions for bwrap
- created %%_sysctldir/90-bwrap.conf

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.8-alt1
- new version 0.1.8 (with rpmrb script)

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt1
- new version 0.1.7 (with rpmrb script)

* Sun Jan 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- new version 0.1.6 (with rpmrb script)

* Sat Dec 31 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- new version 0.1.4 (with rpmrb script)

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1
- new version 0.1.2 (with rpmrb script)

* Sun Aug 14 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- initial build for ALT Linux Sisyphus
