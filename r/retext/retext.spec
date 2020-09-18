%def_without tests

Name:           retext
Version:        7.1.0
Release:        alt2
License:        GPLv3+
Summary:        Text editor for Markdown and reStructuredText
Summary(de):    Texteditor für Markdown und reStructuredText
Group:          Editors
URL: 		https://github.com/retext-project/retext

Source0:        %name-%version.tar
Source1:        %name.1

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): python3-devel python3-module-setuptools /dev/pts
BuildRequires:  python3-module-markups
BuildRequires:  python3-module-docutils
BuildRequires:  python3-module-enchant
BuildRequires:  python3-module-markdown
BuildRequires:  libpng-devel
BuildRequires:  librsvg-devel
BuildRequires:  librsvg-utils
BuildRequires:  ImageMagick-tools
BuildRequires:  qt5-tools-devel
BuildRequires:  python-module-PyQt5-devel

Requires: python3-module-Pygments

%if_with tests
BuildRequires:  libappstream-glib
%endif

%py3_requires docutils enchant markdown sip mdx_math
%add_python3_req_skip FakeVim PyQt5.QtWebEngineWidgets

%description
ReText is a simple but powerful text editor for Markdown and
reStructuredText.

%description -l de
ReText ist ein einfacher, aber leistungsfähiger Texteditor
für Markdown und reStructuredText.

%prep
%setup -q

%build
%python3_build_debug

%install
%python3_install

install -Dm 0644 %SOURCE1 %buildroot/%_man1dir/%name.1

# Generate resized icons
pushd icons
mkdir -p %buildroot/%_datadir/icons/hicolor/{16x16,22x22,24x24,32x32,48x48,64x64,72x72,96x96,128x128,scalable}/apps
for s in 16x16 22x22 24x24 32x32 48x48 64x64 72x72 96x96 128x128
do
    convert ./retext.png -resize $s %buildroot/%_datadir/icons/hicolor/$s/apps/retext.png
done
install -p -m 0644 retext.svg %buildroot/%_datadir/icons/hicolor/scalable/apps
popd

install -Dm 0644 data/*.desktop %buildroot%_desktopdir/%name.desktop

mv %buildroot%_datadir/{metainfo,appdata}

%find_lang retext --with-man

%check
%if_with tests
appstream-util validate-relax --nonet %buildroot%_datadir/appdata/*.appdata.xml ||:
python3 setup.py test
%endif

%files -f retext.lang
%doc changelog.md configuration.md README.md LICENSE_GPL
%_bindir/%name
%_datadir/appdata/*.appdata.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/%name/
%_man1dir/*.1*
%python3_sitelibdir/ReText/
%python3_sitelibdir/*egg-info

%changelog
* Tue Sep 15 2020 Andrey Cherepanov <cas@altlinux.org> 7.1.0-alt2
- Requires python3-module-Pygments.

* Sat Apr 04 2020 Andrey Cherepanov <cas@altlinux.org> 7.1.0-alt1
- New version.

* Mon Sep 24 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.4-alt1
- New version.

* Mon Jul 09 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt1
- New version.

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 10 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- new version 6.0.2

* Wed Jul 13 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- new version 6.0.1

* Tue May 17 2016 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 21 2016 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- Initial build in Sisyphus (based on Fedora spec)

