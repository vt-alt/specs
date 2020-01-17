Name: rrd
Version: 1.7.2
Release: alt2
%define native rrdtool
%define abiversion 8
%define rrdcached_user root
%def_with tcl

# fixed rrdcached.pid place
# https://lists.altlinux.org/pipermail/devel/2017-October/203277.html
%define	_localstatedir	/var

Summary: RRD - round robin database
License: GPL-2.0+ AND LGPL-2.0+
Group: Development/Databases

Url: http://oss.oetiker.ch/rrdtool

Source0: http://oss.oetiker.ch/rrdtool/pub/%native-%version.tar
Source1: rrdcached.init
Source2: rrdcached.sysconfig

Source10: MRTG-HOWTO

Patch0: rrd-1.7.2-alt-build-tcl.patch
Patch1: rrdtool-1.4.5-automake-1.11.2.patch
Patch2: rrdtool-1.4.7-alt-DSO.patch
Patch3: rrdtool-1.5.3-top-dir.patch

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-build-python3
BuildRequires: rpm-build-licenses
BuildRequires: chrpath
BuildRequires: python3-module-setuptools
%if_with tcl
BuildRequires: rpm-build-tcl tcl-devel
%endif

# Automatically added by buildreq on Wed Oct 12 2011
BuildRequires: groff-base libdbi-devel libpango-devel libpng-devel libxml2-devel lua5 perl-Pod-Parser perl-devel python3-devel

Summary(ru_RU.UTF-8): RRDtool - база данных с "циклическим обновлением"

%package -n lib%name%abiversion
Summary: Round Robin Database shared library
Group: System/Libraries
Requires: fonts-ttf-dejavu
Provides: lib%name = %version-%release

%package -n lib%name-devel
Summary: Round Robin Database development files and documentation
Group: Development/C
Requires: lib%name = %version-%release
Provides: %native-devel = %version
Obsoletes: %native-devel < %version

%package utils
Summary: Round Robin Database utilities
Group: Development/Databases
Requires: lib%name = %version-%release
Provides: %native = %version
Obsoletes: %native < %version

%package cached
Summary: Data caching daemon for RRDtool
Group: Databases
Requires: lib%name = %version-%release

%package man
Summary: Round Robin Database man pages
Group: Development/Documentation
BuildArch: noarch

%package doc
Summary: Round Robin Database documentation/examples
Group: Development/Documentation
BuildArch: noarch

%package -n perl-RRD
Summary: Round Robin Database perl modules
Group: Development/Databases
Requires: lib%name = %version-%release
Provides: %name-perl = %version
Obsoletes: %name-perl < %version

%package -n python3-module-rrdtool
Summary: Round Robin Database python modules
Group: Development/Databases
Requires: lib%name = %version-%release
Provides: python3-module-rrd = %version
Obsoletes: python3-module-rrd < 1.5.4-alt2

%if_with tcl
%package tcl
Summary: Round Robin Database tcl extension
Group: Development/Databases
Requires: lib%name = %version-%release
%endif

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

%description -l ru_RU.UTF-8
RRD - сокращение для "Round Robin Database" (база данных с "циклическим
обновлением"). RRD - система для сохранения и показа информации за
определённый промежуток времени (например скорость передачи данных в
сети, температуру в машинном зале, среднюю загрузку сервера). Она
сохраняет данные в очень компактной форме, так что данные не будут
занимать всё больше и больше места с течением времени и предоставляет
разумное графическое представление информации. Может быть использована
как из простых скриптов (shell, perl, etc), так встроена в программы,
которые опрашивают сетевые устройства и показывают данные в удобном
для пользователя виде.

%description -n lib%name%abiversion
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average).

This package contains shared library required for running RRD-based software.

%description -n lib%name-devel
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average).

This package contains development files and documentation required for
development of RRD-based software.

%description utils
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

This package contains utilities for manipulating Round Robin Databases.

%description cached
rrdcached is a daemon that receives updates to existing RRD files,
accumulates them and, if enough have been received or a defined time has
passed, writes the updates to the RRD file.  The daemon was written with
big setups in mind which usually runs into I/O related problems.  This
daemon was written to alleviate these problems.

%description man
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

This package contains man pages for Round Robin Databases.

%description doc
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

This package contains documentations for manipulating Round Robin Databases.
Some examples included too.

%description -n perl-RRD
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

This package contains perl modules for access the Round Robin Databases.

%description -n python3-module-rrdtool
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

This package contains python modules for access the Round Robin Databases.

%if_with tcl
%description tcl
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). It stores the data in a very compact way that will not
expand over time, and it presents useful graphs by processing the data to
enforce a certain data density. It can be used either via simple wrapper
scripts (from shell or Perl) or via frontends that poll network devices and
put a friendly user interface on it.

This package contains tcl extension for access the Round Robin Databases.
%endif

%prep
%setup -n %native-%version
%patch0 -p2

find doc bindings/perl-piped -type f -print0 |
	xargs -r0 fgrep -l /usr/local |
	xargs -r perl -pi -e 's,/usr/local,%prefix,g'

