Name: ganttproject
Version: 2.7.2
Release: alt4

Summary: GanttProject is a tool for creating a project schedule by means of Gantt chart and resource load chart

License: GPLv2 with library exceptions
Group: Office
Url: http://www.ganttproject.biz/

Packager: Andrey Chetepanov <cas@altlinux.org> 

Source: %name-%version.tar
Source1: %name.desktop
Source2: %name.xml
Source3: %name.png

BuildArch: noarch

BuildRequires: rpm-build-java ant
BuildRequires: java-1.8.0-openjdk-devel

AutoProv: yes,noosgi

Requires: java >= 1.8.0

%description
GanttProject is a tool for creating a project schedule by means
of Gantt chart and resource load chart.
With GanttProject you can break down your project into a tree of tasks
and assign human resources that have to work on each task. You can also
establish dependencies between tasks, like "this task can't start
until this one is finished". GanttProject renders your project
using two charts: Gantt chart for tasks and resource load chart
for resources. You may print your charts, generate PDF and HTML
reports, exchange data with Microsoft(R) Project(TM)
and spreadsheet applications.

%prep
%setup
cd ganttproject-builder

%build

%install
cd ganttproject-builder
%ant -Dinstall.dir=%buildroot%_datadir/%name build

# Fix executable bit to program
chmod +x %buildroot%_datadir/%name/%name

# Make symlink to /usr/bin
install -d %buildroot%_bindir
ln -s %_datadir/%name/%name %buildroot%_bindir/%name 

# Create the desktop entry
install -Dm0755 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Create the mime-type for GanttProject
install -Dm0644 %SOURCE2 %buildroot%_datadir/mime/packages/%name.xml

# Copy the icon
install -Dm0644 %SOURCE3 %buildroot%_datadir/icons/hicolor/64x64/apps/%name.png

%files
%doc ganttproject/AUTHORS ganttproject/LICENSE ganttproject/README
%_bindir/%name
%_datadir/%name/
%_desktopdir/*.desktop
%_datadir/mime/packages/%name.xml
%_datadir/icons/hicolor/*/apps/%name.png

%changelog
* Mon Jun 08 2020 Andrey Cherepanov <cas@altlinux.org> 2.7.2-alt4
- Fix open *.gan files in ganttproject (ALT #38024).

* Fri Feb 21 2020 Andrey Cherepanov <cas@altlinux.org> 2.7.2-alt3
- Open *.gan files in ganttproject (ALT #38024).

* Mon Nov 07 2016 Andrey Cherepanov <cas@altlinux.org> 2.7.2-alt2
- Require java-1.8.0 and later (ALT #32710)

* Thu Jul 14 2016 Andrey Cherepanov <cas@altlinux.org> 2.7.2-alt1
- New version
- Build from upstream Git repository

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1 (with rpmrb script) (alt bug #30172)
- cleanup spec

* Fri Dec 23 2011 Michael Shigorin <mike@altlinux.org> 2.0.10-alt1
- 2.0.10
- ensure that the wrapper script is executable

* Tue Feb 08 2011 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt3
- Removed colombia calendar and es desc from spec

* Fri Sep 10 2010 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt2
- Building by nbr, checked

* Thu Sep 09 2010 Sergey Kurakin <kurakin@altlinux.org> 2.0.2-alt1
- Fixed trivial but fatal bug in wrapper
- Fixed repocop issue desktop-file-validate
- License corrected
- Url corrected
- Spec cleanup

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.2-alt0.2.qa1
- NMU (by repocop): the following fixes applied:
  * shared-mime-info for ganttproject
  * update_menus for ganttproject
  * postclean-05-filetriggers for spec file

* Sat Feb 24 2007 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt0.2
- Added full source, after discovery that sources are missing.
  Sources were in ganttproject.cvs.sourceforge.net repository

* Tue Dec 12 2006 Denis Medvedev <nbr@altlinux.ru> 2.0.2-alt0.1
- ALT packaging

* Mon Aug 21 2006 Juan Luis Baptiste <jbaptiste@merlinux.org> 2.0.2-2mer
- Added creation of %_libdir/menu/ganttproject file so menus work
  in PCLinuxOS.

* Fri Aug 11 2006 Juan Luis Baptiste <jbaptiste@merlinux.org> 2.0.2-1mer
- Updated to 2.0.2.

* Thu Aug 10 2006 Juan Luis Baptiste <jbaptiste@merlinux.org> 2.0.1-1mer
- Initial version.
- Added patch to include Holydays calendar of Colombia for year 2006.

