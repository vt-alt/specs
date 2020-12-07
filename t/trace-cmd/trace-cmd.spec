# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:     trace-cmd
Version:  2.9.1
Release:  alt5

Summary:  A front-end for Ftrace Linux kernel internal tracer
License:  GPL-2.0 and LGPL-2.1
Group:    Development/Debug
Url:      https://trace-cmd.org/
Vcs:      https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git
# List:   https://lore.kernel.org/linux-trace-devel/
# List:   https://lore.kernel.org/linux-trace-users/
# Bugs:   https://bugzilla.kernel.org/buglist.cgi?component=Trace-cmd%%2FKernelshark&product=Tools
#
# Poorly documented.
# Presentation: https://lwn.net/Articles/410200/ (2010)
# Article: http://wrightrocket.blogspot.com/2019/07/linux-performance-tool-trace-cmd.html

Source:   %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: asciidoc
BuildRequires: banner
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libfreeglut-devel
BuildRequires: libjson-c-devel
BuildRequires: libXi-devel
BuildRequires: libxml2-devel
BuildRequires: libXmu-devel
BuildRequires: polkit
BuildRequires: python-devel
BuildRequires: qt5-base-devel
BuildRequires: swig
BuildRequires: xmlto
%{?!_without_check:%{?!_disable_check:BuildRequires: CUnit-devel rpm-build-vm}}

%description
The trace-cmd(1) command interacts with the Ftrace tracer that is built inside
the Linux kernel. It interfaces with the Ftrace specific files found in the
debugfs file system under the tracing directory.

%package libs
Summary: trace-cmd libraries
Group: System/Libraries

%description libs
%summary.

%package devel
Summary: Development headers of trace-cmd-libs
Group: Development/C
Requires: %name-libs = %EVR

%description devel
%summary.

%package python3
Summary: Python plugin support for trace-cmd
Group: Development/Python3
Requires: %name = %EVR
Provides: python3(tracecmd)

%description python3
%summary.

%package -n kernelshark
Summary: Graphical reader for trace-cmd(1) output
Group: Development/Debug
Requires: trace-cmd = %EVR

%description -n kernelshark
KernelShark is a front end reader of trace-cmd(1) output. It reads a
trace-cmd.dat(5) formatted file and produces a graph and list view of
the data.

%prep
%setup
sed -i s/not-a-git-repo/%version-%release/ scripts/utils.mk
sed -i 's/import gtk/from gi.repository import Gtk as gtk/' python/*.py
sed -i 's/python2/python3/' python/event-viewer.py

%build
export CFLAGS="%optflags -D_FORTIFY_SOURCE=2 -fstack-protector-strong -fstack-check"
%make_build \
	all doc plugins
%make_build PYTHON_VERS=python3 python

# Following two cannot be built with make -j:
make libs
%{?!_without_check:%{?!_disable_check:make test}}

# Kernelshark shall have trace-cmd already built, or compilation will fail.
banner gui
%make_build \
	prefix=%_prefix \
	libdir=%_libdir \
	gui

%install
banner install
%makeinstall \
	etcdir=%buildroot%_sysconfdir \
	install install_doc install_libs
%makeinstall \
	PYTHON_VERS=python3 install_python
%makeinstall \
	prefix=%_prefix \
	libdir=%_libdir \
	DESTDIR=%buildroot/ \
	install_gui

# Misinstalled by install_gui.
rm -rf %buildroot/usr/etc %buildroot/usr/src/tmp

# error: value "1.1.0" for key "Version" in group "Desktop Entry" is not a known version
sed -i '/Version/d' %buildroot/%_datadir/applications/kernelshark.desktop

%check
desktop-file-validate %buildroot/%_datadir/applications/kernelshark.desktop

# Basic tests
%buildroot%_bindir/trace-cmd | grep version
%buildroot%_bindir/trace-cmd options

# Internal unit tests
export LD_LIBRARY_PATH=$PWD/lib/tracefs:$PWD/lib/traceevent:$PWD/lib/trace-cmd
vm-run --cpu=2 '
  set -xe
  utest/trace-utest
  PATH=%buildroot%_bindir:$PATH
  trace-cmd record -p function -l exit'*' true
  trace-cmd report'

%files
%doc COPYING COPYING.LIB DCO README
%_bindir/trace-cmd
%_sysconfdir/bash_completion.d/trace-cmd.bash
%_man1dir/*.1*
%_man5dir/*.5*

%files libs
%exclude %_libdir/trace-cmd/python
%_libdir/trace-cmd
%_libdir/traceevent
%_libdir/tracefs

%files devel
%_includedir/trace-cmd
%_includedir/traceevent
%_includedir/tracefs

%files python3
%doc Documentation/README.PythonPlugin
%_libdir/trace-cmd/python

%files -n kernelshark
%_bindir/kernelshark
%_bindir/kshark-record
%_bindir/kshark-su-record
%_libdir/kernelshark
%_datadir/applications/kernelshark.desktop
%_datadir/icons/kernelshark
%_datadir/polkit-1/actions/org.freedesktop.kshark-record.policy

%changelog
* Sun Dec 06 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt5
- Enable pkexec (RM#24461) in a way complatible with old cmake (for p9).

* Sat Dec 05 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt4
- Allow connect from pkexec'd process (RM#24461).

* Fri Dec 04 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt3
- Enable pkexec (RM#24461).

* Sun Sep 27 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt2
- Build kernelshark, libs, devel, and python3 packages.

* Thu Jul 23 2020 Vitaly Chikunov <vt@altlinux.org> 2.9.1-alt1
- Update to trace-cmd-v2.9.1 (2020-07-22).

* Mon Jul 20 2020 Vitaly Chikunov <vt@altlinux.org> 2.9-alt1
- Import of trace-cmd-v2.9 (2020-07-17).
- Add some testing into %%check section.

* Sat Sep 07 2019 Vitaly Chikunov <vt@altlinux.org> 2.8.3-alt1
- First build of trace-cmd. (Experimental).
