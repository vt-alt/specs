Name: x11vnc-service
%define unitname x11vnc.service
Version: 0.2
Release: alt2.M90P.1

Summary: Service for x11vnc
License: GPL
Group: Networking/Remote access

Source0: %name-%version.tar.gz
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

BuildArch: noarch
BuildRequires: /proc
Requires: x11vnc

%description
This tool adds the systemd service for x11vnc

%prep
%setup

%install
install -pDm644 %unitname %buildroot%_unitdir/%unitname
install -pDm644 %name.1 %buildroot%_mandir/man1/%name.1
mkdir %buildroot%_sbindir
cat > %buildroot%_sbindir/x11vnc-start-daemon << EOF
#!/bin/bash
AUTH=\`ps aux | grep "\-auth " | head -n 1\`
AUTH=\${AUTH/*\-auth /}
AUTH=\${AUTH/ */}
/usr/bin/x11vnc -auth \$AUTH -dontdisconnect -usepw -shared -forever -rfbport 5900 -rfbauth /root/.vnc/passwd -display :0 -repeat
EOF

%post
%post_service x11vnc

%preun
%preun_service x11vnc

%files
%_unitdir/%unitname
%attr(0755,root,root) %_sbindir/x11vnc-start-daemon
%_mandir/man1/%name.1.xz

%changelog
* Fri Apr 10 2020 Ilfat Aminov <aminov@altlinux.org> 0.2-alt2.M90P.1
- backport to P9

* Wed Oct 09 2019 Ilfat Aminov <aminov@altlinux.org> 0.2-alt3
- Fix: x11vnc fail after system start/reboot

* Wed Oct 09 2019 Ilfat Aminov <aminov@altlinux.org> 0.2-alt2
- Set -repeat option

* Thu Nov 16 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.2-alt1
- Fixed start the service on any DM (MIT-MAGIC-COOKIE file)

* Mon Jan 30 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.1-alt3
- Replaced: postun -> preun

* Tue Dec 20 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.1-alt2
- Fixed spec for p8

* Thu Dec 15 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.1-alt1
- Initial build
- Thanks 'rabochyITs' - https://forum.altlinux.org/index.php?topic=32355#msg285275
