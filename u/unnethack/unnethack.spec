Name: unnethack
Version: 5.3.2
Release: alt2
Summary: An enhancement to the dungeon exploration game NetHack
Group: Games/Adventure
Url: https://unnethack.wordpress.com
License: NGPL
Source: %version.tar.gz
Patch: bison3.7.patch

# Automatically added by buildreq on Sat Nov 26 2011
# optimized out: libtinfo-devel
BuildRequires: flex groff-base libgsl-devel libncurses-devel

%description
UnNetHack is a variant of NetHack.

It features more randomness, more levels, more challenges and more fun
than vanilla NetHack.

%prep
%setup
%patch -p1

%build
LIBS=-lgsl %configure --enable-curses-graphics
# Parallel build races
make include/autoconf_paths.h
make -C src ../include/date.h
%make_build
#make
make -C util recover lev_comp dgn_comp

%install
%make install DESTDIR=%buildroot CHOWN=echo CHGRP=echo CHMOD=echo
mv %buildroot%_datadir/%name/recover %buildroot%_bindir/%name.recover && \
  ln -rs %_bindir/%name.recover %buildroot%_datadir/%name/recover
mv %buildroot%_datadir/%name/%name %buildroot%_bindir/%name.bin && \
  ln -rs %_bindir/%name.bin %buildroot%_datadir/%name/%name
for u in dlb dgn_comp lev_comp tilemap; do
  install util/$u %buildroot%_bindir/%name.$u &&
  ln -rs %buildroot%_bindir/%name.$u %buildroot%_datadir/%name/$u
done

%files
%doc doc README
%attr(2711,root,games) %_bindir/*.bin
%_bindir/*[^n]
%_datadir/%name
%_defaultdocdir/%name
%dir %attr(775,root,games) %_localstatedir/%name
%attr(775,root,games) %_localstatedir/%name/[sbl]*
%attr(664,root,games) %_localstatedir/%name/[^sbl]*

%changelog
* Mon Apr 19 2021 Fr. Br. George <george@altlinux.ru> 5.3.2-alt2
- Fix install bug

* Fri Apr 16 2021 Fr. Br. George <george@altlinux.ru> 5.3.2-alt1
- Autobuild version bump to 5.3.2

* Fri Jan 15 2021 Fr. Br. George <george@altlinux.ru> 5.2.0-alt3
- Fix build with gcc10, eliminate build in install section
- Disable parallel build due to races

* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 5.2.0-alt2
- Fix parallel build

* Wed Oct 16 2019 Fr. Br. George <george@altlinux.ru> 5.2.0-alt1
- Autobuild version bump to 5.2.0

* Thu Feb 27 2014 Fr. Br. George <george@altlinux.ru> 5.1.0-alt1
- Autobuild version bump to 5.1.0
- Fix build

* Thu Apr 19 2012 Fr. Br. George <george@altlinux.ru> 4.0.0-alt1
- Autobuild version bump to 4.0.0

* Thu Mar 01 2012 Fr. Br. George <george@altlinux.ru> 3.6.1-alt1
- Autobuild version bump to 3.6.1

* Sun Nov 27 2011 Fr. Br. George <george@altlinux.ru> 3.6.0-alt1
- Autobuild version bump to 3.6.0
- Snapshot version corrected manually
- Patchset fix

* Sun Nov 27 2011 Fr. Br. George <george@altlinux.ru> 3.5.3-alt20101010.1
- Initial build from scratch