# temporary hack for build tcl subpackage in Sisyphus
# https://lists.altlinux.org/pipermail/devel/2017-October/203186.html
sed -i 's@$TCL_PACKAGE_PATH@%_tcldatadir@g' configure.ac

%build
export PYTHON=%__python3
%add_optflags -I%_builddir/%native-%version/src %optflags_shared -I%_includedir/cgilib -lpng
%autoreconf
%configure \
	--disable-rpath \
	--enable-shared \
	--with-pic \
	--disable-static \
%if_with tcl
	--with-tcllib=%_libdir \
%endif
	--disable-ruby \
	--disable-lua

%make_build

make -C bindings clean

export LD_LIBRARY_PATH=$PWD/src/.libs
pushd bindings/perl-piped
	%perl_vendor_build
popd

pushd bindings/perl-shared
	%perl_vendor_build
popd

%install
pushd bindings/perl-piped
	%perl_vendor_install
popd

pushd bindings/perl-shared
	%perl_vendor_install
popd
pushd bindings
%make python
popd

%if_with tcl
mkdir -p %buildroot%_tcllibdir/
%endif
make DESTDIR=%buildroot install

# seems to have changed in newer configure,
# didn't find it in 5 min; fix here // mike
mv %buildroot%_datadir/%native/examples %buildroot%_docdir/%native-%version/
# ...and %buildroot%_datadir/%native isn't needed more ;-) //asy
rmdir %buildroot%_datadir/%native

# RPATH
find %buildroot -name '*.so' | xargs -n 1 chrpath -d

cp CONTRIBUTORS COPYRIGHT TODO NEWS THREADS LICENSE  %buildroot%_docdir/%native-%version/

#
# rrdcached
#
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT%_localstatedir/lib/rrdcached
install -m644 %SOURCE1 $RPM_BUILD_ROOT%_initdir/rrdcached
sed -e 's|@@USER@@|%rrdcached_user|g' < %SOURCE2 > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/rrdcached

# warning: Installed (but unpackaged) file(s) found:
#    /usr/lib/perl/5.16.3/RRDp.pm
#    /usr/lib/perl/5.16.3/x86_64-linux-thread-multi/RRDs.pm
#    /usr/lib/perl/5.16.3/x86_64-linux-thread-multi/auto/RRDp/.packlist
#    /usr/lib/perl/5.16.3/x86_64-linux-thread-multi/auto/RRDs/.packlist
#    /usr/lib/perl/5.16.3/x86_64-linux-thread-multi/auto/RRDs/RRDs.bs
#    /usr/lib/perl/5.16.3/x86_64-linux-thread-multi/auto/RRDs/RRDs.so
#    /usr/lib/perl/5.16.3/x86_64-linux-thread-multi/perllocal.pod
rm -rf %buildroot/usr/lib/perl

# warning: Installed (but unpackaged) file(s) found:
#    /usr/share/locale/hu/LC_MESSAGES/rrdtool.mo
# hu only in 1.7.0, removed
rm -f %buildroot/usr/share/locale/hu/LC_MESSAGES/rrdtool.mo

%pre cached
# %%rrdcached_user is root now, so groupadd/useradd is not needed
#/usr/sbin/groupadd -rf %rrdcached_user
#/usr/sbin/useradd -r -g %rrdcached_user -d /dev/null -s /dev/null -c "rrdcached daemon" %rrdcached_user &>/dev/null ||:

%post cached
%post_service rrdcached

%preun cached
%preun_service rrdcached

