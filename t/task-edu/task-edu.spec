Name:    task-edu
Version: 1.4.3
Release: alt0.p9.1
License: GPL-3.0+
URL:     https;//www.altlinux.org/Education
Group:   Education

# Education (base part)
Requires: audacity
%ifarch %ix86 x86_64 aarch64
Requires: blender
%endif
Requires: bluefish
Requires: clamav
Requires: clamav-db
Requires: clamtk
Requires: codeblocks
Requires: codeblocks-contrib
Requires: dia
Requires: dosbox
Requires: fbreader
%ifnarch %e2k
Requires: goldendict
%else
Requires: stardict
%endif
Requires: dict-mueller7-utf8
Requires: gcc
Requires: inkscape
Requires: gimp
Requires: gimp-help-ru
Requires: gimp-plugin-gutenprint
Requires: gimp-plugin-refocus-it
Requires: java-devel
Requires: kdenlive
Requires: scribus
%ifnarch %e2k
Requires: shotwell
%endif
Requires: logisim
Requires: basic256
%ifarch %ix86 x86_64
Requires: freebasic
Requires: fpc
Requires: fpc-ide
%endif
Requires: geany
Requires: geany-themes
%ifnarch %e2k
Requires: geany-plugins
Requires: freeplane
%else
Requires: freemind
%endif
Requires: gnome-games-klotski
Requires: gnome-games-mahjongg
%ifnarch %e2k
Requires: gnome-games-aisleriot
%endif
Requires: xsane
Requires: xsane-gimp2
Requires: xsane-doc-ru
Requires: simple-scan
Requires: brasero
%ifnarch armh
Requires: imagination
%endif
Requires: connector
%ifarch %ix86 x86_64 aarch64
Requires: chromium
Requires: chromium-disable-webfonts
%endif
Requires: fonts-otf-mozilla-fira
%ifarch %ix86 x86_64 %e2k
Requires: veyon
%endif
Requires: itest
Requires: kumir2
# Big educational software
Requires: octave
%ifnarch ppc64le
Requires: wxMaxima
%endif
%ifarch %ix86 x86_64
Requires: lazarus
Requires: gambas-full
%endif
# OCR
Requires: gimagereader-qt5
Requires: tesseract
Requires: tesseract-langpack-ru
Requires: tesseract-langpack-en
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifnarch %e2k
Requires: kde5-khelpcenter
%endif
# Content filter and antivirus
Requires: netpolice-filter
Requires: netpolice-main
# For Skydns
%ifnarch %e2k
Requires: ddclient
%endif
Requires: perl-IO-Socket-SSL
# New utilites
Requires: autossh
Requires: inxi
Requires: screenfetch
Requires: ntpdate
Requires: fdisk
Requires: debhelper
Requires: keyutils
Requires: krb5-kinit
Requires: xdg-user-dirs-gtk
Requires: openresolv-bind
# GUI utilities
Requires: gparted
Requires: rosa-imagewriter
%ifnarch %e2k armh
Requires: grub-customizer
%endif
# Additional filesystem support
Requires: fuse-exfat
# Electronic board support
%ifarch %ix86 x86_64
Requires: starboard-preinstall
%endif
# Authenticate with Active Directory and FreeIPA by SSSD
Requires: task-auth-ad-sssd
Requires: task-auth-freeipa
Requires: sssd-ldap
Requires: pam_pkcs11
Requires: gvfs-shares
Requires: shared-desktop-icons
# Mass management and remote assistance
%ifnarch %e2k
Requires: puppet
%endif
%ifarch x86_64 aarch64
Requires: x11spice
%endif
Requires: openssh-server
Requires: python-module-yaml
Requires: python-module-jinja2
Requires: python-modules-json
# LibreOffice
%ifnarch %e2k
%define lo_name LibreOffice-still
%else
%define lo_name LibreOffice
%endif
Requires: %{lo_name}-extensions
Requires: %{lo_name}-integrated
Requires: %{lo_name}-gtk3
Requires: %{lo_name}-langpack-ru
Requires: libreoffice-languagetool
Requires: mythes-ru
Requires: hyphen-ru
Requires: gst-plugins-bad
Requires: gst-plugins-ugly
Requires: pentaho-reporting-flow-engine
Requires: perl-DBD-mysql
Requires: postgresql-jdbc
Requires: mysql-connector-java
# Alterator modules
Requires: alterator-notes
Requires: alterator-groups
Requires: alterator-logs
Requires: alterator-net-general
Requires: alterator-net-openvpn
Requires: alterator-net-wifi
Requires: alterator-sslkey
Requires: alterator-updates
# Communications
Requires: pidgin
Requires: pidgin-libnotify
# Other stuff
Requires: htop
Requires: apt-rsync
Requires: avplay
%ifarch %ix86 x86_64
Requires: bumblebee
%endif
Requires: cabextract
Requires: cheese
Requires: libsqlite
Requires: lm_sensors3-utils
Requires: man-pages-ru
Requires: mc-full
Requires: media-player-info
Requires: nano
Requires: quick-usb-formatter
Requires: rpm-build
Requires: sane
Requires: sane-frontends
Requires: setbranding
Requires: system-report
Requires: udev-rule-generator-cdrom
%ifarch %ix86 x86_64
Requires: virtualbox-guest-utils
Requires: xorg-dri-intel
%endif
Requires: xorg-drv-synaptics
Requires: xorg-conf-synaptics
Requires: zbar
Requires: audit
Requires: vixie-cron
# New stuff
Requires: xfce4-whiskermenu-plugin
Requires: menulibre
Requires: mugshot
Requires: xfce-polkit
# New utilites
Requires: disable-usb-autosuspend
Requires: color-prompt-and-man
Requires: shutter
Requires: screenkey
# Mozilla
Requires: thunderbird
# Search
Requires: recoll-full
# Append all modules from xscreensaver
Requires: desktop-screensaver-modules-xscreensaver
Requires: desktop-screensaver-modules-xscreensaver-gl
Requires: systemd-settings-enable-showstatus
Requires: systemd-settings-disable-dumpcore
Requires: systemd-settings-enable-log-to-tty12
# Helper to deploy system services
Requires: deploy
# Network
Requires: ipset
Requires: vlan-utils
# Group policy management
Requires: alterator-gpupdate
%ifnarch armh
Requires: adp
%endif
%ifarch %e2k
Requires: rtc
%endif
Summary(ru_RU.UTF-8): Базовый образовательный комплект
Summary: Educational software (base set)
%description
%{summary}.

