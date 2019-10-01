%def_with tools
%define _unpackaged_files_terminate_build 1
%define mansuff xz
#set_compress_method none
%set_compress_method %mansuff
Name: girar-nmu
Version: 2.010.2
Release: alt1

Summary: girar client utilities for NMU automation
License: GPL-2.0-or-later
Group: Development/Other
Packager: Igor Vlasenko <viy@altlinux.org>
Url: http://www.altlinux.org/Git.alt/girar-nmu
#BuildArch: noarch

%if_with tools
Requires: girar-tools = %EVR
%endif

Source: %name-%version.tar

#BuildRequires: help2man
BuildRequires: m4
BuildRequires: perl-devel perl-podlators perl(RPM/Header.pm) perl-RPM-Source-Editor perl-RPM-Source-Convert perl(Pod/Usage.pm) perl(Date/Parse.pm) /usr/bin/pod2man perl-Gear-Rules perl(Source/Shared/Utils/GlobList.pm) perl(Source/Repository/RPM/ALTLinuxSrcList.pm) perl(Source/Shared/FindMirror/ALTLinux.pm)

Requires: gear
Requires: perl-RPM-Source-Editor >= 0.9233

%description
This package contains girar utilities for NMU automation.

%package -n  girar-tools
Summary: girar client tools for easy girar upload
Group: Development/Other
BuildArch: noarch
Conflicts: girar-nmu < 2

%description -n girar-tools
This package contains useful client utilities for girar and gitery
to guery upload methods, clone gits from tasks and gitery
and to help upload and manage tasks.

%prep
%setup
rm *.spec

%build
%make VERSION=%version
gcc -O2 %optflags -o girar-nmu-helper-pos-sort pos-sort.c

%install
%makeinstall_std

