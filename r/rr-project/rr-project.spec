Name:		rr-project
Version:	5.2.0
Release:	alt2
Summary:	Record and Replay Framework
Group:		Development/Debuggers
License:	AS
URL:		https://github.com/iovisor/bcc
Source:		%name-%version.tar
ExclusiveArch:	x86_64
Requires:	gdb

BuildRequires(pre): rpm-macros-cmake
BuildRequires:	ccache
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	capnproto-devel
BuildRequires:	python-module-pexpect
BuildRequires:	gdb
BuildRequires:	/proc

%description
rr is a lightweight tool for recording, replaying and debugging execution of
applications (trees of processes and threads). Debugging extends gdb with very
efficient reverse-execution, which in combination with standard gdb/x86
features like hardware data watchpoints, makes debugging much more fun.

%prep
%setup -q
subst "s!/bin/!/lib/rr/!" src/replay_syscall.cc
subst "s!/bin/rr_page_!lib/rr/rr_page_!" src/AddressSpace.cc

%build
%cmake -Ddisable32bit=ON
%cmake_build

%install
%cmake_install
mv %buildroot/%_bindir/rr_* %buildroot/usr/lib/rr/
subst '1s:/usr/bin/bash:/bin/bash:' %buildroot%_bindir/signal-rr-recording.sh

%files
%doc LICENSE README.md
%_bindir/rr
%_bindir/signal-rr-recording.sh
/usr/share/rr/
/usr/lib/rr

%changelog
* Wed May 26 2021 Arseny Maslennikov <arseny@altlinux.org> 5.2.0-alt2
- NMU: spec: adapt to new cmake macros.

* Thu Jun 14 2018 Vitaly Chikunov <vt@altlinux.ru> 5.2.0-alt1
- First build of rr for ALT.

