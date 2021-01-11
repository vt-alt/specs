Name:     purple-xmpp-http-upload
Version:  0.2.2
Release:  alt1

Summary:  HTTP File Upload plugin for libpurple (XMPP Protocol)
License:  GPLv3
Group:    Networking/Instant messaging
Url:      https://github.com/Junker/purple-xmpp-http-upload

Packager: Evgeniy Korneechev <ekorneechev@altlinux.org>

Source:   %name-%version.tar

BuildRequires: libgio-devel glib2-devel libxml2-devel libpurple-devel > 2.13.0-alt2

Requires: libpurple > 2.13.0-alt2

%description
XEP-0363: HTTP File Upload plugin for libpurple (Pidgin, Finch, etc.)

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_libdir/purple-2/*.so

%changelog
* Thu Dec 10 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.2.2-alt1
- New version

* Wed Dec 12 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.1-alt1
- Initial build for Sisyphus
