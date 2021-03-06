# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		fcitx-m17n
Version:	0.2.4
Release:	alt1_1
Summary:	M17n Engine for Fcitx
Group:		System/Libraries
License:	LGPLv2+
URL:		https://fcitx-im.org/wiki/M17N
Source0:	http://download.fcitx-im.org/fcitx-m17n/%{name}-%{version}.tar.xz

BuildRequires:	ctest cmake, fcitx-devel gettext gettext-tools, intltool, libm17n-devel
Requires:	fcitx
Source44: import.info

%description
Fcitx-m17n is a M17n engine wrapper for Fcitx. 
It allows input of many languages using the 
input table maps from m17n-db.

%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%{fedora_cmake} ..
%make_build VERBOSE=1
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README.rst
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/m17n/default

%changelog
* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_1
- update to new version by fcimport

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.1.3-alt2
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_2
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_1
- initial fc import

