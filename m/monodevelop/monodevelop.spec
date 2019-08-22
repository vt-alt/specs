%define _unpackaged_files_terminate_build 1

%def_disable tests

Name: monodevelop
Version: 7.6.9.22
Release: alt3

Summary: MonoDevelop is a project to port SharpDevelop to Gtk#
License: LGPLv2.1
Group: Development/Other
Url: https://www.monodevelop.com

ExclusiveArch: %ix86 x86_64

# https://github.com/mono/monodevelop.git
Source: %name-%version.tar
Source2: version.config

# Following data is obtained after running autogen, configure and make
Source3: buildinfo
Source4: nuget-core.tar
Source5: nuget-external-fsharpbinding.tar
Source6: nuget-home.tar
Source7: restored-targets-external.tar

# External dependencies (git submodules)
Source10: RefactoringEssentials-%version.tar
Source11: debugger-libs-%version.tar
Source12: guiunit-%version.tar
Source13: libgit-binary-%version.tar
Source14: libgit-binary-libgit2-%version.tar
Source15: libgit-binary-libssh2-%version.tar
Source16: libgit2-%version.tar
Source17: libgit2sharp-%version.tar
Source18: macdoc-%version.tar
Source19: mdtestharness-%version.tar
Source20: mono-addins-%version.tar
Source21: mono-tools-%version.tar
Source22: monomac-%version.tar
Source23: monomac-maccore-%version.tar
Source24: nrefactory-%version.tar
Source25: nuget-binary-%version.tar
Source26: sharpsvn-binary-%version.tar
Source27: xwt-%version.tar

Patch1: %name-fix-rpm-autoreq.patch
Patch2: %name-disable-nuget-and-git.patch
Patch3: %name-update-rpm-autoreq.patch

# https://github.com/mono/monodevelop/issues/6221
Patch4: %name-alt-fix-export-solution-issue.patch

Patch5: %name-alt-desktop-translation.patch

# monodis fails to process following files
%add_findprov_skiplist %_libexecdir/%name/AddIns/MonoDevelop.Refactoring/System.Text.Encoding.CodePages.dll
%add_findprov_skiplist %_libexecdir/%name/AddIns/MonoDevelop.UnitTesting/VsTestConsole/*
%add_findprov_skiplist %_libexecdir/%name/bin/System.IO.Compression.dll
%add_findprov_skiplist %_libexecdir/%name/bin/System.Runtime.InteropServices.RuntimeInformation.dll
%add_findprov_skiplist %_libexecdir/%name/bin/System.Text.Encoding.CodePages.dll

%add_findreq_skiplist  %_libexecdir/%name/AddIns/MonoDevelop.Refactoring/System.Text.Encoding.CodePages.dll
%add_findreq_skiplist  %_libexecdir/%name/AddIns/MonoDevelop.UnitTesting/VsTestConsole/*
%add_findreq_skiplist  %_libexecdir/%name/bin/System.IO.Compression.dll
%add_findreq_skiplist  %_libexecdir/%name/bin/System.Runtime.InteropServices.RuntimeInformation.dll
%add_findreq_skiplist  %_libexecdir/%name/bin/System.Text.Encoding.CodePages.dll

# Remove missing dependencies
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | \
	sed -e "/mono\(System\.Web\.DataVisualization\).*/d" \\\
	-e "/mono\(Microsoft\.VisualStudio\.ImageCatalog\).*/d" \\\
	-e "/mono\(PresentationCore\).*/d"'

BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-mono >= 2.0.0
BuildRequires: mono-devel-full msbuild
BuildRequires: intltool /usr/bin/msgfmt
BuildRequires: desktop-file-utils perl-XML-Parser shared-mime-info
BuildRequires: /usr/bin/7z
BuildRequires: /proc
BuildRequires: xsp
BuildRequires: autoconf automake cmake
BuildRequires: fsharp libgtk-sharp2-devel libgnome-sharp-devel
BuildRequires: libssh2-devel
BuildRequires: referenceassemblies-pcl

Requires: mono-core
Requires: mono-web
Requires: mono-devel-full
Requires: pkg-config
Requires: xsp
Requires: git
Requires: fsharp
Requires: referenceassemblies-pcl
Requires: msbuild

%description
This is MonoDevelop which is intended to be a full-featured
integrated development environment (IDE) for mono and Gtk#.
It was originally a port of SharpDevelop 0.98.

%prep
%setup

