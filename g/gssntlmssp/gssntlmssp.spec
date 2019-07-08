%def_with wbclient

Name: gssntlmssp
Version: 0.8.0
Release: alt1
Summary: GSSAPI NTLMSSP Mechanism

Group: System/Libraries
License: LGPLv3+
Url: https://pagure.io/gssntlmssp
# Git-VCS: https://pagure.io/gssntlmssp.git
Source: %name-%version.tar
Patch: %name-%version.patch

Requires: libkrb5 >= 1.13
Requires: libwbclient

BuildRequires: xsltproc xml-utils
BuildRequires: docbook-style-xsl docbook-dtds
BuildRequires: doxygen
BuildRequires: libkrb5-devel >= 1.13
BuildRequires: libunistring-devel
BuildRequires: zlib-devel
BuildRequires: libssl-devel
%{?_with_wbclient:BuildRequires: libwbclient-devel}

%description
A GSSAPI Mechanism that implements NTLMSSP

%package devel
Summary: Development header for GSSAPI NTLMSSP
Group: Development/C
License: LGPLv3+
BuildArch: noarch
Requires: %name = %version-%release

%description devel
Adds a header file with definition for custom GSSAPI extensions for NTLMSSP

%prep
%setup
%patch -p1

%build
mkdir -p m4
%autoreconf
%configure \
    %{subst_with wbclient} \
    --disable-static

%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/gss/mech.d
install -pm644 examples/mech.ntlmssp %buildroot%_sysconfdir/gss/mech.d/ntlmssp.conf
# Clenaup
rm -rf %buildroot%_docdir/%name

%find_lang %name

%check
make test_gssntlmssp

%files -f %name.lang
%config(noreplace) %_sysconfdir/gss/mech.d/ntlmssp.conf
%_libdir/gssntlmssp
%_man8dir/gssntlmssp.8*
%doc README.md COPYING doc/*

%files devel
%_includedir/gssapi/*

%changelog
* Thu Jul 04 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.8.0-alt1
- update to new release

* Fri Aug 31 2018 Alexey Shabalin <shaba@altlinux.org> 0.7.0-alt3
- build with openssl-1.1

* Thu Dec 01 2016 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.0-alt2
- Strict requires for libwbclient, not for libwbclient-sssd

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.0-alt1.qa1
- NMU: rebuilt with libunistring.so.2.

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Thu Nov 13 2014 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt2
- build with krb5-1.13

* Thu Aug 28 2014 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0
- build with wbclient support

* Wed Jul 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Mon Jun 16 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- initial build
