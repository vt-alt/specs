Name: engineering-meta
Version: p9
Release: alt2
Summary: Metapackage for install Engineering Applications
Summary(ru_RU.UTF-8): Метапакет для установки инженерных приложений
Group: Engineering
License: GPL-2.0-or-later
Url: https://altlinux.org/Engineering

ExcludeArch: armh ppc64le

Requires: engineering-2D-CAD = %EVR
Requires: engineering-3D-CAD = %EVR
Requires: engineering-3D-printing = %EVR
Requires: engineering-APCS = %EVR
Requires: engineering-CAM = %EVR
%ifarch %ix86 x86_64 aarch64
Requires: engineering-CNC = %EVR
%endif
Requires: engineering-EDA = %EVR
Requires: engineering-misc = %EVR

%description
Metapackage for install Engineering Applications.

%description -l ru_RU.UTF-8
Метапакет для установки инженерных приложений.

%package -n engineering-2D-CAD
Summary: Metapackage for install 2D CAD Applications
Summary(ru_RU.UTF-8): Мета-пакет для установки 2D САПР
Group: Engineering

Requires: librecad
Requires: qcad
Requires: qelectrotech
Requires: solvespace

%description -n engineering-2D-CAD
Metapackage for install 2D CAD (Computer Aided Design)
Applications.

%description -n engineering-2D-CAD -l ru_RU.UTF-8
Мета-пакет для установки 2D САПР
(систем автоматизированного проектирования).

%package -n engineering-3D-CAD
Summary: Metapackage for install 3D CAD Applications
Summary(ru_RU.UTF-8): Мета-пакет для установки 3D САПР
Group: Engineering

Requires: freecad
Requires: povray
%ifarch %ix86 x86_64 aarch64
Requires: openscad
Requires: openscad-MCAD
Requires: openscad-libraries-mcad
Requires: meshlab
%endif

%description -n engineering-3D-CAD
Metapackage for install 3D CAD (Computer Aided Design)
Applications.

%description -n engineering-3D-CAD -l ru_RU.UTF-8
Мета-пакет для установки 3D САПР
(систем автоматизированного проектирования).

%package -n engineering-3D-printing
Summary: Metapackage for install 3D Printing Applications
Summary(ru_RU.UTF-8): Метапакет для установки приложений 3D печати
Group: Engineering

Requires: cura
Requires: printrun
Requires: repraptor

%description -n engineering-3D-printing
Metapackage for install 3D Printing Applications.

%description -n engineering-3D-printing -l ru_RU.UTF-8
Метапакет для установки приложений 3D печати.

%package -n engineering-APCS
Summary: Metapackage for install APCS Applications
Summary(ru_RU.UTF-8): Метапакет для установки приложений АСУ ТП
Group: Engineering

# Open SCADA system
Requires: openscada-Model.AGLKS
Requires: openscada-Model.Boiler
Requires: openscada-docRU

# UniSet - library for building distributed industrial control systems
Requires: libuniset2-utils
Requires: libuniset2-extension-logicproc
Requires: libuniset2-extension-rrd
Requires: libuniset2-extension-sqlite
Requires: libomniORB-names
Requires: uniset2-testsuite
Requires: libuniset2-docs
Requires: uniset2-testsuite-doc

# Modbus network simulation
Requires: qmaster
Requires: qslave

# PLC (Programmable Logic Controller)
#Requires: beremiz # needed porting to python3
#Requires: yaplc-ide # needed fix with new beremiz

%description -n engineering-APCS
Metapackage for install APCS (Advanced Process Control Software)
Applications.

%description -n engineering-APCS -l ru_RU.UTF-8
Метапакет для установки приложений АСУ ТП
(автоматизированные системы управления технологическим процессом).

%package -n engineering-CAM
Summary: Metapackage for install CAM Applications
Summary(ru_RU.UTF-8): Метапакет для установки CAM приложений
Group: Engineering

%ifarch %ix86 x86_64
Requires: camotics
%endif
Requires: pycam
Requires: flatcam
Requires: pcb2gcodeGUI
#Requires: rastercarve # not allowed on p9

%description -n engineering-CAM
Metapackage for install CAM (Computer-aided manufacturing)
Applications.
Also install gcode-generators.

%description -n engineering-CAM -l ru_RU.UTF-8
Метапакет для установки CAM (системы автоматизации технологической
подготовки производства), а также генераторов gcode.

%package -n engineering-CNC
Summary: Metapackage for install CNC Applications
Summary(ru_RU.UTF-8): Metapackage for install CNC Applications
Group: Engineering

%ifarch %ix86 x86_64 aarch64
Requires: linuxcnc
Requires: mesaflash
%endif

%description -n engineering-CNC
Metapackage for install CNC (Computer Numerical Control)
Applications.

%description -n engineering-CNC -l ru_RU.UTF-8
Метапакет для установки ЧПУ (числовое программное управление)
станков и другого программного обеспечения с этим связанного.

%package -n engineering-EDA
Summary: Metapackage for install EDA Applications
Summary(ru_RU.UTF-8): Метапакет для установки САПР электронных устройств
Group: Engineering

Requires: kicad
Requires: ktechlab
Requires: qucs
Requires: qucs-s

%description -n engineering-EDA
Metapackage for install EDA (Electronic Design Automation)
Applications.

%description -n engineering-EDA -l ru_RU.UTF-8
Метапакет для установки программного обеспечения для автоматизации
проектирования электронных устройств.

%package -n engineering-misc
Summary: Metapackage for install engineering miscellaneous applications
Summary(ru_RU.UTF-8): Метапакет для установки некатегоризированного инженерного ПО
Group: Engineering

Requires: cu
Requires: cutecom

%description -n engineering-misc
Engineering applications not included in any category.

%description -n engineering-misc -l ru_RU.UTF-8
Метапакет для установки некатегоризированного инженерного ПО.

%files
%files -n engineering-2D-CAD
%files -n engineering-3D-CAD
%files -n engineering-3D-printing
%files -n engineering-APCS
%files -n engineering-CAM
%ifarch %ix86 x86_64 aarch64
%files -n engineering-CNC
%endif
%files -n engineering-EDA
%files -n engineering-misc

%changelog
* Sat Jul 03 2021 Anton Midyukov <antohami@altlinux.org> p9-alt2
- Add ktechlab to engineering-EDA
- Change License to GPL-2.0

* Mon Jun 28 2021 Anton Midyukov <antohami@altlinux.org> p9-alt1
- Initial build for p9