pushd external/RefactoringEssentials          ; tar xf %SOURCE10 --strip-components=1 ; popd
pushd external/debugger-libs                  ; tar xf %SOURCE11 --strip-components=1 ; popd
pushd external/guiunit                        ; tar xf %SOURCE12 --strip-components=1 ; popd
pushd external/libgit-binary                  ; tar xf %SOURCE13 --strip-components=1 ; popd
pushd external/libgit-binary/external/libgit2 ; tar xf %SOURCE14 --strip-components=1 ; popd
pushd external/libgit-binary/external/libssh2 ; tar xf %SOURCE15 --strip-components=1 ; popd
pushd external/libgit2                        ; tar xf %SOURCE16 --strip-components=1 ; popd
pushd external/libgit2sharp                   ; tar xf %SOURCE17 --strip-components=1 ; popd
pushd external/macdoc                         ; tar xf %SOURCE18 --strip-components=1 ; popd
pushd external/mdtestharness                  ; tar xf %SOURCE19 --strip-components=1 ; popd
pushd external/mono-addins                    ; tar xf %SOURCE20 --strip-components=1 ; popd
pushd external/mono-tools                     ; tar xf %SOURCE21 --strip-components=1 ; popd
pushd external/monomac                        ; tar xf %SOURCE22 --strip-components=1 ; popd
pushd external/monomac/maccore                ; tar xf %SOURCE23 --strip-components=1 ; popd
pushd external/nrefactory                     ; tar xf %SOURCE24 --strip-components=1 ; popd
pushd external/nuget-binary                   ; tar xf %SOURCE25 --strip-components=1 ; popd
pushd external/sharpsvn-binary                ; tar xf %SOURCE26 --strip-components=1 ; popd
pushd external/xwt                            ; tar xf %SOURCE27 --strip-components=1 ; popd

%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2

cp %SOURCE2 ./

# Prepare build info: add current date to prebuilt file
mkdir -p build/bin
cp %SOURCE3 ./build/bin/buildinfo
LANG=C date '+Build date: %%Y-%%m-%%d %%H:%%M:%%S%%:::z' >> ./build/bin/buildinfo

