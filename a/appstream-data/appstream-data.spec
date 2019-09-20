%define _unpackaged_files_terminate_build 1

Name:      appstream-data
Summary:   ALT Linux AppStream metadata
Version:   20190919
Release:   alt1
Group:     System/Configuration/Packaging
BuildArch: noarch
License:   CC0 and CC-BY and CC-BY-SA and GFDL
URL:       http://www.altlinux.org/SoftwareCenter/Applications
Source:    %name-%version.tar
Source1:   manual-%version.tar

%description
This package provides the distribution specific AppStream metadata
required for ALT Linux Software Center.

%prep
%setup -a1

%install
mkdir -p %buildroot%_datadir/app-info/xmls
mkdir -p %buildroot%_datadir/app-info/icons

cp -r icons/* %buildroot%_datadir/app-info/icons/
cp -r xmls/* %buildroot%_datadir/app-info/xmls/
cp -r manual-%version/* %buildroot%_datadir/app-info/xmls/

%files
%_datadir/app-info/xmls/*
%_datadir/app-info/icons/altlinux

%changelog
* Thu Sep 19 2019 Andrey Cherepanov <cas@altlinux.org> 20190919-alt1
- Append package with Russian localization for LibreOffice and Firefox.

* Sun Sep 01 2019 Andrey Cherepanov <cas@altlinux.org> 20190901-alt1
- Fix for manual id of conflicted packages (firefox/firefox-esr, LibreOffice/LibreOffice-still) by <launchable> tag
- Add missing project_license tags
- Add apply plugin for screenshot fix
- Move screenshot text to <image> subtag (ALT #37143)
- Fix project license information (ALT #37038)

* Thu Jul 18 2019 Andrey Cherepanov <cas@altlinux.org> 20190718-alt2
- Remove MIME type desktop files.
- appstream-db: add -i parameter for use id instead of pkgname to search.

* Thu Jul 18 2019 Andrey Cherepanov <cas@altlinux.org> 20190718-alt1
- Add LibreOffice and LibreOffice-still.
- Fix gnome-games-aisleriot item.

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 20190715-alt1
- Add applications and popular fonts.

* Sun Jul 14 2019 Andrey Cherepanov <cas@altlinux.org> 20190714-alt1
- Add missing project_license to packages.
- appstream-db: add apply command for mass modification.

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 20190712-alt1
- Mass add applications from its desktop files.
- Fix update-list script.
- Remove old statistic files.

* Wed Jul 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20190702-alt1
- Updated appstream-data for Sisyphus.

* Wed Dec 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20181212-alt1
- Generated appstream-data for Sisyphus.

* Sun Mar 08 2015 Andrey Cherepanov <cas@altlinux.org> 20150308-alt1
- Initial build in Sisyphus
