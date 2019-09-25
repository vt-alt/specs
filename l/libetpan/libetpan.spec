Name: libetpan
Version: 1.9.3
Release: alt3

Summary: This mail library  provide a portable, efficient middleware for different kinds of mail access
License: %bsdstyle
Group: Development/C

Url: https://www.etpan.org/libetpan.html

# git://github.com/dinhviethoa/libetpan.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
# Patches from upstream git.
# Must be dropped when new version is released.
Patch1: Fixed-return-code-of-mailimap_logout-327.patch
Patch2: Fix-mailmime_write-add-handler-for-MAILMIME_FIELD_LO.patch
Patch3: Fix-TLS-timeouts-with-recent-versions-of-GnuTLS-330.patch
Patch4: mailimap_quota_getquotaroot-Fix-SIGSEGV-334.patch

%def_with gnutls
%def_without openssl

%define _unpackaged_files_terminate_build 1

BuildRequires(pre): rpm-build-licenses

# FIXME: Is it really needed g++?
BuildRequires: gcc-c++

%{?_with_gnutls:BuildRequires: libgnutls-devel libgcrypt-devel libgpg-error-devel zlib-devel}
%{?_with_openssl:BuildRequires: libssl-devel}
BuildRequires: libsasl2-devel
BuildRequires: liblmdb-devel
BuildRequires: liblockfile-devel libexpat-devel libcurl-devel

%package devel
Summary: Development environment for %name library.
Group: Development/C
Requires: %name = %version-%release
%{?_with_gnutls:Requires: libgnutls-devel libgcrypt-devel libgpg-error-devel zlib-devel}
%{?_with_gnutls:Requires: libssl-devel}
Requires: libsasl2-devel
Requires: liblmdb-devel
Requires: liblockfile-devel

%description
The purpose of this mail library is to provide a portable, efficient
middleware for different kinds of mail access. When using the drivers
interface, the interface is the same for all kinds of mail access,
remote and local mailboxes.

%description devel
This package contains the header files and libraries for building
program which use lib%name.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
ln -s README.md README

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_with openssl} \
	%{subst_with gnutls} \
	--enable-lmdb \
	--enable-ipv6
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog NEWS COPYRIGHT README AUTHORS
%_libdir/%name.so.*

%files devel
%_bindir/%name-config
%dir %_includedir/%name
%_includedir/%name/*.h
%_includedir/%name.h
%_libdir/%name.so

%changelog
* Mon Sep 23 2019 Mikhail Efremov <sem@altlinux.org> 1.9.3-alt3
- Patch from upstream:
    + mailimap_quota_getquotaroot: Fix SIGSEGV (#334).

* Thu May 16 2019 Mikhail Efremov <sem@altlinux.org> 1.9.3-alt2
- Patches from upstream:
    + Fixed return code of mailimap_logout (#327).
    + Fix mailmime_write(): add handler for
      MAILMIME_FIELD_LOCATION (#329).
    + Fix TLS timeouts with recent versions of GnuTLS (#330).

* Thu Feb 21 2019 Mikhail Efremov <sem@altlinux.org> 1.9.3-alt1
- Patches from upstream:
  + Fix the compiler warning against uninitialized use (#323)
  + add missing stddef.h include for 'NULL' (#322)
- Updated to 1.9.3.

* Fri Dec 21 2018 Mikhail Efremov <sem@altlinux.org> 1.9.2-alt1
- Drop upstreamed patch.
- Use liblmdb instead of libdb4.7.
- Updated to 1.9.2.

* Tue Oct 30 2018 Mikhail Efremov <sem@altlinux.org> 1.9.1-alt3
- Enable TLS-1.3 again.
- Add TLS server name indication support.

* Tue Oct 09 2018 Mikhail Efremov <sem@altlinux.org> 1.9.1-alt2
- Disable TLS-1.3 for now.

* Fri Sep 21 2018 Mikhail Efremov <sem@altlinux.org> 1.9.1-alt1
- Fix 'may be used uninitialized' warning.
- Fix from upstream:
  + Fixed snprintf() output.
- Updated to 1.9.1.

* Mon Jun 19 2017 Mikhail Efremov <sem@altlinux.org> 1.8-alt1
- Updated to 1.8.

* Tue Jul 19 2016 Mikhail Efremov <sem@altlinux.org> 1.7.2-alt2
- Patch from upstream:
  + Fixed crash with IDLE.

* Thu Jun 16 2016 Mikhail Efremov <sem@altlinux.org> 1.7.2-alt1
- Patch from upstream:
  + Fixed memory leak.
- Updated to 1.7.2.

* Thu Apr 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7-alt1
- Updated to 1.7.

* Fri Dec 04 2015 Mikhail Efremov <sem@altlinux.org> 1.6-alt2
- Rebuild with gnutls-3.4.x.

* Mon Nov 10 2014 Mikhail Efremov <sem@altlinux.org> 1.6-alt1
- Updated to 1.6.

* Thu Aug 21 2014 Mikhail Efremov <sem@altlinux.org> 1.5-alt1
- Update Url.
- Updated to 1.5.

* Tue Sep 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.1-alt1.1
- NMU: rebuilt with cyrus-sasl 2.1.26

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.1-alt1
- Fix License.
- Updated to 1.1.

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58-alt2
- Rebuilt for soname set-versions

* Mon Aug 10 2009 Alexey Rusakov <ktirf@altlinux.org> 0.58-alt1.1
- now really fixed ALT #10833.
- updated buildreqs slightly.

* Sun Aug 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.58-alt1
- 0.58
- removed obsolete post/postun macros.
- fixed -devel subpackage requires (closing ALT #10833).

* Thu Oct 16 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.57-alt1.1
-  build with new GnuTLS.

* Fri Oct 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.57-alt1
-  0.57.

* Mon Oct 06 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.56-alt1
-  0.56.

* Mon Aug 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.54-alt1
-  0.54.

* Thu Sep 27 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.52-alt1
-  0.52.

* Fri May 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.49-alt1
-  0.49.

* Wed Nov 29 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.48-alt1
-  0.48.

* Wed Oct 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.47cvs5-alt1
-  0.47.

* Mon Aug 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.46-alt1
-  0.46.

* Fri Jun 16 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.45-alt1.1
-  rebuild with new gnutls.

* Tue Mar 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.45-alt1
-  0.45.

* Mon Mar 20 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.43-alt1
-  0.43.

* Wed Dec 07 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.41-alt1
-  0.41.

* Wed Nov 09 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.40-alt1
-  0.40.

* Tue Oct 04 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.39.1-alt1
- 0.39. 

* Mon Aug 01 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.38-alt1
-  0.38.

* Wed Jul 13 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.37-alt0.2
-  missing requires added.

* Wed Jul 13 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.37-alt0.1
-  initial build.