# unpack nuget packages
tar xf %SOURCE4
mkdir -p packages
pushd packages
for i in ../nuget-core/*.nupkg ; do
    name=$(basename ${i%%.nupkg})
    mkdir $name
    pushd $name
    7z x ../$i
    cp ../$i ./
    popd
done

# unzip unpacks filenames with %% sign as is. Convert it. TODO: make a more generic solution when necessary
find . -iname '*%%2B*' | while read file ; do
    mv $file $(echo $file | sed -e 's:%%2B:+:g') ||:
done
popd

tar xf %SOURCE5
mkdir -p external/fsharpbinding/packages
pushd external/fsharpbinding/packages
for i in ../../../nuget-external-fsharpbinding/*.version.txt ; do
    name=$(basename ${i%%.version.txt})
    namelower=$(echo $name | tr A-Z a-z)
    version=$(cat $i)
    dir=$(dirname $i)
    mkdir $name
    pushd $name
    # these nupkg file names are usually lowercase
    7z x ../$dir/${namelower}.${version}.nupkg
    cp ../$dir/${namelower}.${version}.nupkg ./${namelower}.${version}.nupkg
    popd
done

# unzip unpacks filenames with %% sign as is. Convert it. TODO: make a more generic solution when necessary
find . -iname '*%%2B*' | while read file ; do
    mv $file $(echo $file | sed -e 's:%%2B:+:g') ||:
done
popd

tar xf %SOURCE6
mkdir -p nuget/packages
pushd nuget/packages
for i in ../../nuget-home/*.version.txt ; do
    name=$(basename ${i%%.version.txt})
    dir=$(dirname $i)
    for version in $(cat $i) ; do
        mkdir -p $name/$version
        pushd $name/$version
        7z x ../../$dir/${name}.${version}.nupkg
        # copy additionally required files
        cp ../../$dir/${name}.${version}.nupkg ./
        cp ../../$dir/${name}.${version}.nupkg.sha512 ./
        # nuspec file names are usually lowercase
        for nuspec in ./*nuspec ; do
            mv $nuspec $(echo $nuspec | tr A-Z a-z)
        done
        popd
    done
done

# unzip unpacks filenames with %% sign as is. Convert it. TODO: make a more generic solution when necessary
find . -iname '*%%2B*' | while read file ; do
    mv $file $(echo $file | sed -e 's:%%2B:+:g') ||:
done
popd

tar xf %SOURCE7

find . -type f -print0 | xargs -0 \
    sed -i \
        -e 's:../version.config:version.config:g' \
        -e 's:..\\version.config:version.config:g' \
        -e "s:@NUGETDIR@:$(pwd)/nuget/packages:g" \
        -e "s:@RPMPROJECTDIR@:$(pwd):g"

%__subst '/^Encoding=/d;
	s/^Exec=monodevelop$/Exec=monodevelop %%F/;
	s/^Categories=.*$/Categories=Development;IDE;/
	' monodevelop.desktop
%__subst "s|^pkgconfigdir *= \$(prefix)/lib/pkgconfig|pkgconfigdir = %_pkgconfigdir|" \
	Makefile.am

# mono tries to do awk+sed and fails at it for some unknown reason. Workaround it.
cp src/core/MonoDevelop.Core/BuildVariables.cs.in src/core/MonoDevelop.Core/BuildVariables.cs
sed -i \
    -e "s:@PACKAGE_VERSION@:$(cat version.config | grep '^Version=' | sed -e 's|Version=||'):g" \
    -e "s:@PACKAGE_VERSION_LABEL@:$(cat version.config | grep '^Label=' | sed -e 's|Label=||'):g" \
    -e "s:@COMPAT_ADDIN_VERSION@:$(cat version.config | grep '^CompatVersion=' | sed -e 's|CompatVersion=||'):g" \
    -e "s:@BUILD_LANE@:$(cat version.config | grep '^BUILD_LANE=' | sed -e 's|BUILD_LANE=||'):g" \
    -e "s:@FULL_VERSION@:%version:g" \
    src/core/MonoDevelop.Core/BuildVariables.cs

%build
NOCONFIGURE=yes sh ./autogen.sh
%configure  \
	    --disable-update-mimedb --disable-update-desktopdb \
        --enable-subversion \
        --enable-git \
        --enable-monoextensions \
	    %{subst_enable tests}

%make

%install
%makeinstall_std

# Following plugin causes monodevelop to crash, remove it
rm -f %buildroot%_libexecdir/%name/bin/libe_sqlite3.so

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/*
%_libexecdir/%name
%_pkgconfigdir/*.pc
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%{name}*.png
%_iconsdir/hicolor/scalable/apps/%{name}*.svg
%_xdgmimedir/packages/*
%_datadir/appdata/%{name}.appdata.xml
%_man1dir/*

%changelog
* Tue Jun 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.9.22-alt3
- Added Russian translation to desktop file (Closes: #36849)

* Tue Oct 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.9.22-alt2
- Fixed work of solution format conversion.

* Tue Oct 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.6.9.22-alt1
- Updated to upstream version 7.6.9.22.

* Thu Jul 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.5.3.7-alt1
- Updated to upstream version 7.5.3.7.

* Wed Mar 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0.864-alt1
- Updated to stable upstream version 6.3.0.864.

* Wed Sep 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2.44-alt3
- Updated runtime dependencies.

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2.44-alt2
- Rebuilt with support of %%ubt macro.

* Fri Jul 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2.44-alt1
- Updated to stable upstream version 6.1.2.44

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 2.8.6.4-alt1
- 2.8.6.4

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- build with internal Cecil

* Thu Jun 17 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4

* Thu Mar 18 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2
- changed License

* Mon Oct 19 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt2
- update buildreq

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Fri Mar 13 2009 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2
- updated patches list

* Sun Feb 01 2009 Alexey Shabalin <shaba@altlinux.ru> 1.9.1-alt3.1
- rebuild with mono-2.2 (fix requires new cecil )

* Mon Jan 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt3
- fixed manual deps to be x86_64-friendly

* Sat Jan 03 2009 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt2
- desktop file fixes according to repocop results

* Sun Nov 23 2008 Ildar Mulyukov <ildar@altlinux.ru> 1.9.1-alt1
- 1.9.1
- manual rpm reqs for MonoDevelop.VersionControl.Subversion.dll
- new switch: %%def_(en|dis)able tests - disabled

* Fri Oct 31 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt1.r117558
- 2.0 alpha1, svn version 117558
- main package and core addins. extra addins move to package monodevelop-extra

* Tue Apr 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt2
- use gtksourceview2-sharp

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- 1.0

* Mon Feb 25 2008 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1
- 0.19
- revised patch3 (use system cecil)

* Wed Jan 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.18.1-alt1
- 0.18.1
- use system cecil (patch3)
- cleanup spec
- use gtksourceview1-sharp

* Wed Nov 28 2007 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt0.20071121
- 0.17
- use gtksourceview-2.0 and gtksourceview2-sharp
- disable build database support - fail build with gtksourceview2-sharp
- use firefox instead seamonkey
- add man page mdtool

* Tue Oct 09 2007 Alexey Shabalin <shaba@altlinux.ru> 0.16-alt1
- 0.16
- add seamonkey, libgnomeui to Requires (#13033)

* Sat Sep 08 2007 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15
- fix build for x86_64

* Sat Jul 28 2007 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- Update to 0.14
- source from svn (no full archive in download homepage)

* Sun Mar 25 2007 Ildar Mulyukov <ildar@altlinux.ru> 0.13.1-alt1
- 0.13.1
- new translation ru.po
- disable nemerle AddIn, it's not working right now

* Tue Dec 12 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.12-alt2
- added "enable-feature" switches

* Wed Sep 27 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.12-alt1
- BuildRequires fixes
- new features on

* Wed Jul 19 2006 Ildar Mulyukov <ildar@altlinux.ru> 0.11-alt1
- 0.11
- automatic dependancies calculation (due to rpm-4.0.4-alt66.1)

* Sun May 22 2005 Evgeny Sinelnikov <sin@altlinux.ru> 0.7-alt1
- Update to release

* Mon May 16 2005 Evgeny Sinelnikov <sin@altlinux.ru> 0.6-alt1
- Initial build for ALTLinux.