%package preschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (дошкольное образование)
Summary: Educational software (preschool)
Group: Education
Requires: gcompris-qt
Requires: gcompris-qt-voices-ru
Requires: childsplay
Requires: childsplay-alphabet_sounds_ru
Requires: tuxpaint
Requires: kde5-khangman
Requires: kde5-kanagram
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifnarch %e2k
Requires: kde5-khelpcenter
%endif
%description preschool
%{summary}.

%package gradeschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (начальная школа)
Summary: Educational software (gradeschool)
Group: Education
Requires: task-edu
Requires: kde5-profile
Requires: kde5-kolourpaint
Requires: kde5-ktouch
Requires: gcompris-qt
Requires: gcompris-qt-voices-ru
Requires: trikStudio
Requires: trikStudio-data
Requires: kde5-kbruch
Requires: abiword
Requires: python3-tools
Requires: python3-module-pygame
Requires: python3-module-pygame-doc
Requires: python3-modules-curses
Requires: afce
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifarch %e2k
Requires: scratch
%endif
%ifarch %ix86 x86_64
Requires: scratch-desktop
%endif
%ifnarch %e2k
Requires: kde5-khelpcenter
Requires: trikStudioJunior
%endif
%description gradeschool
%{summary}.

%package highschool
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (cредняя школа)
Summary: Educational software (highschool)
Group: Education
Requires: task-edu
Requires: kumir2
Requires: codeblocks
Requires: kde5-profile
Requires: kde5-kolourpaint
%ifarch %ix86 x86_64
Requires: lazarus
Requires: openscad
Requires: scilab
%endif
%ifarch %ix86 x86_64 %e2k
Requires: synfigstudio
%endif
Requires: dia
Requires: trikStudio
Requires: kde5-marble
%ifnarch ppc64le
Requires: wxMaxima
%endif
Requires: bluefish
Requires: afce
# KDE5 localization and profile
Requires: kde5-profile
Requires: qt5-translations
%ifarch %e2k
Requires: scratch
%endif
%ifarch %ix86 x86_64
Requires: scratch-desktop
%endif
%ifnarch %e2k
Requires: qcad
Requires: kde5-khelpcenter
%endif
%ifarch %ix86 x86_64 aarch64 ppc64le
Requires: freecad
%endif
Requires: python-module-pip
Requires: python3-module-pip
%description highschool
%{summary}.

