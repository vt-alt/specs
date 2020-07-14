Name: colortail
Version: 0.3.3
Release: alt1

Summary: A colorised tail with configuration files
License: GPLv2+
Group: Monitoring

Url: http://joakimandersson.se/projects/colortail/
Source: %name-%version.tar.gz

BuildRequires: gcc-c++

%description
Colortail is a log colorizer make log checking easier.
It works like tail but can read one or more configuration files.
In which it's specified which patterns result in which colors.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall
install -d %buildroot/%_sysconfdir/%name
install -pm644 example-conf/conf* %buildroot/%_sysconfdir/%name

%files
%doc INSTALL README AUTHORS ChangeLog BUGS TODO
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_bindir/*

%changelog
* Mon Jul 13 2020 Michael Shigorin <mike@altlinux.org> 0.3.3-alt1
- initial build for ALT Sisyphus (thx rosa)

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.3.3-2
+ Revision: 0c968fa
- MassBuild#464: Increase release tag