mkdir -p %buildroot%perl_vendor_privlib/RPM/Source/Transformation/
cp -a lib/RPM/Source/Transformation/* %buildroot%perl_vendor_privlib/RPM/Source/Transformation/

mkdir -p %buildroot%_sysconfdir/%name/
install -m 644 config/* %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_bindir/
install -m 755 girar-* rpm-sign-* srpmlschangelog %buildroot%_bindir/

for i in girar-* srpmlschangelog dist/girar-*; do
    name=`basename $i`
    pod2man  --name $name --center 'girar-nmu utils' --section 1 --release %version $i > $name.1 ||:
done
find . -name '*.1' -size 0 -print -delete
mkdir -p %buildroot%_man1dir
install -m 644 *.1 %buildroot%_man1dir/

while read link script; do
    ln -s $link %buildroot%_bindir/$script
    ln -s $link.1.%mansuff %buildroot%_man1dir/$script.1.%mansuff
done << 'EOF'
girar-task-add-git	girar-task-for-each-git
girar-task-add-git	girar-build-git
girar-task-add-srpm	girar-task-for-each-srpm
girar-task-add-srpm	girar-build-srpm
girar-task-add-rebuild girar-task-add-del
girar-task-add-rebuild girar-task-add-copy
girar-task-add-rebuild girar-task-for-each-rebuild
girar-task-add-rebuild girar-task-for-each-del
girar-task-add-rebuild girar-task-for-each-copy
girar-task-add-rebuild girar-build-rebuild
girar-task-add-rebuild girar-build-del
girar-task-add-rebuild girar-build-copy
EOF

%files
%doc README
%perl_vendor_privlib/RPM*
%_bindir/srpmlschangelog*
%_man1dir/srpmlschangelog*
%_bindir/girar-nmu-*
%_man1dir/girar-nmu-*

%if_with tools
%files -n girar-tools
%exclude %_bindir/girar-nmu-*
%exclude %_man1dir/girar-nmu-*
%endif

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/default
%config(noreplace) %_sysconfdir/%name/e2k
%_bindir/rpm-sign-*
%_bindir/girar-*
%_man1dir/girar-*

%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 2.010.2-alt1
- bugfix release

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 2.010.1-alt1
- added -Q (--no-output) to girar-get-upload-method

* Sat Apr 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.009-alt1
- bug fix for new --test-only

* Fri Apr 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.008-alt1
- bugfix release thanks to Denis Medvedev (nbr@)

* Thu Mar 21 2019 Igor Vlasenko <viy@altlinux.ru> 2.007-alt1
- updated man pages

* Wed Mar 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.006-alt1
- bugfix release for -e in sh scripts

* Tue Mar 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.005-alt1
- support for -m, set -e in sh scripts

* Mon Mar 18 2019 Igor Vlasenko <viy@altlinux.ru> 2.004-alt1
- support for --commit and --fail-early/late

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.003-alt1
- new version

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1
- new version
- if not configured, ssh aliases are detected from git config
- (closes: #35458)

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.001-alt1
- new version

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1
- release

* Wed Feb 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.999-alt1
- 2.0 beta 6

* Sat Jan 12 2019 Igor Vlasenko <viy@altlinux.ru> 1.998-alt1
- 2.0 beta 5

* Thu Dec 20 2018 Dmitry V. Levin <ldv@altlinux.org> 1.997-alt1.1
- Updated URL and license information.
- Fixed build with bash4.
- NMU.

* Wed Oct 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.997-alt1
- add girar-get-upload-method --missing mode

* Mon Sep 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.996-alt1
- added --commit-no-edit (-C) option to girar-build-git

* Tue Jul 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.995-alt1
- fixed --share bug

* Mon Jun 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.994-alt1
- 2.0 beta 4

* Sat Jun 23 2018 Igor Vlasenko <viy@altlinux.ru> 1.993-alt1
- 2.0 beta 3

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.992-alt1
- 2.0 beta 2

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.991-alt1
- 2.0 beta 1

* Wed Jun 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.990-alt1
- 2.0 alpha

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- e2k support (add -H git.e2k to use)

* Wed Apr 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- added -N for not signing already signed rpm

* Fri Mar 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- girar-nmu-helper-git-push-build: allow running not from
  the toplevel Git working dir (closes: #34595)

* Tue Feb 06 2018 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- added support for gpg agent forwarding thanks to slev@

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- new version

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1
- --test-only support

* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- basic support for rpmsign 4.13

* Sat Sep 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- use Source::Shared::Utils::GlobList

* Sun Apr 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- new version

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- support for gitery path in girar-nmu-helper-git-push-build

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1
- new version

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- new version

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- use new CLI

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- use new TransformContainer

* Mon Jan 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- use new R::S::E interface

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- use RPM::Header

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- updated BR:

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- rest of fixes for interface changes in R::S::E Transform 16

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- fixes for interface changes in R::S::E Transform 16

* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- more verbose debug for marked files

* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- added buildfrom-rpm-marked opt to girar-nmu-sort-transaction

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- added girar-nmu-helper-task-add-rebuild

* Sun Nov 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- <before_subtask_id> support in girar-nmu-helper-git-push-build

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- improved debug output in girar-nmu-sort-transaction

* Fri Nov 13 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.27-alt2
- girar-nmu-helper-clone-and-setup-build-commit: configure the remote
  in a standard way (like "git remote add" does; ALT#31482).
- minor tweaks in the code:
  - factored out git://git.altlinux.org/gears and
    git://git.altlinux.org/srpms as variables (to become environment
    parameters in future).
  - typo in documentation.

* Thu Oct 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- <before_subtask_id> support in girar-nmu-helper-task-add-srpm

* Tue Oct 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.26-alt1
- girar-nmu-helper-task-add-git: fixed typo.

* Sat Aug 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- support for girar and gitery

* Sun Dec 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- new version

* Thu Dec 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- new version

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- new version

* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- new version

* Wed Nov 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- bugfix release

* Sun Oct 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- bugfix release thanks to glebfm@ (closes: #30371)

* Fri Sep 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- new version

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- use Gear::Rules library

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- new version
