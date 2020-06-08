Name: zeek-cmake
Version: 20190609
Release: alt1

Summary: CMake scripts used in Zeek

Group: Development/C
License: BSD
Url: https://github.com/zeek/cmake

# Source-url: https://github.com/zeek/cmake/archive/master.zip
Source: %name-%version.tar

BuildArch: noarch
AutoReq: no

%description
This is a collection of CMake scripts intended to be included as a
git submodule in other repositories related to Zeek (www.zeek.org).

* remote logging
* remote events
* distributed data stores


%prep
%setup

# disable rpath
%__subst "s|.*SetupRPATH.*||" CommonCMakeConfig.cmake

%install
mkdir -p %buildroot%_datadir/%name/
cp -a * %buildroot%_datadir/%name/

%files
%doc COPYING README
%_datadir/%name/

%changelog
* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 20190609-alt1
- initial build for ALT Sisyphus
