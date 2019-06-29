Name: xygrib-maps-HiRes
Version: 0.1
Release: alt1

Summary: Higher resolution maps for XyGrib

License: %gpl2only
Group: Networking/Other
Url: https://opengribs.org/en/downloads
Source0: XyGrib___High_Resolution_Maps.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: xygrib-data

%description
This package contains higher resolution maps (200 m and 100 m) for
XyGrib (warning: size of package about 74Mb). This is a part of
GSHHS 1.9 distribution from ftp://ftp.soest.hawaii.edu/gshhg/legacy/

%prep

%build

%install

%__mkdir_p %buildroot%_datadir/openGribs/XyGrib

# README excluded because it is contained in the package zygrib-data
tar xzf %SOURCE0 -C %buildroot/%_datadir/openGribs/XyGrib --exclude=README.*
pushd %buildroot/%_datadir/openGribs/XyGrib/data
    mv data/* .
    rm -r data
popd

%files
%attr(0644,root,root) %_datadir/openGribs/XyGrib/data/maps/gshhs/*

%changelog
* Fri Jun 28 2019 Sergey Y. Afonin <asy@altlinux.ru> 0.1-alt1
- Initial build for AltLinux
