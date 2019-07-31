# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		0
%define libwlocate	libwlocate%{major}
%define libwlocate_d	libwlocate-devel
%define git		git20130127
%define rel		10

Name:		libwlocate
Version:	1.1
Release:	alt1_%rel.%git
Summary:	Open WLAN Map interface library

Group:		Development/C
License:	MIT
URL:		http://code.google.com/p/wlocate/
Source0:	libwlocate-git.tar.bz2
Patch0:		libwlocate-cflags.patch

BuildRequires:	libwireless-devel
Source44: import.info

%description
Library for doing location lookup based on free openwlanmap.org data.

    * accessing the local WLAN-hardware
    * checking for WLAN-networks that are available
    * accessing the database
    * returning the current geographic position or an error code in case localisation failed

#------------------------------------------------------------------------------

%package -n	%{libwlocate}
Summary:	Open WLAN Map interface library
Group:		System/Libraries
Provides:	%name = %version-%release
Provides:	%arch_tagged libwlocate.so

%description -n	%{libwlocate}
Library for doing location lookup based on free openwlanmap.org data.

    * accessing the local WLAN-hardware
    * checking for WLAN-networks that are available
    * accessing the database
    * returning the current geographic position or an error code in case localisation failed

%files -n %{libwlocate}
%_libdir/*.so.%{major}
%_libdir/*.so

#------------------------------------------------------------------------------

%package -n	%{libwlocate_d}
Summary:	Devel files needed to build apps based on %name
Group:		Development/C
Requires:	%{libwlocate} = %version
Provides:	%name-devel = %version-%release

%description -n	%{libwlocate_d}
Devel files needed to build apps based on %name.

%files -n %{libwlocate_d}
%_includedir/libwlocate.h
%_libdir/*.so

#-----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p1


%build


make -f Makelib

%install
mkdir -p %{buildroot}/%_libdir %{buildroot}/usr/include
# ensure .so files are executable (0755) for proper -debuginfo extraction
install -m0755 libwlocate.so %{buildroot}/%_libdir/libwlocate.so.0
ln -sf libwlocate.so.0 %{buildroot}/%_libdir/libwlocate.so
install -m0644 libwlocate.h %{buildroot}/usr/include/

chmod 0644 COPYING CREDITS README



%changelog
* Mon Jul 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_10.git20130127
- fixed devel (closes: #37049)

* Tue Apr 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.git201301279
- new version

