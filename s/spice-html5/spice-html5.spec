%define _unpackaged_files_terminate_build 1

Name: spice-html5
Version: 0.3.0
Release: alt1
Summary: Pure Javascript SPICE client
Group: Networking/Remote access

License: LGPLv3
Url: http://www.spice-space.org
Source: %name/%name-%version.tar

BuildArch: noarch
# this path is used for symlinking into an actual project
Provides: %_datadir/spice-html5/src

%description
%name is a Javascript SPICE client.  This includes a simple HTML
page to initiate a session, and the client itself.  It includes a configuration
file for Apache, but should work with any web server.

%prep
%setup

%build

%install
%makeinstall_std

%files
%_datadir/%name
%doc COPYING COPYING.LESSER README TODO apache.conf.sample

%changelog
* Fri Dec 18 2020 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.2.2 -> 0.3.0.

* Fri Jun 05 2020 Stanislav Levin <slev@altlinux.org> 0.2.2-alt2
- Corrected spice-html5 path to provide.

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 0.2.2-alt1
- new version 0.2.2

* Wed Apr 17 2019 Stanislav Levin <slev@altlinux.org> 0.1.7-alt3.gitf9f700e
- Fixed Provides.

* Mon Nov 12 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt2.gitf9f700e
- Updated to a latest git snapshot for the FleetCommander.

* Sun Oct 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Mon Nov 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt2
- add patch for view Ctrl-Alt-Delete button

* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- Initial packaging

