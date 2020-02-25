Name:       BALL
Version:    1.4.3_beta1.793.git37fc53c
Release:    alt3

Summary:    Biochemical Algorithms Library
License:    LGPL, GPL
Group:      Sciences/Chemistry

Url:        http://www.ball-project.org
Source:     %name-%version.tar
Source1:    ball.desktop

Patch1: BALL-alt-link-glew.patch

Packager:   Grigory Ustinov <grenka@altlinux.org>

BuildRequires: boost-asio-devel cmake doxygen eigen3 flex ghostscript-utils
BuildRequires: glibc-devel-static graphviz libGLEW-devel liblpsolve-devel
BuildRequires: libsvm-devel python-module-sip-devel python3-dev qt5-tools-devel
BuildRequires: qt5-webengine-devel tbb-devel

ExclusiveArch: %ix86 x86_64

%add_python_req_skip BALL BALLCore VIEW

%description
BALL (Biochemical Algorithms Library) is an application framework
in C++ that has been specifically designed for rapid software
development in Molecular Modeling and Computational Molecular Biology.
It provides an extensive set of data structures as well as classes
for Molecular Mechanics, advanced solvation methods, comparison and
analysis of protein structures, file import/export, and visualization.
BALL is currently being developed in the groups of Oliver Kohlbacher
(University of Tuebingen, Germany), Andreas Hildebrandt (Saarland
University, Saarbruecken, Germany), and Hans-Peter Lenhof (Saarland
University, Saarbruecken, Germany).

%package devel
Group: Sciences/Chemistry
Summary: Header files for %name

%description devel
Header files for %name

%prep
%setup
%patch1 -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

# BALLView needs these system variables
mkdir -p %buildroot%_sysconfdir/profile.d
cat > %buildroot%_sysconfdir/profile.d/ball.sh <<@@@
export BALLVIEW_DATA_PATH=/usr/share/BALL/
export BALL_DATA_PATH=/usr/share/BALL/
@@@
chmod +x %buildroot%_sysconfdir/profile.d/ball.sh

# install desktop file
mkdir -p %buildroot%_datadir/applications
cp -vf %SOURCE1 %buildroot%_datadir/applications/

%files
%_bindir/*
%_datadir/%name
%_libdir/*so.1.5
%exclude %_libdir/lib*.so
%_sysconfdir/profile.d/ball.sh
%_datadir/applications/ball.desktop

%files devel
%_docdir/*
%_includedir/%name
%_libdir/*.so
%_libdir/cmake/BALL/*.cmake

%changelog
* Mon Nov 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.3_beta1.793.git37fc53c-alt3
- Fixed linking error.

* Thu Feb 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.3_beta1.793.git37fc53c-alt2
- Fixed FTBFS.

* Fri Sep 21 2018 Grigory Ustinov <grenka@altlinux.org> 1.4.3_beta1.793.git37fc53c-alt1
- Initial build for Sisyphus (Closes: #21629).
