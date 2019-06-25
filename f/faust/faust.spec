Name: faust
Version: 0.9.90
Release: alt2.2

Summary: FAUST is a compiled language for real-time audio signal processing
License: GPLv2+
Group: Sound
Url: http://faust.grame.fr/

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
#Patch: %name-1.0-alt-makefile-fixes.patch

BuildRequires(pre): gcc-c++

%description
FAUST is a compiled language for real-time audio signal processing.

The name FAUST stands for Functional AUdio STream. Its programming model 
combines two approaches : functional programming and block diagram composition.
You can think of FAUST as a structured block diagram language with a textual syntax.

Programming with FAUST is somehow like working with electronic circuits
and signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram : a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters).

Faust is a compiled language translated to C++. In order to generate the most
efficient code, the compilation is based on a semantic approach. Instead of
compiling directly the block-diagram as described by the user, the idea is to
compile its mathematical meaning (what it actually computes). 


%package doc
Summary: Documentation for FAUST, a compiled language for real-time audio signal processing
Group: Sound
BuildArch: noarch
Requires: %name = %version-%release

%description doc
FAUST is a compiled language for real-time audio signal processing.

The name FAUST stands for Functional AUdio STream. Its programming model 
combines two approaches : functional programming and block diagram composition.
You can think of FAUST as a structured block diagram language with a textual syntax.

Programming with FAUST is somehow like working with electronic circuits
and signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram : a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters).

Faust is a compiled language translated to C++. In order to generate the most
efficient code, the compilation is based on a semantic approach. Instead of
compiling directly the block-diagram as described by the user, the idea is to
compile its mathematical meaning (what it actually computes). 

This package contains documentation for FAUST

%package examples
Summary: Examples for FAUST, a compiled language for real-time audio signal processing
Group: Sound
BuildArch: noarch
Requires: %name = %version-%release

%description examples
Examples for FAUST, a compiled language for real-time audio signal processing.


%package -n faust2appls
Summary: Useful scripts that combines faust and g++ to generates executable binary
Group: Sound
Requires: %name = %version-%release
BuildArch: noarch

%description -n faust2appls
FAUST is a compiled language for real-time audio signal processing.

The name FAUST stands for Functional AUdio STream. Its programming model 
combines two approaches : functional programming and block diagram composition.
You can think of FAUST as a structured block diagram language with a textual syntax.

Programming with FAUST is somehow like working with electronic circuits
and signals. A FAUST program is a list of definitions that defines a signal
processor block-diagram : a piece of code that produces output signals
according to its input signals (and maybe some user interface parameters).

Faust is a compiled language translated to C++. In order to generate the most
efficient code, the compilation is based on a semantic approach. Instead of
compiling directly the block-diagram as described by the user, the idea is to
compile its mathematical meaning (what it actually computes). 

This package contains some useful scripts for FAUST

%package devel
Summary: Development files for FAUST, a compiled language for real-time audio signal processing
Group: Development/C++
Requires: %name = %version-%release
BuildArch: noarch

%description devel
Development files for FAUST, a compiled language for real-time audio signal processing.

%prep
%setup
#patch -p1

%build
#configure
%make_build

%install
mkdir -p %buildroot/%_bindir/
%makeinstall install
%find_lang %name

mkdir -p %buildroot/%_docdir/%name-%version/
cp -ar README COPYING documentation/*.pdf %buildroot%_docdir/%name-%version/
mkdir -p %buildroot%_docdir/%name-%version/additional_documentation
install -pD -m0644 documentation/misc/*.pdf %buildroot%_docdir/%name-%version/additional_documentation
cp -ar examples/ %buildroot%_docdir/%name-%version/
install -pD -m0644 tools/README %buildroot%_docdir/%name-%version/README.tools

pushd tools/faust2appls
%makeinstall install
install -pD -m0644 README %buildroot%_docdir/%name-%version/README.faust2appls
popd

%files -f %name.lang
%dir %doc %_docdir/%name-%version/
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/COPYING
%_bindir/%name

%files doc
%doc %_docdir/%name-%version/*.pdf
%doc %_docdir/%name-%version/additional_documentation

%files examples
%doc %_docdir/%name-%version/examples

%files -n faust2appls
%_bindir/*
%exclude %_bindir/%name
%_docdir/%name-%version/README.faust2appls
%_docdir/%name-%version/README.tools

%files devel
%_includedir/%name
%_libexecdir/%name
%exclude %_libexecdir/%name/android
%exclude %_libexecdir/%name/iOS*

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.90-alt2.2
- rebuild with octave 5

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.90-alt1.2
- Rebuild with new Ruby autorequirements.

* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 0.9.90-alt1.1
- Rebuilt for aarch64

* Mon May 29 2017 Anton Midyukov <antohami@altlinux.org> 0.9.90-alt1
- New version 0.9.90

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.9.4-alt2.qa1
- NMU: rebuilt for debuginfo.

* Fri Jul 31 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt2
- minor gcc fixes

* Fri Jul 31 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt1
- package name fix

* Sun Apr 26 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt0.2
- appls and docs added

* Thu Apr 23 2009 Timur Batyrshin <erthad@altlinux.org> 0.9.9.4-alt0.1
- initial build
