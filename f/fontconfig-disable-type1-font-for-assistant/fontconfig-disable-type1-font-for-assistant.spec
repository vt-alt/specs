Name:     fontconfig-disable-type1-font-for-assistant
Version:  1.0
Release:  alt1

Summary:  Replace Type1 font Nimbus Sans L by Liberation Sans for Assistant
License:  GPLv3+
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: fontconfig
Requires: fonts-ttf-liberation 

BuildArch: noarch

%description
Replace Type1 font Nimbus Sans L by Liberation Sans for Assistant.

%prep

%install
mkdir -p %buildroot%_datadir/fontconfig/conf.avail
cat > %buildroot%_datadir/fontconfig/conf.avail/99-fonts-type1.conf << EOF.
<?xml version='1.0'?>
<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>
<fontconfig>
    <match target="pattern">
        <test name="family">
            <string>Nimbus Sans L</string>
        </test>
        <edit name="family" mode="assign" binding="same">
            <string>Liberation Sans</string>
        </edit>
    </match>
</fontconfig>
EOF.
mkdir -p %buildroot%_sysconfdir/fonts/conf.d
ln -s ../../../%_datadir/fontconfig/conf.avail/99-fonts-type1.conf %buildroot%_sysconfdir/fonts/conf.d/99-fonts-type1.conf

%files
%_sysconfdir/fonts/conf.d/99-fonts-type1.conf
%_datadir/fontconfig/conf.avail/99-fonts-type1.conf

%changelog
* Tue Nov 05 2019 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
