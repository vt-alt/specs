%def_without doc

Name: keepass
Version: 2.43
Release: alt1

Summary: Password manager

Group: File tools
License: GPLv2+
URL: http://keepass.info/
ExclusiveArch: %ix86 x86_64

#source from: https://sourceforge.net/projects/keepass/files/KeePass 2.x/
Source0: %name-%version.tar
Source1: %name.appdata.xml

# Upstream does not include a .desktop file, etc..
Patch0: keepass-2.35-fedora-linux.patch

# Move XSL files to /usr/share/keepass:
Patch1: keepass-2.35-fedora-config.patch

# Locate locally-installed help files:
Patch2: keepass-2.35-fedora-doc.patch

# Automatically added by buildreq on Wed Mar 27 2019
# optimized out: fakeroot fontconfig fonts-bitmap-misc libX11-locales libgdk-pixbuf libwayland-client libwayland-server mono-core mono-data mono-data-oracle mono-data-sqlite mono-devel mono-dyndata mono-extras mono-locale-extras mono-monodoc mono-mvc mono-nunit mono-reactive mono-reactive-winforms mono-wcf mono-web mono-winforms mono-winfx python-base python-module-BeautifulSoup python-modules python-modules-compiler python-modules-email python-modules-encodings xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb
BuildRequires: ImageMagick-tools msbuild xvfb-run
BuildRequires: desktop-file-utils
%if_with doc
BuildRequires: archmage
BuildRequires: python-module-pychm
%endif
Requires: mono-winforms >= 5.0.0.0
Requires: xdotool
Requires: xsel

# The debuginfo package would be empty if created.
%global debug_package %nil

%description
KeePass is a free open source password manager, which helps you to
remember your passwords in a secure way. You can put all your passwords in
one database, which is locked with one master key or a key file.  You
only have to remember one single master password or select the key file
to unlock the whole database.

%package doc
Summary: Documentation for the KeePass password manager
Group: Documentation

BuildArch: noarch

