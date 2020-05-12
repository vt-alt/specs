%def_enable shared
%def_enable static
%def_enable nls

Name: progsreiserfs
%define lname lib%name
Version: 0.3.0.5
Release: alt4
Summary: Programs needed for manipulating reiserfs partitions
Summary(ru_RU.UTF-8): Программа для манипулирования разделами диска с reiserfs
Summary(uk_UA.UTF-8): Програми для маніпулювання розділами диску з reiserfs
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
# Url: ftp://ftp.namesys.com/pub/libreiserfs/
Source: %name-%version.tar
Patch: %name-%version-m4.patch
Patch1: libreiserfs-0.3.0.5-gettext.patch
%{?_enable_shared:Requires: %lname = %version-%release}

BuildRequires: libuuid-devel

%description
%name is a package that allows you to create, destroy, resize and copy
reiserfs filesystem.

%description -l uk_UA.UTF-8
%name - пакет, який дозволє створювати, знищувати, змінювати розмір та
копіювати файлову систему reiserfs.

%description -l ru_RU.UTF-8
%name - пакет для создания, удаления, изменения рамера и копирования файловой системы reiserfs.

%if_enabled shared
%package -n %lname
Summary: Shared library for reiserfs utilities
Group: System/Libraries

%description -n %lname
This package includes the shared library needed to run %lname-based
software.
%endif


%package -n %lname-devel
Summary: Files required to compile software that uses %lname
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
This package includes the header files for %lname.


%if_enabled static
%package -n %lname-devel-static
Summary: Files required to compile statically linked software that uses %lname
Group: Development/C
Requires: %lname = %version-%release

%description -n %lname-devel-static
This package includes the libraries needed to statically link software with
%lname.
%endif

%prep
%setup -q
%patch -p1
%patch1 -p1
for f in mk tune; do
	sed -i -r "s/(${f}fs)\.(reiserfs)/\2.\1/g" doc/${f}fs.reiserfs.8
done
[ -e config.rpath ] || :> config.rpath


%build
%autoreconf -fisv
%configure \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_enable nls} \
	--enable-threads=posix \
	--enable-largefile \
	--disable-rpath \
	--with-gnu-ld
%make_build
gzip -9c ChangeLog > ChangeLog.gz


%install
%makeinstall_std
for f in mk tune; do
	mv %buildroot%_sbindir/{${f}fs.reiserfs,reiserfs.${f}fs}
	mv %buildroot%_man8dir/{${f}fs.reiserfs,reiserfs.${f}fs}.8
done


%files
%doc AUTHORS ChangeLog.* NEWS README THANKS
%_sbindir/*
%_man8dir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%{?_enable_shared:%_libdir/*.so}
%_includedir/*
%_datadir/aclocal/*


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%changelog
* Tue May 05 2020 Anton Midyukov <antohami@altlinux.org> 0.3.0.5-alt4
- Fix build with gettext > 0.20
- Cleanup spec

* Thu Jul 04 2013 Led <led@altlinux.ru> 0.3.0.5-alt3
- rename tunefs.reiserfs* to reiserfs.tunefs*
  (conflicts w/reiserfsprogs)

* Tue Mar 12 2013 Led <led@altlinux.ru> 0.3.0.5-alt2
- fixed %name.m4
- cleaned up BuildRequires
- fixed reiserfs.mkfs man page

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0.5-alt1.2
- Rebuilt for debuginfo

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.3.0.5-alt1.1
- rebuild (with the help of girar-nmu utility)

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 0.3.0.5-alt1
- 0.3.0.5
  + no more fsck
  + no more doc/API
  + removed patches
- buildreq
- me as a (inappropriate) Packager: again

* Tue Aug 19 2008 Led <led@altlinux.ru> 0.3.0.4-alt3
- cleaned up spec
- cleaned up BuildRequires

* Thu Jan 19 2006 Led <led@altlinux.ru> 0.3.0.4-alt2
- added patch from Ubuntu
- added API to %lname-devel's docs
- fixed spec

* Thu Jan 19 2006 Led <led@altlinux.ru> 0.3.0.4-alt1
- new version
- enable lib%name-devel-static
- fix spec
- rename fsck.reiserfs to reiserfs.fsck and mkfs.reiserfs* to reiserfs.mkfs*
  (conflicts w/reiserfsprogs)
- build static library by default

* Fri Dec 26 2003 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.4
- removed *.la
- don't build static library by default

* Fri Nov 08 2002 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.3
- patch from Yury Umanets is applied
- moved libs to /lib (see alt0.2)
- not including /sbin/fsck.reiserfs (conflicts w/reiserfsprogs and a stub anyway)

* Thu Nov 07 2002 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.2
- moved utils from /usr/sbin to /sbin (#1057)

* Tue Oct 29 2002 Michael Shigorin <mike@altlinux.ru> 0.3.0.3-alt0.1
- 0.3.0.3

* Wed Feb 20 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.7-alt1
* New version of the progsreiserfs

* Mon Feb 18 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.6-alt2
- Copyright information fixed.
- progsreiserfs.spec fixed.
- THANKS file added.
- NAMESYS-README added.

* Sun Feb 16 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.6-alt1
- New version of the progsreiserfs packed.

* Mon Feb 11 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.5-alt2
- Some progsreiserfs.spec fixes.

* Mon Feb 11 2002 Yury Umanets <umka@altlinux.ru> progsreiserfs-0.1.5-alt1
- Initial release

