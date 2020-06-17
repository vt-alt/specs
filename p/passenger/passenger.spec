%define        pkgname passenger
%define        mod_name mod_%pkgname
%define        module_package_name apache2-mod_%pkgname

Name:          %pkgname
Version:       6.0.4
Release:       alt1
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers
Summary(ru_RU.UTF-8): Простой и ясный мост между приложениями на Рельсах и серверами Апач и Нгинкс
Group:         System/Servers
License:       MIT
Url:           https://github.com/phusion/passenger
Vcs:           https://github.com/phusion/passenger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       %name.load
Source2:       %name.conf
Source3:       %name.start
Source4:       locations.ini

BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-apache2
BuildRequires: %(eval echo %apache2_apr_buildreq)
BuildRequires: apache2-devel >= 2.2.5
BuildRequires: zlib-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: apache2-httpd-worker
BuildRequires: gcc-c++
BuildRequires: gem(rack)

%add_findreq_skiplist %ruby_gemslibdir/**/*
Requires(pre): apache2 >= %apache2_version-%apache2_release
Conflicts:     ruby1.8-passenger

%description
Phusion Passenger - a.k.a. mod_rails or mod_rack - makes deployment of
Ruby web applications, such as those built on the revolutionary Ruby on
Rails web framework, a breeze. It follows the usual Ruby on Rails
conventions, such as "Don't-Repeat-Yourself".
 * Deployment is only a matter of uploading application files.
   No Ruby (on Rails)-specific server configuration required!
 * Supports both the industry standard Apache web server and the fast
   and lightweight Nginx web server.
 * Allows Ruby on Rails applications to use about 33%% less memory, when
   used in combination with Ruby Enterprise Edition (optional).
 * Zero maintenance. No port management, server process monitoring or
   stale file cleanup required. Errors are automatically recovered
   whenever possible.
 * Designed for performance, stability and security. Phusion Passenger
   should never crash Apache even in case of crashing Rails applications
 * Well-documented, for both system administrators and developers!

%description -l ru_RU.UTF-8
Phusion Passenger™ известный как mod_rails или mod_rack


%package       -n %module_package_name

Summary:       Easy and robust deployment Ruby on Rails applications on Apache webserver
Summary(ru_RU.UTF-8): Простой и ясный мост между приложениями на Рельсах и сервером Апач
Group:         System/Servers
Requires:      apache2-httpd-worker passenger = %version
Provides:      %mod_name = %version

%description   -n %module_package_name
Documentation files for %module_package_name


%package       -n gem-%pkgname
Summary:       Library files for %gemname gem
Summary(ru_RU.UTF-8): Файлы библиотечные для самоцвета %gemname
Group:         Development/Ruby

%description   -n gem-%pkgname
Library files for %gemname gem.

%description   -n gem-%pkgname -l ru_RU.UTF8
Файлы библиотечные для самоцвета %gemname.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --pre=apache2

%install
%ruby_install
install -p -D -m 755 -- $(find -name passenger_native_support.so) %buildroot%ruby_gemextdir/passenger_native_support.so

#mod_passenger
install -p -D -m 755 -- buildout/apache2/%mod_name.so %buildroot%apache2_libexecdir/%mod_name.so
install -d -m 755 -- %buildroot%apache2_mods_available
install -d -m 755 -- %buildroot%apache2_mods_start
install -p -m 644 -- %SOURCE1 %buildroot%apache2_mods_available/%pkgname.load
install -p -m 644 -- %SOURCE2 %buildroot%apache2_mods_available/%pkgname.conf
install -p -m 644 -- %SOURCE3 %buildroot%apache2_mods_start/100-%pkgname.conf
install -p -D -m 644 -- %SOURCE4 %buildroot/%ruby_gemlibdir/locations.ini
sed 's,@a_libexecdir@,%apache2_libexecdir,g' \
    -i %buildroot%apache2_mods_available/%pkgname.load
sed -e 's,@passenger_path@,%ruby_gemlibdir/locations.ini,g' -e 's,@ruby_exec@,%__ruby,g' \
    -i %buildroot%apache2_mods_available/%pkgname.conf
sed -e 's,@rubylibdir@,%ruby_sitearchdir,g' \
    -e 's,@a_libexecdir@,%apache2_libexecdir,g' \
    -e 's,@bindir@,%_bindir,g' \
    -e 's,@libdir@,%_libdir,g' \
    -e 's,@datadir@,%_datadir,g' \
    -e 's,@name@,%name,g' \
    -i %buildroot%ruby_gemlibdir/locations.ini

%post -n %module_package_name
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%pkgname.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
	echo "Some errors detected in Apache2 configuration!"
	echo "To use %mod_name check configuration and start %apache2_dname service."
	echo
    fi
else
    echo "Apache2 %mod_name module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%pkgname=no' lines."
    echo
fi

%preun -n %module_package_name
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%pkgname.load ] && %apache2_sbindir/a2dismod %pkgname 2>&1 >/dev/null ||:
fi

%postun -n %module_package_name
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
	echo "Some errors detected in Apache2 configuration!"
	echo "To complete %mod_name uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi

%files
%doc README*
%_bindir/*
%_mandir/*

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n %module_package_name
%config(noreplace) %apache2_mods_available/%pkgname.conf
%config            %apache2_mods_available/%pkgname.load
%config            %apache2_mods_start/100-%pkgname.conf
%apache2_libexecdir/%mod_name.so

%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 6.0.4-alt1
- ^ 6.0.2 -> 6.0.4
- ! spec tags

* Fri Jun 28 2019 Pavel Skrylev <majioa@altlinux.org> 6.0.2-alt1
- > Ruby Policy 2.0
- ^ 4.0.60 -> 6.0.2

* Sun Jul 17 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.60-alt1
- Update to last 4.0.x release

* Wed Mar 19 2014 Led <led@altlinux.ru> 4.0.10-alt1.1
- Rebuilt with ruby-2.0.0-alt1

* Wed Aug 14 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.10-alt1
- Update to new 4.0.x release
- Rename library and data directories from phusion-passenger to passenger
- Install locations.ini for packaged directories to file:
  RUBY_SITEARCHDIR/phusion_passenger/locations.ini

* Tue Aug 13 2013 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.21-alt1
- Update to last 3.0.x release

* Thu Apr 18 2013 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.19-alt1
- Update to release

* Fri Nov 30 2012 Led <led@altlinux.ru> 3.0.17-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Aug 30 2012 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.17-alt1
- Update to release

* Sun Nov 27 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Update to release
- Start build with new scheme based on upstream git repository:
  https://github.com/FooBarWidget/passenger.git

* Sun Nov 27 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.9-alt3
- Build new release to Sisyphus with Python-2.7

* Fri Nov 18 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.9-alt2
- Add unowned packaged directories
- Fix passenger_native_support.so installation path
- Update spec-file for common way

* Fri Nov 18 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.9-alt1
- Update to release
- Add conflict to ruby1.8-passenger

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.5-alt1.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.5-alt1
- Update to release

* Fri Apr 15 2011 Malo Skryleve <malo@altlinux.org> 3.0.2-alt2
- Fixed some errors

* Sat Feb 26 2011 Malo Skryleve <malo@altlinux.org> 3.0.2-alt1
- initial build for ALT Linux Sisyphus

