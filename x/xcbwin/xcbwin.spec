Name:     xcbwin
Version:  0.3
Release:  alt1.gitd5f21cf

Summary:  Xcbwin - a simple C++ class for graphical outputs using XCB
License:  MIT
Group:    Development/Other
Url:      https://github.com/jofalk/Xcbwin

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

%description
Xcbwin is a lightweight class that provides rudimental and fast methods to
produce simple graphical outputs. The Xcbwin class is written for the
"Computational Physics" lecture given at the University of Wuerzburg (Germany).
Hence it is designed to be easy to use even by students, that are new to C++.

Currently the class provides methods to:
* Draw lines, circles, points, rectangles and text
* Plot functions
* Save screenshot of drawing
* Change the color
* Handle keyboard events

%package -n lib%name-devel
Summary: Xcbwin - a simple C++ class for graphical outputs using XCB
Group: Development/C++
Requires: libxcb-devel
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name-devel
Xcbwin is a lightweight class that provides rudimental and fast methods to
produce simple graphical outputs. The Xcbwin class is written for the
"Computational Physics" lecture given at the University of Wuerzburg (Germany).
Hence it is designed to be easy to use even by students, that are new to C++.

Currently the class provides methods to:
* Draw lines, circles, points, rectangles and text
* Plot functions
* Save screenshot of drawing
* Change the color
* Handle keyboard events

%prep
%setup
# Change path to xcbwin.h in examples
subst 's|../xcbwin.h|xcbwin.h|' demo/*.cpp

%install
install -Dpm 0644 xcbwin.h %buildroot%_includedir/xcbwin.h

%files -n lib%name-devel
%doc *.md demo
%_includedir/xcbwin.h

%changelog
* Sat Dec 26 2020 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1.gitd5f21cf
- Initial build for Sisyphus