%package secondary-vocational
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (среднее профессиональное образование)
Summary: Educational software (secondary vocational)
Group: Education
Requires: codeblocks
%ifarch %ix86 x86_64
Requires: lazarus
%endif
%ifnarch %e2k armh
Requires: freecad
Requires: qcad
%endif
%ifnarch ppc64le
Requires: wxMaxima
%endif
Requires: octave
Requires: qt-creator
Requires: qt-creator-doc
Requires: cmake
Requires: ninja-build
Requires: qt5-base-devel
Requires: qt5-base-doc
#Requires: Eclipse
#Requires: Texmacs
Requires: logisim
Requires: fritzing
Requires: projectlibre
Requires: python3-tools
Requires: python3-module-pygame
Requires: python3-module-pygame-doc
Requires: python3-modules-curses
Requires: python-module-pip
Requires: python3-module-pip
%description secondary-vocational
%{summary}.

%package university
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (высшее образование)
Summary: Educational software (university)
Group: Education
Requires: codeblocks
Requires: qt-creator
Requires: qt-creator-doc
Requires: cmake
Requires: ninja-build
Requires: qt5-base-devel
Requires: qt5-base-doc
#Requires: Eclipse
%ifarch %ix86 x86_64
Requires: lazarus
Requires: gambas-full
Requires: monodevelop
Requires: openscad
%endif
Requires: swi-prolog
#Requires: Texmacs
%ifnarch ppc64le
Requires: wxMaxima
%endif
Requires: octave
%ifnarch %e2k
Requires: qcad
%endif
%ifnarch %e2k armh
Requires: freecad
Requires: qgis
Requires: qgis-grass
Requires: qgis-python
%endif
Requires: projectlibre
Requires: openmpi
Requires: fritzing
Requires: python3-tools
Requires: python3-module-pygame
Requires: python3-module-pygame-doc
Requires: python3-modules-curses
Requires: python-module-pip
Requires: python3-module-pip
%description university
%{summary}.

%package kde5
Summary(ru_RU.UTF-8): Среда KDE5 для Альт Образование
Summary: KDE5 for Alt Education
Group: Education
Requires: kde5
Requires: kf5-plasma-workspace
Requires: kde5-network-manager-nm
Requires: libqimageblitz5
Requires: kde5-krfb
Requires: kde5-edu
Requires: kde5-printing
Requires: kde5-scanning
Requires: kde5-connect
Requires: LibreOffice-still-kde5
Requires: nextcloud-client-kde5
Requires: branding-alt-education-kde-settings
%description kde5
%{summary}.

%package teacher
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (для учителей)
Summary: Software for teachers
Group: Education
%ifnarch armh
Requires: veyon
%endif
Requires: itest-server
Requires: ansible
%ifnarch %e2k armh
Requires: semaphore
%endif
Requires: virt-viewer
Requires: OpenBoard
Requires: touchegg
%description teacher
%{summary}.