%description doc
Documentation for KeePass, a free open source password manager.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Work around libpng bug (https://bugzilla.redhat.com/show_bug.cgi?id=1276843):
find -name \*.png -print0 | xargs -0 mogrify -define png:format=png32

%build
( cd Build && sh PrepMonoDev.sh )
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="5.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
msbuild /target:KeePass /property:Configuration=Release
for subdir in Images_App_HighRes Images_Client_16 Images_Client_HighRes; do
    xvfb-run -a mono Build/KeePass/Release/KeePass.exe -d:`pwd`/Ext/$subdir --makexspfile `pwd`/KeePass/Resources/Data/$subdir.bin
done
msbuild /target:KeePass /property:Configuration=Release
%if_with doc
%__python -c 'import archmod.CHM; archmod.CHM.CHMDir("Docs").process_templates("Docs/Chm")'
%endif

%install
install -d %buildroot/%prefix/lib/%name %buildroot/%_datadir/%name %buildroot/%_datadir/%name/XSL %buildroot/%_datadir/applications %buildroot/%_bindir %buildroot/%_datadir/mime/packages %buildroot/%_datadir/icons/hicolor/512x512/apps %buildroot/%_datadir/icons/hicolor/256x256/apps %buildroot/%_datadir/icons/hicolor/128x128/apps %buildroot/%_datadir/icons/hicolor/64x64/apps %buildroot/%_datadir/icons/hicolor/48x48/apps %buildroot/%_datadir/icons/hicolor/32x32/apps %buildroot/%_datadir/icons/hicolor/16x16/apps %buildroot/%_mandir/man1 %buildroot/%_docdir/%name %buildroot/%_datadir/metainfo
install -p -m 0644 Build/KeePass/Release/KeePass.exe Ext/KeePass.config.xml Ext/KeePass.exe.config %buildroot/%prefix/lib/%name
install -p -m 0644 Ext/XSL/KDBX_Common.xsl Ext/XSL/KDBX_DetailsFull_HTML.xsl Ext/XSL/KDBX_DetailsLight_HTML.xsl Ext/XSL/KDBX_PasswordsOnly_TXT.xsl Ext/XSL/KDBX_Tabular_HTML.xsl %buildroot/%_datadir/%name/XSL
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_512.png %buildroot/%_datadir/icons/hicolor/512x512/apps/%name.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_256.png %buildroot/%_datadir/icons/hicolor/256x256/apps/%name.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_128.png %buildroot/%_datadir/icons/hicolor/128x128/apps/%name.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_64.png %buildroot/%_datadir/icons/hicolor/64x64/apps/%name.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_48.png %buildroot/%_datadir/icons/hicolor/48x48/apps/%name.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_32.png %buildroot/%_datadir/icons/hicolor/32x32/apps/%name.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_16.png %buildroot/%_datadir/icons/hicolor/16x16/apps/%name.png
desktop-file-install --dir=%buildroot/%_datadir/applications dist/%name.desktop
install -p -m 0644 dist/%name.xml %buildroot/%_datadir/mime/packages
install -p -m 0644 dist/%name.1 %buildroot/%_mandir/man1
install -p -m 0644 %SOURCE1 %buildroot/%_datadir/metainfo
install -p dist/%name %buildroot/%_bindir
sed 's/\r$//' Docs/History.txt > %buildroot/%_docdir/%name/History.txt
sed 's/\r$//' Docs/License.txt > %buildroot/%_docdir/%name/License.txt
%if_with doc
cp -pr Docs/Chm %buildroot/%_docdir/%name/
%endif

%files
%dir %_docdir/%name
%doc %_docdir/%name/History.txt
%doc %_docdir/%name/License.txt
%_bindir/%name
%prefix/lib/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/mime/packages
%_datadir/icons/hicolor/512x512/apps/%name.png
%_datadir/icons/hicolor/256x256/apps/%name.png
%_datadir/icons/hicolor/128x128/apps/%name.png
%_datadir/icons/hicolor/64x64/apps/%name.png
%_datadir/icons/hicolor/48x48/apps/%name.png
%_datadir/icons/hicolor/32x32/apps/%name.png
%_datadir/icons/hicolor/16x16/apps/%name.png
%_mandir/man1/%name.1*
%_datadir/metainfo/%name.appdata.xml

%if_with doc
%files doc
%dir %_docdir/%name
%doc %_docdir/%name/Chm/
%endif

%changelog
* Mon Sep 16 2019 Oleg Solovyov <mcpain@altlinux.org> 2.43-alt1
- new version: 2.43

* Tue May 14 2019 Oleg Solovyov <mcpain@altlinux.org> 2.42.1-alt2
- require xsel

* Mon May 06 2019 Oleg Solovyov <mcpain@altlinux.org> 2.42.1-alt1
- new version: 2.42.1

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 2.41-alt2
- NMU: disable optional doc package build

* Tue Jan 15 2019 Oleg Solovyov <mcpain@altlinux.org> 2.41-alt1
- new version: 2.41

* Thu Sep 13 2018 Oleg Solovyov <mcpain@altlinux.org> 2.40-alt1
- new version: 2.40
- do not build for aarch64

* Wed May 30 2018 Oleg Solovyov <mcpain@altlinux.org> 2.39.1-alt1%ubt
- new version: 2.39.1

* Mon May 07 2018 Oleg Solovyov <mcpain@altlinux.org> 2.39-alt1%ubt
- new version: 2.39

* Thu Jan 11 2018 Oleg Solovyov <mcpain@altlinux.org> 2.38-alt1%ubt
- new version: 2.38

* Fri Dec 08 2017 Oleg Solovyov <mcpain@altlinux.org> 2.37-alt3%ubt
- add xdotool for auto-type feature

* Mon Nov 20 2017 Oleg Solovyov <mcpain@altlinux.org> 2.37-alt2%ubt
- move appdata -> metainfo

* Fri Oct 27 2017 Oleg Solovyov <mcpain@altlinux.org> 2.37-alt1%ubt
- new version: 2.37

* Tue Jul 25 2017 Oleg Solovyov <mcpain@altlinux.org> 2.36-alt2%ubt
- Build with mono 5

* Tue Jun 13 2017 Oleg Solovyov <mcpain@altlinux.org> 2.36-alt1%ubt
- new version: 2.36

* Thu Mar 09 2017 Oleg Solovyov <mcpain@altlinux.org> 2.35-alt1%ubt.1
- fixed requires

* Tue Mar 07 2017 Oleg Solovyov <mcpain@altlinux.org> 2.35-alt1%ubt
- added ubt tag for easy migrationing between branches

* Tue Feb 28 2017 Oleg Solovyov <mcpain@altlinux.org> 2.35-alt1
- ported from Fedora