%files -n lib%name%abiversion
%doc COPYRIGHT
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib*.so
%_libdir/pkgconfig/*

%files utils
%doc COPYRIGHT
%exclude %_bindir/rrdcached
%_bindir/*

%files cached
%_bindir/rrdcached
%attr(0755,root,root) %config %_initdir/rrdcached
%config(noreplace) %_sysconfdir/sysconfig/rrdcached
%attr(3775,root,%rrdcached_user) %dir %_localstatedir/lib/rrdcached

%files man
%_man1dir/*
%_man3dir/lib*

%files doc
%dir %_docdir/%native-%version
%doc %_docdir/%native-%version/*

%files -n perl-RRD
%perl_vendor_privlib/RRD*
%perl_vendor_archlib/RRD*
%perl_vendor_autolib/RRD*

%files -n python3-module-rrdtool
%python3_sitelibdir/*

%if_with tcl
%files tcl
%_libdir/tcl*.so
%endif

# TODO:
# - make proper switches for language bindings
#   (the tcl one looks broken too as of 1.5.4-alt2.1)

%changelog
* Thu Jan 09 2020 Anton Farygin <rider@altlinux.ru> 1.7.2-alt2
- switched to python-3.7
- fixed License and added copyright to library and utils package

* Thu Jan 09 2020 Anton Farygin <rider@altlinux.ru> 1.7.2-alt1
- 1.7.0 -> 1.7.2 (closes: #37648)

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1.1
- rebuild with new perl 5.26.1

* Sat Oct 28 2017 Sergey Y. Afonin <asy@altlinux.ru> 1.7.0-alt1
- 1.7.0 (abiversion changed to 8)
- added python-module-setuptools to BuildRequires
- enabled tcl bindings (used temporary hack)
- redefined _localstatedir

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt3
- rebuilt with libdbi-0.9.0
- removed "Packager" field
- moved build requires for tcl into if_with section
- disabled tcl bindings

* Wed Feb 22 2017 Michael Shigorin <mike@altlinux.org> 1.5.4-alt2.2
- dropped BR: ruby as it's unconditionally disabled anyways

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt2.1
- rebuild with new perl 5.24.1

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt2
- NMU: python-module-rrd renamed to python-module-rrdtool

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 25 2015 Sergey Y. Afonin <asy@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Sat Jun 20 2015 Sergey Y. Afonin <asy@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.4.7-alt4
- built for perl 5.18

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt3.1
- Rebuilt with libpng15

* Mon Sep 03 2012 Vladimir Lettiev <crux@altlinux.ru> 1.4.7-alt3
- rebuilt for perl-5.16

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt2.1
- Fixed build

* Fri May 04 2012 Michael Shigorin <mike@altlinux.org> 1.4.7-alt2
- fixed FTBFS using automake-1.11 with a gentoo patch

* Mon Feb 27 2012 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt1
- new version 1.4.7 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt1.3
- Rebuild with Python-2.7

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 1.4.5-alt1.2
- rebuilt for perl-5.14

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.5-alt1.1
- Rebuilt for debuginfo

* Sun Jan 02 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.4.4-alt1.1
- rebuilt with perl 5.12

* Wed Jul 14 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Fri May 07 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.4.3-alt5
- fixed URL

* Wed May 05 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.4.3-alt4
- changed "License: %gpl2only" to "License: %gpl2plus with exceptions"
- added CONTRIBUTORS,COPYRIGHT,README,TODO,NEWS,THREADS to rrd-doc package
- added "Requires: fonts-ttf-dejavu" for librrd package (thanks john#sakh.com)
- separated rrd-cached package, initial configuration for rrdcached

* Fri Apr 16 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.4.3-alt3
- fixed renaming rrd-perl and rrd-pythnon (added Provides, thanks vsu@)
- separated man and doc packages (noarch)

* Thu Apr 15 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.4.3-alt2
- renamed librrd to librrd4 (according SharedLibsPolicy)

* Wed Apr 14 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.4.3-alt1
- 1.4.3 (closes: ALT#23331)
- Removed rrd-1.2.28-alt-compile.patch
- renamed rrd-perl to perl-RRD

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.30-alt1.1
- Rebuilt with python 2.6

* Mon Mar 23 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.30-alt1
- 1.2.30
- renamed rrd-pythnon to python-module-rrd

* Sun Jan 11 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.29-alt1
- 1.2.29

* Fri Sep 05 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.28-alt1
- 1.2.28

* Fri Mar 07 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.27-alt1
- 1.2.27

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.2.26-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 19 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.26-alt1
- 1.2.26

* Sat May 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.23-alt1
- 1.2.23

* Sun Nov 05 2006 Michael Shigorin <mike@altlinux.org> 1.2.15-alt1
- 1.2.15
- accepted changes by lav@:
  * Sun Nov 05 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.15-alt0.1
  + NMU: new version, fix tcl installation on x86_64
  + fix tcl installation on x86 too
  + fix perl module linking
  + cleanup spec, add russian description, remove strange patches
- added Packager:, other minor spec cleanups

* Thu Jun 29 2006 Michael Shigorin <mike@altlinux.org> 1.2.13-alt1
- 1.2.13
- NMU: fix x86_64 build
- updated patch0 (sort of...)
- disabled tcl subpackage build (too much hassle right now)
  + first it seemed like these are troublesome on x86_64,
    later it apeared that i586 build is broken too
- minor spec cleanup

* Tue Jan 17 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Sun Oct 09 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.11-alt1
- fix tcl bindings package

* Fri Sep 16 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.11-alt0
- 1.2.11

* Wed Jun 29 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.2.10-alt0
- 1.2.10
- Added Python module

* Sun Aug 29 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0.49-alt1
- 1.0.49

* Mon Dec 15 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0.45-alt2
- remove *.la from package

* Mon Sep 08 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0.45-alt1
- 1.0.45
- rebuild with hasher

* Thu Jan 30 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.0.40-alt1
- 1.0.40

* Wed Oct 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.33-alt1
- 1.0.33.
- Added missing RRDs.pm module.
- Moved static library to devel-static subpackage.
- Relocated documentation.
- Built with libpng.so.3

* Tue Jul 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.30-ipl3mdk
- Rebuilt with new perl.

* Mon Jun 25 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.0.30-ipl2mdk
- Rebuilt with perl-5.6.1

* Tue Feb 20 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.30-ipl1mdk
- 1.0.30.

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> 1.0.28-ipl1mdk
- Initial revision.

