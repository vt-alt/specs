Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pod2man
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# TODO: fixes scons to generate debug information
%global debug_package %{nil}

%define _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/xsunpinyin.conf
%define gitdate 20190805

Name:		sunpinyin
Version:	3.0.0
Release:	alt1_0.5.20190805git
Summary:	A statistical language model based Chinese input method engine
License:	LGPLv2 or CDDL
URL:		http://code.google.com/p/sunpinyin/
Source0:	%{name}-%{gitdate}.tar.xz
Source2:	http://downloads.sourceforge.net/project/open-gram/lm_sc.3gm.arpa-20140820.tar.bz2
Source3:	http://downloads.sourceforge.net/project/open-gram/dict.utf8-20131214.tar.bz2
Patch0: 	sunpinyin-use-python3.patch
Patch1: 	sunpinyin-fixes-scons.patch
BuildRequires:  gcc-c++
BuildRequires:	libsqlite3-devel
BuildRequires:	gettext gettext-tools	
BuildRequires:	scons
BuildRequires:	perl(Pod/Man.pm)
BuildRequires:	python3-devel
Source44: import.info

%description
Sunpinyin is an input method engine for Simplified Chinese. It is an SLM based
IM engine, and features full sentence input.

SunPinyin has been ported to various input method platforms and operating 
systems. The 2.0 release currently supports iBus, XIM, and Mac OS X. 

%package devel
Group: Development/C
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files that allows user
to write their own front-end for sunpinyin.

%package data
Group: System/Libraries
Summary:	Little-endian data files for %{name}
License:	CC-BY-SA
Obsoletes:	%{name}-data-le
Obsoletes:	%{name}-data-be

%description data
The %{name}-data package contains necessary lexicon data and its index data
files needed by the sunpinyin input methods.

%prep
%setup -q -n %{name}-%{gitdate}
%patch0 -p1 -b .python3
%patch1 -p1 -b .scons

mkdir -p raw
cp %SOURCE2 raw
cp %SOURCE3 raw
pushd raw
tar xvf lm_sc.3gm.arpa-20140820.tar.bz2
tar xvf dict.utf8-20131214.tar.bz2
popd

%build
# export CFLAGS, CXXFLAGS, LDFLAGS, ...
%configure || :

scons %{?_smp_mflags} --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir}
export PATH=`pwd`/src:$PATH
pushd raw
ln -sf ../doc/SLM-inst.mk Makefile
%make_build VERBOSE=1
popd

%install
scons %{?_smp_mflags} --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir} install --install-sandbox=%{buildroot}
pushd raw
make install DESTDIR=%{buildroot} INSTALL="install -p"
popd

# additional %%doc files to include by path to avoid duplicates/conflicts
# see https://bugzilla.redhat.com/1001266
install -m0644 AUTHORS TODO %{buildroot}%{_docdir}/%{name}




%files
%doc --no-dereference COPYING *.LICENSE
%{_libdir}/libsunpinyin*.so.*
%{_docdir}/%{name}/README
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/TODO

%files devel
%{_libdir}/libsunpinyin*.so
%{_libdir}/pkgconfig/sunpinyin*.pc
%{_includedir}/sunpinyin*

%files data
%{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_docdir}/%{name}/SLM-*.mk

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_0.5.20190805git
- new version

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 2.0.4-alt2_0.11
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.11
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.9
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.8
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_0.7
- initial fc import

