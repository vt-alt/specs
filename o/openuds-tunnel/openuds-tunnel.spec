%define _unpackaged_files_terminate_build 1
%define appdir %_var/lib/tomcat/webapps

Name: openuds-tunnel
Version: 2.5.0
Release: alt2
Summary: Clientless remote desktop gateway
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/dkmstr/openuds

Source: ssh-tunnel.tar
Source2: transport.war
Source3: uds.conf
Source4: sshd_uds.pam
Source5: sshd_uds.conf
Source6: sshd_uds.service

BuildRequires(pre): rpm-macros-cmake rpm-build-java
BuildRequires: /proc
BuildRequires: java-devel
#BuildRequires: maven-local
#BuildRequires: maven
BuildRequires: tomcat
BuildRequires: cmake gcc-c++
BuildRequires: libcurl-devel libpam-devel

Requires: openssh-server
Requires: openuds-guacamole-tunnel
Requires: pam_uds
Requires: libnss_uds

%description
Guacamole is an HTML5 web application that provides access
to desktop environments using remote desktop protocols such as VNC or RDP.
A centralized server acts as a tunnel and proxy,
allowing access to multiple desktops through a web browser.
No plugins are needed: the client requires nothing more than a web browser
supporting HTML5 and AJAX.
This is the client-part.

This portion of UDS (HTML5 tunnel) is based on Apache Guacamole.

%package -n openuds-guacamole-tunnel
Summary: Clientless remote desktop gateway
License: Apache-2.0
Group: Networking/Remote access
Provides: tomcat-transport-webapps = %EVR
Provides: guacamole-openuds = %EVR
Requires: tomcat
Requires: java-headless
Requires: guacamole-server
BuildArch: noarch
AutoReqProv: noosgi, noosgi-fc

%description -n openuds-guacamole-tunnel
Guacamole is an HTML5 web application that provides access
to desktop environments using remote desktop protocols such as VNC or RDP.
A centralized server acts as a tunnel and proxy,
allowing access to multiple desktops through a web browser.
No plugins are needed: the client requires nothing more than a web browser
supporting HTML5 and AJAX.
This is the client-part.

This portion of UDS (HTML5 tunnel) is based on Apache Guacamole.

%package -n pam_uds
Summary: PAM for OpenUDS
Group: System/Base
License: GPLv2+

%description -n pam_uds
%summary.

%package -n libnss_uds
Summary: NSS module for OpenUDS
Group: System/Base
License: GPLv2+

%description -n libnss_uds
%summary.

It is necessary to change "passwd" in /etc/nsswitch.conf to
passwd: files uds

%prep
%setup -n pam-http

%build
%cmake
%cmake_build

%install
#%%cmakeinstall_std
install -p -D -m 644 BUILD/src/libnss_uds.so %buildroot/%_lib/libnss_uds.so.2
install -p -D -m 644 BUILD/src/pam_uds.so %buildroot/%_lib/security/pam_uds.so

# Tmcat webapps
mkdir -p %buildroot%_datadir/tomcat
mkdir -p %buildroot%appdir/%name
#cp %SOURCE2 %buildroot/%appdir/transport.war
pushd %buildroot%appdir/%name
%jar -xf %SOURCE2
popd

# config
install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/uds.conf

# sshd_uds
mkdir %buildroot%_sbindir
ln -s sshd %buildroot%_sbindir/sshd_uds
install -p -D -m 600 %SOURCE4 %buildroot%_sysconfdir/pam.d/sshd_uds
install -p -D -m 600 %SOURCE5 %buildroot%_sysconfdir/openssh/sshd_uds_config
install -p -D -m 644 %SOURCE6 %buildroot%_unitdir/sshd_uds.service

%post -n libnss_uds
if [ -f /etc/nsswitch.conf ] ; then
            grep -E -q '^passwd:.* uds' /etc/nsswitch.conf ||
            sed -i.rpmorig -r -e '
                s/^passwd:(.*)/\1:\2 uds/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi
update_chrooted all

%postun -n libnss_uds
if [ "$1" = "0" ]; then
        if [ -f /etc/nsswitch.conf ] ; then
                sed -i.rpmorig -e '
                        /^passwd:/ !b
                        s/[[:blank:]]\+uds\>//
                        ' /etc/nsswitch.conf >/dev/null 2>&1 || :
        fi
fi
update_chrooted all


%post
%post_service sshd_uds

%preun
%preun_service sshd_uds

%files
%config(noreplace) %attr(0644, root, root) %_sysconfdir/uds.conf
%config(noreplace) %attr(0600, root, root) %_sysconfdir/pam.d/sshd_uds
%config(noreplace) %attr(0600, root, root) %_sysconfdir/openssh/sshd_uds_config
%_sbindir/sshd_uds
%_unitdir/sshd_uds.service

%files -n libnss_uds
/%_lib/libnss_uds.so.2
%exclude /%_lib/libnss_uds.so

%files -n pam_uds
/%_lib/security/pam_uds.so

%files -n openuds-guacamole-tunnel
#%appdir/%name.war
%defattr(0644,tomcat,tomcat,0755)
%appdir/%name

%changelog
* Mon Jan 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt2
- Fixed sshd_uds.service

* Mon Dec 07 2020 Alexey Shabalin <shaba@altlinux.org> 2.5.0-alt1
- Initial build