%package server-apps
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (серверные приложения)
Summary: Server applications for education
Group: Education
%ifnarch %e2k
Requires: puppetserver
Requires: puppetdb
%endif
%ifnarch %e2k armh
Requires: semaphore
%endif
Requires: ansible
Requires: clamav
Requires: clamav-db
Requires: mariadb-server
Requires: mariadb-client
Requires: nano
Requires: apt-rsync
Requires: apt-repo
Requires: setbranding
Requires: htop
Requires: bash-completion
Requires: dansguardian
Requires: perl-DBD-mysql
#Requires: ejudge
Requires: openfire
Requires: alterator-datetime
Requires: alterator-console
Requires: apache2-httpd-worker
Requires: mariadb-server
Requires: installed-db-office-server-mediawiki
Requires: installed-db-office-server-nextcloud
Requires: installed-db-office-server-moodle
Requires: alterator-fbi
#Requires: alterator-bacula
Requires: alterator-ca
Requires: alterator-ddns
Requires: alterator-dhcp
Requires: alterator-firsttime
Requires: alterator-kdc
Requires: alterator-ldap-groups
Requires: alterator-ldap-users
Requires: alterator-mirror
Requires: alterator-net-domain
Requires: alt-domain-server
Requires: alterator-net-eth
Requires: alterator-net-pppoe
Requires: alterator-net-pptp
%ifarch %ix86 x86_64
Requires: alterator-netinst
%endif
Requires: alterator-net-openvpn
Requires: alterator-net-routing
Requires: alterator-net-bond
Requires: alterator-net-bridge
Requires: alterator-net-iptables
Requires: alterator-openldap
Requires: samba4
Requires: alterator-openvpn-server
Requires: alterator-squid
Requires: alterator-squidmill
Requires: alterator-quota
Requires: alterator-trust
Requires: anonftp
Requires: alterator-vsftpd
Requires: alterator-xinetd
Requires: alterator-postfix-dovecot
Requires: alterator-ulogd
Requires: xauth
Requires: xrdp
Requires: pulseaudio-module-xrdp
%ifarch %ix86 x86_64
Requires: docker-ce
Requires: lsb
%endif
Requires: tcpdump
%description server-apps
%{summary}.

%package video-conferencing
Summary(ru_RU.UTF-8): Образовательное программное обеспечение (сервер видеоконференций)
Summary: Video-conferencing server for education
Group: Education
Requires: prosody
Requires: jitsi-meet-doc
Requires: jitsi-meet-prosody
Requires: jitsi-meet-web
Requires: jitsi-meet-web-config
Requires: jitsi-videobridge
%ifarch x86_64
Requires: jicofo
%endif
%description video-conferencing
%{summary}.

%package school
Summary(ru_RU.UTF-8): Образовательное программное обеспечение для школ
Summary: Complete list of education software for schools
Group:   Education
Requires: task-edu
Requires: task-edu-gradeschool
Requires: task-edu-highschool
Requires: task-edu-teacher
%description school
%{summary}.

%files

%files preschool

%files gradeschool

%files highschool
 
%files secondary-vocational

%files university

%ifnarch %e2k
%files kde5
%endif

%files teacher

%files server-apps

%ifnarch %e2k
%files video-conferencing
%endif

%files school

%changelog
* Wed Apr 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt0.p9.1
- Backport new version to p9 branch.

* Wed Apr 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- Add touchegg to task-edu-teacher.

* Tue Apr 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt0.p9.1
- Backport new version to p9 branch.
- Return scilab and qgis.

* Tue Apr 27 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Add pulseaudio-module-xrdp, alterator-net-bond, alterator-net-bridge
  and alterator-net-iptables to task-edu-server-apps.

* Fri Apr 23 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt0.p9.1
- Add xsane-doc-ru.

* Fri Apr 23 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- Update for Sisyphus.
- Move from qgis to qgis3.
- Completely remove documentation for pip.
- Add xsane-doc-ru.
- Remove python3-modules-nis.

* Mon Apr 12 2021 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Replace italc3 to veyon.

* Sun Apr 11 2021 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Remove documentation for pip.

* Wed Apr 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Use java-devel instead of java-1.8.0-openjdk-devel.
- Add trikStudioJunior to task-edu-gradeschool.
- Add pip both for Python and Python3 for task-edu-highschool,
  task-edu-secondary-vocational and task-edu-university.

* Sat Apr 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Remove installer-feature* packages.

* Thu Apr 01 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt3
- Initial build for Sisyphus.
