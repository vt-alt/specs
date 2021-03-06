Name: pyclewn
Version: 2.3
Release: alt2

Summary: Using vim as a front end to a debugger (supports gdb and pdb)
License: GPLv2
Group: Development/Debuggers
BuildArch: noarch

Source: %name-%version.tar.gz
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3 rpm-build-vim
BuildRequires: vim-console

%add_python3_req_skip msvcrt win32con win32console win32gui win32pipe


%description
Pyclewn allows using vim as a front end to a debugger. Pyclewn currently
supports gdb and pdb.

The debugger output is redirected to a vim window, the pyclewn console.
The debugger commands are mapped to vim user-defined commands with
a common letter prefix, and with completion available on the commands
and their first argument.

On unix when running gvim, the controlling terminal of the program to
debug is the terminal used to launch pyclewn. Any other terminal can be
used when the debugger allows it, for example after using the attach or
tty gdb commands or using the --tty option with pdb. On Windows, gdb
pops up a console attached to the program to debug.

%package -n python3-module-%name
Group: Development/Python3
Summary: Supplemental module for %name

%description -n python3-module-%name
Supplemental module for %name

%prep
%setup -n %name-%version
%patch0 -p2

# hack out " (ALT Linux)" from gdb version
sed -i 's@lines.next()@lines.next().replace(" (ALT Linux)","")@' lib/clewn/gdb.py
cat > %name <<@@@
#!/usr/bin/python3

import clewn.vim as vim
vim.main()
@@@

%build
export EDITOR=/usr/bin/vim
%python3_build

vim -S lib/clewn/runtime/pyclewn-%version.vmb +:q

%install
export EDITOR=/usr/bin/vim
%python3_install

mkdir -p %buildroot%vim_runtime_dir
cp -a $HOME/.vim/* %buildroot%vim_runtime_dir/
install -D %name %buildroot%_bindir/%name

%files
%doc README NEWS
%vim_runtime_dir/*/*
%vim_runtime_dir/*/.??*
%exclude %vim_runtime_dir/doc/tags
%_bindir/*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*


%changelog
* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.3-alt2
- Build for python2 disabled.

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3

* Wed Jan 13 2016 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2

* Tue Apr 21 2015 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1
- fix installation

* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 1.11-alt1
- Autobuild version bump to 1.11
- Adapt for ALT gdb version

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 1.10-alt1
- Autobuild version bump to 1.10
- Package is binary now

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1.9-alt1
- Autobuild version bump to 1.9

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Initial build from scratch

