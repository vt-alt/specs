
Name: adcli
Version: 0.9.0

Release: alt1
Summary: Active Directory enrollment
License: LGPLv2+
Group: Networking/Other

Url: http://cgit.freedesktop.org/realmd/adcli
Source: %name-%version.tar
Patch: %name-%version.patch

Requires: libsasl2-plugin-gssapi

BuildRequires: intltool
BuildRequires: /usr/bin/krb5-config
BuildRequires: libldap-devel libsasl2-devel
BuildRequires: libxslt
BuildRequires: xmlto

%description
adcli is a library and tool for joining an Active Directory domain using
standard LDAP and Kerberos calls.

%package doc
Summary: adcli documentation
Group: Development/Documentation
BuildArch: noarch

%description doc
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls. This package contains its
documentation.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static --disable-silent-rules --enable-strict
%make_build


%install
%makeinstall_std

%check
%make_build check

%files
%_sbindir/adcli
%doc AUTHORS COPYING ChangeLog NEWS README
%_man8dir/*

%files doc
%doc %_datadir/doc/adcli

%changelog
* Thu Jan 23 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- 0.9.0

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt2
- NMU: remove %ubt from release

* Sun Aug 06 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1%ubt
- 0.8.2

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Nov 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.6-alt1
- 0.7.6 (ALT #31470)

* Wed Apr 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.7.5-alt1
- Initial build package
