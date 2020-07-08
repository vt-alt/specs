%define _unpackaged_files_terminate_build 1
# Suppress warning emerging from mentioning this macro in changelog
%define _sysconfigdir /etc

# Enable cmake RPATH for unit tests
%global _cmake_skip_rpath %nil

Name: libnss-role
Version: 0.5.0
Release: alt3

Summary: NSS API library and admin tools for roles and privilegies

License: LGPLv2.1
URL: https://github.com/altlinux/libnss-role
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

# https://github.com/altlinux/libnss-role.git
Source: %name-%version.tar

Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed

BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: libcmocka
BuildRequires: libcmocka-devel
BuildRequires: libpam0
BuildRequires: libpam0-devel

Requires: libpam0

%description
NSS API library and admin tools for roles and privilegies.

%package devel
Summary: Header for developing applications managing Roles
Group: Development/Other
Requires: %name = %version-%release

%description devel
Headers for developing applications managing Roles throw
NSS API library for roles and privilegies.

%prep
%setup

%build
%cmake \
	-DNSS_LIBDIR=/%_lib \
	-DROLE_LIBDIR=%_libdir \
	-DMANDIR=%_man8dir \
	-DCMAKE_INSTALL_PREFIX:PATH=%_prefix
%cmake_build

%check
cd BUILD
%make_build test

./checkver %version

%install
%cmakeinstall_std
mkdir -p %buildroot%_sysconfdir/role.d

%post
if [ "$1" = "1" ]; then
    grep -q '^group:[[:blank:]]*\(.\+[[:blank:]]\+\)*role\($\|[[:blank:]]\)' \
        %_sysconfdir/nsswitch.conf || \
    sed -i.rpmorig -e 's/^\(group:.\+\)$/\1 role/g' \
        %_sysconfdir/nsswitch.conf
fi
update_chrooted all

%postun
if [ "$1" = "0" ]; then
    sed -i -e 's/^group:role/group:/g' \
           -e 's/^\(group:\)\(.\+[[:blank:]]*\)*[[:blank:]]\+role\($\|[[:blank:]].*\)$/\1\2\3/g' \
        %_sysconfdir/nsswitch.conf
fi
update_chrooted all

%files
%config(noreplace) %verify(not md5 size mtime) %_sysconfdir/role
%dir %_sysconfdir/role.d
%_sysconfdir/pam.d/role*
/%_lib/libnss_*.so.*
%_sbindir/roleadd
%_sbindir/roledel
%_bindir/rolelst
%_libdir/*.so.*
%_man8dir/*

%files devel
%_libdir/*.so
%_includedir/role/

%changelog
* Wed May 13 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.5.0-alt3
- Fix roleadd installation
- Correct show of project version

* Wed Apr 15 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.5.0-alt2
- Fix install role.d directory (replace mkdir from check section to install)

* Wed Apr 15 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.5.0-alt1
- Add support /etc/role.d directory as addition installable configuration
- Replace build system to cmake
- Add unit testing

* Sat Apr 04 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1.1
- NMU: fixed SConstruct

* Tue Aug 06 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.4.1-alt1
- Fix double memory free with crash before writing (Closes: 37077)

* Wed Jun 19 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- parser.c: fix memory leak
- major refactoring
- increase buffer count for getpwuid/getgrgid/getgrnam
- build with -g, RPM will strip binaries automatically and generate debuginfo

* Fri Apr 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- change URL, Packager, add source url
- rolelst: add -n arg to print gid instead of group names
- print help to stdout
- roleadd/roledel: improve descriptions

* Fri Apr 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- full refactoring

* Fri Apr 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.9-alt2
- fast hack: increase buffers up to 32000

* Sat Jul 14 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.9-alt1
- fix getgrnam_r and getgrgid_r using, increase buffer

* Tue May 02 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.8-alt3
- Fixed fgetc and realloc usage.

* Thu Jul 11 2013 Pavel Shilovsky <piastry@altlinux.org> 0.2.8-alt2
- Merge git.alt branch

* Mon Jul 01 2013 Pavel Shilovsky <piastry@altlinux.org> 0.2.8-alt1
- Skip blank lines in the config file

* Sat Nov 19 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.7-alt4
- Fix devel-file-in-non-devel-package rpmlint violation
- Add comments to configuration due rpmlint violation

* Sat Feb 26 2011 Pavel Shilovsky <piastry@altlinux.org> 0.2.7-alt3
- Replace /etc/nsswitch.conf with %_sysconfigdir/nsswitch.conf

* Sat Jan 15 2011 Pavel Shilovsky <piastry@altlinux.org> 0.2.7-alt2
- Fix module version

* Mon Nov 29 2010 Pavel Shilovsky <piastry@altlinux.org> 0.2.7-alt1
- Add comment support

* Wed Nov 03 2010 Pavel Shilovsky <piastry@altlinux.org> 0.2.6-alt2
- Fix version

* Tue Nov 02 2010 Pavel Shilovsky <piastry@altlinux.org> 0.2.6-alt1
- Bug fixing

* Sun Oct 24 2010 Pavel Shilovsky <piastry@altlinux.org> 0.2.5-alt1
- Add new parsing rules
- Update mans
- Code style and bug fixing
- Delete cpp implementation

* Mon Jul 19 2010 Pavel Shilovsky <piastry@altlinux.org> 0.2.4-alt1
- Fixed librole_reading() error handling
- Set unlimit group len at parse_line()
- rolelst prints group names instead of gids

* Wed Jan 20 2010 Pavel Shilovsky <piastry@altlinux.org> 0.2.3-alt1
- Fixed bugs in pam_check and parser
- Add error messages

* Wed Nov 11 2009 Pavel Shilovsky <piastry@altlinux.org> 0.2.2-alt2
- Fixed passing sisyphus-check

* Wed Nov 11 2009 Pavel Shilovsky <piastry@altlinux.org> 0.2.2-alt1
- Migrated to  c-language utilites
- Bugs' fixing

* Wed Sep 30 2009 Pavel Shilovsky <piastry@altlinux.org> 0.2.1-alt1
- Code refactoring and bug's fixing.

* Fri Sep 11 2009 Pavel Shilovsky <piastry@altlinux.org> 0.2.0-alt1
- Implemented module on C language
- Added work with gids

* Sat Jun 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.6-alt3
- Build with boost-1.39.0
- Fixed bug with local user and group reading
- Improve error handling

* Thu Feb 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.6-alt2
- Remove post_ldconfig and postun_ldconfig
- Fixed potential problem in sections post and postun (#18984)
- Adjusted project URL

* Thu Dec 11 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.6-alt1
- Fixed install directory for system tools
- Fixed manuals
- Improved error handling

* Fri Nov 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.5-alt1
- Replace include files

* Fri Nov 14 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.4-alt1
- Fixed helps for utilities
- Added utilities manuals
- Change project URL

* Wed Oct 29 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.3-alt4
- Fixed libdir installation path for x86_64

* Wed Oct 29 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.3-alt3
- Fixed build with gcc4.3

* Sun Sep 28 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.3-alt2
- Fixed nsswitch.conf update scripts
- Prepared for i18n

* Wed Aug 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.3-alt1
- Added pam support
- Started utils i18n support
- Added class UserReader

* Fri Jul 11 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.2-alt1
- Improved error handling

* Fri Jul 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.1-alt1
- Updated utilities:
 + Fixed roledel
 + Added rolelst

* Thu Jun 26 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1-alt1
- Initial build for ALT

