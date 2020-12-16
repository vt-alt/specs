%define _unpackaged_files_terminate_build 1

%define realname gnome-sharp

Summary: GNOME bindings for Mono
Name: lib%{realname}
Version: 2.24.2
Release: alt6
License: LGPLv2+
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Source: http://ftp.gnome.org/pub/GNOME/sources/%realname/2.20/%realname-%version.tar.bz2
Patch11: %realname-2.20.0-fix-configs.patch
Patch12: %realname-%version-alt-build.patch

Url: http://www.mono-project.com/

BuildPreReq: glib2-devel >= 2.13.0
BuildPreReq: libgtk+2-devel >= 2.13.0
BuildPreReq: libgtk-sharp2-devel >= 2.12.2
BuildPreReq: libgtk-sharp2-gapi >= 2.12.2
BuildPreReq: libart_lgpl-devel >= 2.3.20
BuildPreReq: gnome-vfs-devel >= 2.22.0
BuildPreReq: libgnomecanvas-devel >= 2.20.0
BuildPreReq: libgnomeui-devel >= 2.23.0

BuildPreReq: rpm-build-mono
BuildRequires: /proc

BuildRequires: mono-core libSM-devel mono-devel >= 2.8

%description
Gnome# is a .NET language binding for assorted GNOME libraries.
This assembly has following configuration:
   Optional assemblies included in the build:
      * art-sharp.dll: yes
      * gnomevfs-sharp.dll: yes
      * gnome-sharp.dll: yes

%package devel
Summary: .Net language bindings for GNOME: development files
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the Gtk\# project
to parse and bind Gnome libraries.

%prep
%setup -n %realname-%version -q
%patch11 -p1
%patch12 -p2

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall

%files
%_bindir/gconfsharp2-schemagen
%_libdir/*.so
%prefix/lib/gtk-sharp-2.0/*
%_monodir/gac/*
%_monodir/gtk-sharp-2.0/*
%doc AUTHORS README ChangeLog

%files devel
%_datadir/gapi-2.0/*.xml
%_pkgconfigdir/*

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.24.2-alt6
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.24.2-alt5
- NMU: remove %ubt from release

* Mon Jul 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.24.2-alt4%ubt
- Rebuilt for additional architectures.

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.24.2-alt3%ubt
- Rebuilt with support of %%ubt macro.

* Tue Jul 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.24.2-alt2
- Rebuilt with mono-5

* Tue Nov 23 2010 Alexey Shabalin <shaba@altlinux.ru> 2.24.2-alt1
- 2.24.2
- build with mono-2.8

* Mon Jul 06 2009 Alexey Shabalin <shaba@altlinux.ru> 2.24.1-alt1
- 2.24.1
- move pkgconfig files from main to devel package

* Thu Oct 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Tue Aug 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- 2.20.1

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- 2.20.0

* Fri Dec 28 2007 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt6
- Fixed build with automake-1.10 

* Mon Nov 26 2007 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt5
- add --disable-static to configure
- rebuild with new rpm-build-mono-1.2
- move pkgconfig files from devel to main package

* Wed Sep 12 2007 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt4
- fix patch11

* Tue Sep 11 2007 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt3
- fix build wuth libgtkhtml-3.14 (patch10)
- add patch (patch11) from Debian - adding missing DDLs to generated configs

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt2
- add libSM-devel in BuildRequires

* Thu Nov 30 2006 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt1.1
- rebuild with fixed rpm-build-mono

* Tue Oct 10 2006 Ildar Mulyukov <ildar@altlinux.ru> 2.16.0-alt1
- 1st release for Sisyphus 
