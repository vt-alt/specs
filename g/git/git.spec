Name: git
Version: 2.24.1
Release: alt1

Summary: Git core and tools
License: GPLv2
Group: Development/Other
Url: https://git-scm.com/

# git://git.altlinux.org/gears/g/git.git
Source: %name-%version-%release.tar

%def_enable curl
%def_enable expat
%def_with arch
%def_with cvs
%def_with email
%def_with tk
%def_with gui
%def_with doc
%def_with gitweb
%def_without python
%def_with svn

# List of architectures worthy of running the test suite.
%define check_arches x86_64 %ix86
%ifarch %check_arches
%def_with check
%else
%def_without check
%endif

%define _libexecdir /usr/libexec
%define gitexecdir %_libexecdir/git-core
%define pkgdocdir %_docdir/%name

Requires: %name-core = %EVR, perl-Git = %EVR

BuildRequires: hardlink, libssl-devel, perl-devel, perl-podlators, perl(Error.pm), zlib-devel >= 0:1.2
%{!?_without_python:BuildRequires: python-modules-encodings >= 0:2.4}
%{!?_without_cvs:BuildRequires: cvs perl(DBI.pm)}
%{!?_disable_curl:BuildRequires: libcurl-devel}
%{!?_disable_expat:BuildRequires: libexpat-devel}
%{!?_without_email:BuildRequires: perl(Mail/Address.pm) perl(Net/SMTP/SSL.pm) perl(Term/ReadLine.pm)}
%{!?_without_svn:BuildRequires: perl(Encode.pm) perl(Memoize.pm) perl(SVN/Core.pm) perl(Term/ReadKey.pm) perl(YAML/Any.pm) subversion subversion-server-common}
%{!?_without_doc:BuildRequires: asciidoc > 0:6.0.3, xmlto}
%{?!_without_gitweb:BuildRequires: perl(charnames.pm) perl(CGI.pm) perl(Encode.pm)}
%{?!_without_check:%{?!_disable_check:BuildRequires: cvsps gnupg perl(HTTP/Date.pm) perl(Term/ANSIColor.pm) perl(DBD/SQLite.pm) perl(Encode/JP.pm) unzip}}

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

%package core
Summary: Git core tools
Group: Development/Other
Requires: diffstat less openssh-clients rsync
# due to git commit --fast.
Provides: git-commit-fast

%description core
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains core set of Git tools with minimal dependencies.

%package server
Summary: Simple TCP git server for git repositories
Group: System/Servers
Requires: %name-core = %EVR

%description server
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains git server that normally listens on TCP port 9418.
It waits for a connection, and will just execute "git-upload-pack"
when it gets one.  It is ideally suited for read-only updates, i.e.,
pulling from git repositories.

%package arch
Summary: Git tools for importing Arch repositories
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR, tla

%description arch
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Git tools for importing Arch repositories.

%package cvs
Summary: Git tools for importing CVS repositories
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR, perl-Git = %EVR, cvs, cvsps

%description cvs
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Git tools for importing CVS repositories.

%package -n perl-Git
Summary: Perl interface to Git
Group: Development/Perl
BuildArch: noarch
Requires: %name-core = %EVR

%description -n perl-Git
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Perl interface to Git.

%package email
Summary: Git tools for sending email
Group: Development/Other
BuildArch: noarch
Requires: perl-Git = %EVR
# Workaround for ALT#23407.
Requires: perl(MIME/Base64.pm) perl(Authen/SASL.pm)

%description email
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Git tools for sending email.

%package svn
Summary: Git tools for importing Subversion repositories
Group: Development/Other
Requires: %name-core = %EVR, perl-Git = %EVR, subversion

%description svn
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Git tools for importing Subversion repositories.

%package -n gitk
Summary: Git revision tree visualiser ('gitk')
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR, tk >= 8.4

%description -n gitk
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Git revision tree visualiser ('gitk').

%package gui
Summary: Git GUI tool
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR, tk >= 8.4

%description gui
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Git GUI tool.

%package -n gitweb
Summary: Git web interface
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR
Requires: perl(charnames.pm)

%description -n gitweb
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains simple web interface to track changes in Git
repositories.

%package -n libgit-devel
Summary: Git develpoment library and header files
Group: Development/C

%description -n libgit-devel
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains libgit.a develpoment library and accompanying
header files.

%package doc
Summary: Git documentation
Group: Development/Documentation
BuildArch: noarch
Provides: %name-docs = %EVR
Obsoletes: %name-docs

%description doc
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains the Git documentation in text and HTML formats.

%package contrib
Summary: Git contrib files
Group: Development/Other
BuildArch: noarch
AutoReq: no
Requires: %name-core = %EVR

%description contrib
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains Git contributed software.

%package diff-highlight
Summary: Utility that highlights changes in diffs
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR

%description diff-highlight
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains diff-highlight utility, which is a part of Git
contributed software.

%package subtree
Summary: Merge subtrees together and split repository into subtrees
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR

%description subtree
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains git-subtree utility which is a part of Git
contributed software.

%package full
Summary: Git core and tools
Group: Development/Other
BuildArch: noarch
Requires: %name-core = %EVR, perl-Git = %EVR, %name-server = %EVR
%{!?_without_arch:Requires: %name-arch = %EVR}
%{!?_without_cvs:Requires: %name-cvs = %EVR}
%{!?_without_email:Requires: %name-email = %EVR}
%{!?_without_svn:Requires: %name-svn = %EVR}
%{!?_without_tk:Requires: gitk = %EVR}
%{!?_without_gui:Requires: %name-gui = %EVR}
%{!?_without_doc:Requires: %name-doc = %EVR}
%{!?_without_gitweb:Requires: gitweb = %EVR}

%description full
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.

This package contains the full set of Git tools.

%prep
%setup -n %name-%version-%release
rm -r perl/Git/LoadCPAN*
cat >config.mak <<'EOF'
V = 1
CFLAGS = %optflags
NO_GETTEXT = 1
GNU_ROFF = 1
ETC_GITCONFIG = /etc/gitconfig
prefix = %_prefix
libdir = %_libdir
mandir = %_mandir
htmldir = %pkgdocdir
NO_PERL_CPAN_FALLBACKS = 1
%{?_disable_curl:NO_CURL = 1}
%{?_disable_expat:NO_EXPAT = 1}
%{?_without_python:NO_PYTHON = 1}
%{?_without_python:SCRIPT_PYTHON_INS = }
EOF

%build
touch git-gui/credits
%make_build -C Documentation doc.dep
%make_build all %{!?_without_doc:man html}
%make_build -C contrib/diff-highlight
%make_build -C contrib/subtree all %{!?_without_doc:doc}

%check
%{?_without_email:rm t/t9001-send-email.sh}
%make_build -k test

%install
%makeinstall_std \
	install-lib \
	%{!?_without_doc:install-man install-html}
%makeinstall_std %{!?_without_doc:install-doc} -C contrib/subtree

mkdir -p %buildroot%_includedir/git
find -name \*.d -print0 |
	xargs -0 sed -n 's/^\([^:[:space:]]*\.h\)[[:space:]]*:.*/\1/p' -- |
	sort -u |
	xargs realpath -e --relative-to=. -- |
	sort -u > headers.list
tr / '\n' < headers.list |
	grep -Fv .h |
	sort -u |
	xargs -i ln -s . %buildroot%_includedir/git/'{}'
xargs install -pm644 -t %buildroot%_includedir/git -- < headers.list

chmod a-x %buildroot%gitexecdir/git-sh-setup
install -pDm644 contrib/completion/git-completion.bash \
	%buildroot%_datadir/bash-completion/completions/git
# Generate shell functions provides list.
(
	echo '# shell functions provides list'
	sed -n 's/^\([A-Za-z][A-Za-z_0-9]*\)[[:space:]]*().*/\1/pg' \
		%buildroot%gitexecdir/git-sh-setup |
		LC_COLLATE=C sort -u
) > %buildroot%gitexecdir/.provides.sh

# git-server.
mkdir -p %buildroot%_sbindir
mv %buildroot%gitexecdir/git-daemon %buildroot%_sbindir/
install -pD -m640 git.xinetd \
	%buildroot%_sysconfdir/xinetd.d/git

# Fix manpages.
find %buildroot%_mandir -type f -print0 |
	xargs -r0 grep -lZ '^.\+\.sp$' -- |
	xargs -r0 sed -i 's/^\(.\+\)\(\.sp\)$/\1\n\2/' --

find %buildroot%_datadir/git-core/ -name '*watchman*' -delete -print

# Install docs and contrib.
mkdir -p %buildroot%pkgdocdir/
install -pm644 Documentation/SubmittingPatches %buildroot%pkgdocdir/
install -Dm755 contrib/diff-highlight/diff-highlight %buildroot%_bindir
cp -a contrib %buildroot%_datadir/git-core/
rm -r %buildroot%_datadir/git-core/contrib/completion
rm -r %buildroot%_datadir/git-core/contrib/emacs
rm -r %buildroot%_datadir/git-core/contrib/examples
rm -r %buildroot%_datadir/git-core/contrib/diff-highlight
rm -r %buildroot%_datadir/git-core/contrib/subtree

# Remove unpackaged files.
%{?_without_arch:rm %buildroot%gitexecdir/git-archimport}
%{?_without_email:rm %buildroot%gitexecdir/git-*email*}
%{?_without_svn:rm %buildroot%gitexecdir/git-*svn*}

# Relocate hooks, convert template hooks to symlinks.
pushd %buildroot%_datadir/git-core/templates/hooks
	mkdir ../../hooks
	for f in *.sample; do
		mv $f ../../hooks/${f%%.sample}
		ln -s %_datadir/git-core/hooks/${f%%.sample} $f
	done
popd

# Avoid compressing templates.
%set_compress_topdir %_mandir

# Hardlink identical files together.
%define __spec_install_custom_post  hardlink -vc %buildroot

%pre server
/usr/sbin/groupadd -r -f _gitd
/usr/sbin/useradd -r -g _gitd -d /dev/null -s /dev/null -c 'The git server' -n _gitd >/dev/null 2>&1 ||:

%files

%files full

%files core
%_datadir/bash-completion/completions/git
%_bindir/*
%exclude %_bindir/git-cvs*
%gitexecdir/
%exclude %gitexecdir/git-cvs*
%exclude %gitexecdir/git-gui*
%exclude %gitexecdir/git-citool
%exclude %gitexecdir/git-add--interactive
%exclude %gitexecdir/git-subtree
%exclude %_bindir/gitk
%exclude %_bindir/diff-highlight
%exclude %_bindir/diff-highlight
%{!?_without_arch:%exclude %gitexecdir/git-archimport}
%{!?_without_email:%exclude %gitexecdir/git-*email*}
%{!?_without_svn:%exclude %gitexecdir/*svn*}
%_datadir/git-core/
%exclude %_datadir/git-core/contrib/
%if_with doc
%_mandir/man?/*
%exclude %_man1dir/git-subtree.*
%exclude %_man1dir/git-daemon.*
%exclude %_man1dir/git-svn*.1*
%exclude %_man1dir/git-cvs*.1*
%exclude %_man1dir/git-archimport.1*
%exclude %_man1dir/git-*email*.1*
%exclude %_man1dir/gitk*.1*
%exclude %_man3dir/Git.3*
%exclude %_mandir/man?/gitweb.*
%endif #doc

%files server
%_sbindir/git-daemon
%if_with doc
%_man1dir/git-daemon.*
%endif #doc
%attr(640,root,wheel) %config(noreplace) %_sysconfdir/xinetd.d/git

%if_with arch
%files arch
%gitexecdir/git-archimport
%if_with doc
%_man1dir/git-archimport.1*
%endif #doc
%endif #arch

%if_with cvs
%files cvs
%_bindir/*cvs*
%gitexecdir/*cvs*
%if_with doc
%_man1dir/git-cvs*.1*
%endif #doc
%endif #cvs

%files -n perl-Git
%gitexecdir/git-add--interactive
%if_with doc
%_man3dir/Git.3*
%endif
%perl_vendor_privlib/Git/
%perl_vendor_privlib/Git.pm
%exclude %perl_vendor_privlib/Git/SVN*

%if_with email
%files email
%gitexecdir/*email*
%if_with doc
%_man1dir/git-*email*.1*
%endif #doc
%endif #email

%if_with svn
%files svn
%gitexecdir/*svn*
%if_with doc
%_man1dir/git-svn*.1*
%endif #doc
%perl_vendor_privlib/Git/SVN*
%endif #svn

%if_with tk
%files -n gitk
%_bindir/gitk
%_datadir/gitk/
%if_with doc
%_man1dir/gitk.1*
%endif #doc
%endif #tk

%if_with gui
%files gui
%gitexecdir/git-gui*
%gitexecdir/git-citool
%_datadir/git-gui/
%if_with doc
# Not Yet...
# %_man1dir/git-gui.1*
# %_man1dir/git-citool.1*
%endif #doc
%endif #gui

%if_with gitweb
%files -n gitweb
%_datadir/gitweb/
%if_with doc
%_mandir/man?/gitweb.*
%endif #doc
%endif #gitweb

%files -n libgit-devel
%exclude %_libdir/common-main.o
%_libdir/lib*
%_includedir/*

%files doc
%pkgdocdir/

%files contrib
%dir %_datadir/git-core/
%_datadir/git-core/contrib/

%files diff-highlight
%_bindir/diff-highlight
%doc contrib/diff-highlight/README

%files subtree
%gitexecdir/git-subtree
%if_with doc
%_man1dir/git-subtree.*
%endif #doc

%changelog
* Sun Dec 08 2019 Dmitry V. Levin <ldv@altlinux.org> 2.24.1-alt1
- 2.24.0 -> 2.24.1 (fixes: CVE-2019-1348, CVE-2019-1387, CVE-2019-19604);
  this update also addresses a few Windows and/or NTFS issues
  (fixes: CVE-2019-1349, CVE-2019-1350, CVE-2019-1351, CVE-2019-1352,
  CVE-2019-1353, CVE-2019-1354).

* Sun Dec 08 2019 Dmitry V. Levin <ldv@altlinux.org> 2.24.0-alt4
- Removed Git::LoadCPAN proxy, we can rely on our system perl
  Error and Mail::Address modules.

* Sat Dec 07 2019 Dmitry V. Levin <ldv@altlinux.org> 2.24.0-alt3
- Fixed "--without doc" and "--without email" builds
  (by Michael Shigorin and me).

* Sun Nov 17 2019 Dmitry V. Levin <ldv@altlinux.org> 2.24.0-alt2
- Relocated bash completions (closes: #37426).
- Packaged git-subtree as a separate subpackage (closes: #37432).

* Mon Nov 04 2019 Dmitry V. Levin <ldv@altlinux.org> 2.24.0-alt1
- 2.21.0 -> 2.24.0.

* Sun Feb 24 2019 Dmitry V. Levin <ldv@altlinux.org> 2.21.0-alt1
- 2.19.2 -> 2.21.0.

* Wed Nov 21 2018 Dmitry V. Levin <ldv@altlinux.org> 2.19.2-alt1
- 2.17.2 -> 2.19.2.

* Thu Sep 27 2018 Dmitry V. Levin <ldv@altlinux.org> 2.17.2-alt1
- 2.17.1 -> 2.17.2 (fixes: CVE-2018-17456).

* Thu Aug 09 2018 Dmitry V. Levin <ldv@altlinux.org> 2.17.1-alt4
- Packaged diff-highlight as a separate subpackage
  (by Ivan A. Melnikov; closes: #35223).

* Fri Aug 03 2018 Dmitry V. Levin <ldv@altlinux.org> 2.17.1-alt3
- perl-Git: explicitly added perl(Error.pm) and perl(Mail/Address.pm)
  to dependencies.

* Fri Aug 03 2018 Dmitry V. Levin <ldv@altlinux.org> 2.17.1-alt2
- Renamed git subpackage to git-full (closes: #34254).
- Created new git subpackage that pulls in git-core and perl-Git
  subpackages only (closes: #34716).

* Tue May 22 2018 Dmitry V. Levin <ldv@altlinux.org> 2.17.1-alt1
- 2.16.4 -> 2.17.1.

* Tue May 22 2018 Dmitry V. Levin <ldv@altlinux.org> 2.16.4-alt1
- 2.15.2 -> 2.16.4.

* Tue May 22 2018 Dmitry V. Levin <ldv@altlinux.org> 2.15.2-alt1
- 2.14.4 -> 2.15.2.

* Tue May 22 2018 Dmitry V. Levin <ldv@altlinux.org> 2.14.4-alt1
- 2.13.7 -> 2.14.4.

* Tue May 22 2018 Dmitry V. Levin <ldv@altlinux.org> 2.13.7-alt1
- 2.12.5 -> 2.13.7.

* Fri Sep 22 2017 Dmitry V. Levin <ldv@altlinux.org> 2.12.5-alt1
- 2.11.4 -> 2.12.5.

* Fri Sep 22 2017 Dmitry V. Levin <ldv@altlinux.org> 2.11.4-alt1
- 2.10.5 -> 2.11.4.

* Fri Sep 22 2017 Dmitry V. Levin <ldv@altlinux.org> 2.10.5-alt1
- 2.10.4 -> 2.10.5 (fixes: CVE-2017-14867).

* Thu Aug 10 2017 Dmitry V. Levin <ldv@altlinux.org> 2.10.4-alt1
- 2.10.3 -> 2.10.4.

* Thu May 11 2017 Dmitry V. Levin <ldv@altlinux.org> 2.10.3-alt1
- 2.10.2 -> 2.10.3 (fixes: CVE-2017-8386).

* Fri Oct 28 2016 Dmitry V. Levin <ldv@altlinux.org> 2.10.2-alt1
- 2.9.3 -> 2.10.2.

* Fri Aug 12 2016 Dmitry V. Levin <ldv@altlinux.org> 2.9.3-alt1
- 2.8.4 -> 2.9.3.

* Mon Jun 06 2016 Dmitry V. Levin <ldv@altlinux.org> 2.8.4-alt1
- 2.7.4 -> 2.8.4.

* Fri Mar 18 2016 Dmitry V. Levin <ldv@altlinux.org> 2.7.4-alt1
- 2.6.6 -> 2.7.4

* Thu Mar 17 2016 Dmitry V. Levin <ldv@altlinux.org> 2.6.6-alt1
- 2.6.5 -> 2.6.6.

* Thu Mar 17 2016 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt3
- Merged jk/path-name-safety-2.6
  (fixes CVE‑2016‑2315 and CVE-2016-2324; closes: #31896).

* Mon Jan 11 2016 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt2
- Backported commit v2.7.0-rc2~9^2~11 (closes: #31665).

* Mon Jan 04 2016 Dmitry V. Levin <ldv@altlinux.org> 2.6.5-alt1
- 2.6.4 -> 2.6.5.

* Wed Dec 16 2015 Dmitry V. Levin <ldv@altlinux.org> 2.6.4-alt1
- 2.1.4 -> 2.6.4.

* Wed Dec 17 2014 Dmitry V. Levin <ldv@altlinux.org> 2.1.4-alt1
- Updated to maint 2.1.4.

* Wed Nov 05 2014 Dmitry V. Levin <ldv@altlinux.org> 2.1.3-alt1
- Updated to maint 2.1.3.

* Wed Jul 30 2014 Dmitry V. Levin <ldv@altlinux.org> 2.0.4-alt1
- Updated to maint 2.0.4.

* Fri May 30 2014 Dmitry V. Levin <ldv@altlinux.org> 1.9.4-alt1
- Updated to maint 1.9.4.

* Fri Feb 14 2014 Dmitry V. Levin <ldv@altlinux.org> 1.8.5.5-alt1
- Updated to maint v1.8.5.5.

* Sat Jan 25 2014 Dmitry V. Levin <ldv@altlinux.org> 1.8.4.5-alt1
- Updated to maint v1.8.4.5.
- Applied upstream fix for git-pull manpage (closes: #29718).

* Thu Nov 21 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.4.4-alt1
- Updated to maint v1.8.4.4.

* Thu Nov 14 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.4.3-alt1
- Updated to maint v1.8.4.3.

* Tue Jul 23 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.3.4-alt1
- Updated to maint v1.8.3.4.

* Mon May 13 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.2.3-alt1
- Updated to maint v1.8.2.3.

* Mon Apr 08 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.1.6-alt1
- Updated to maint v1.8.1.6.

* Sat Mar 02 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.1.5-alt1
- Updated to maint v1.8.1.5.

* Fri Feb 22 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.1.4-alt1
- Updated to maint v1.8.1.4 (fixes CVE-2013-0308 in git-imap-send).

* Fri Feb 08 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.1.3-alt1
- Updated to maint v1.8.1.3.

* Mon Jan 28 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.1.2-alt1
- Updated to maint v1.8.1.2.

* Mon Jan 14 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.1.1-alt1
- Updated to maint v1.8.1.1.

* Sun Jan 06 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.0.3-alt1
- Updated to maint v1.8.0.3.
- git-am: fixed "hg" patch format support (closes: #28248).

* Thu Oct 18 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.12.4-alt1
- Updated to maint v1.7.12.4.

* Tue Oct 09 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.12.3-alt1
- Updated to maint v1.7.12.3.

* Sat Oct 06 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.12.2-alt1
- Updated to maint v1.7.12.2-8-g9376c86.

* Sun Sep 16 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.11.7-alt1
- Updated to maint v1.7.11.7.

* Wed Sep 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.11.6-alt1
- Updated to maint v1.7.11.6.

* Wed Aug 15 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.11.5-alt1
- Updated to maint v1.7.11.5.

* Tue Aug 14 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.11.4-alt2
- Updated to maint v1.7.11.4-27-gb17a01d.
- Disabled broken i18n (closes: #27590).

* Tue Jul 31 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.11.4-alt1
- Updated to maint v1.7.11.4.

* Tue Jul 24 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.11.3-alt1
- Updated to maint v1.7.11.3.

* Mon Jun 18 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.10.5-alt1
- Updated to maint v1.7.10.5.

* Wed Jun 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.10.4-alt1
- Updated to maint 1.7.10.4.

* Fri Apr 27 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.9.7-alt1
- Updated to maint v1.7.9.7.

* Tue Apr 03 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.9.6-alt1
- Updated to maint v1.7.9.6.

* Tue Mar 27 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.9.5-alt1
- Updated to maint v1.7.9.5.

* Tue Mar 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.9.4-alt1
- Updated to maint v1.7.9.4.

* Wed Mar 07 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.9.3-alt1
- Updated to maint v1.7.9.3.
- git add --edit: do not pass terminal color sequences to editor
  (closes: #26999).

* Fri Feb 24 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.9.2-alt1
- Updated to maint v1.7.9.2.

* Thu Jan 19 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.8.4-alt1
- Updated to maint v1.7.8.4.

* Sun Jan 08 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.8.3-alt1
- Updated to maint v1.7.8.3.

* Fri Dec 16 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.7.5-alt1
- Updated to maint v1.7.7.5.

* Fri Dec 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.7.4-alt1
- Updated to maint v1.7.7.4-1-g1e501a7.
- libgit-devel: Fixed installed header files.

* Thu Nov 10 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.7.3-alt1
- Updated to maint v1.7.7.3.

* Wed Nov 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.7.2-alt1
- Updated to maint v1.7.7.2.

* Thu Oct 27 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.7.1-alt2
- Updated to maint v1.7.7.1-49-g25f745f.

* Wed Oct 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.7.1-alt1
- Updated to maint v1.7.7.1.

* Mon Sep 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.6.4-alt1
- Updated to maint v1.7.6.4.

* Tue Sep 13 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.6.3-alt1
- Updated to maint v1.7.6.3.

* Wed Sep 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.6.2-alt1
- Updated to maint v1.7.6.2.

* Thu Aug 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.6.1-alt1
- Updated to maint v1.7.6.1.

* Fri Aug 05 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.6-alt1
- Updated to maint v1.7.6-40-ge9e0643.

* Thu Jun 02 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.5.4-alt1
- Updated to maint v1.7.5.4.

* Fri May 27 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.5.3-alt1
- Updated to maint v1.7.5.3.

* Tue May 24 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.5.2-alt1
- Updated to maint v1.7.5.2-1-g9963e02.

* Wed Apr 20 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.4.5-alt1
- Updated to maint v1.7.4.5.

* Thu Apr 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.4.4-alt1
- Updated to maint v1.7.4.4.

* Mon Apr 04 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.4.3-alt1
- Updated to maint v1.7.4.3.

* Mon Mar 28 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.4.2-alt1
- Updated to maint v1.7.4.2.

* Sat Feb 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.4.1-alt1
- Updated to maint v1.7.4.1.

* Thu Feb 03 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.4-alt1
- Updated to maint v1.7.4.

* Thu Jan 06 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.5-alt1
- Updated to maint v1.7.3.5.

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.4-alt1
- Updated to maint v1.7.3.4 (fixes an XSS in gitweb, see CVE-2010-3906).

* Fri Dec 10 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.3-alt1
- Updated to maint v1.7.3.3.
- gitweb: perl-unicore is required nowadays (see #24733).

* Mon Nov 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.2-alt2
- Updated to maint v1.7.3.2-4-g60aa9cf.
- Fixed build with new perl.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.2-alt1
- Updated to maint v1.7.3.2.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.1-alt1
- Updated to maint v1.7.3.1-9-g8695353.
- Rebuilt with libssl.so.10.

* Fri Sep 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.3-alt1
- Updated to maint v1.7.2.3.
- Relocated hooks to /usr/share/git-core/hooks/,
  converted template hooks to symlinks.

* Fri Aug 20 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.2-alt1
- Updated to maint v1.7.2.2.

* Fri Aug 13 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.1-alt2
- Updated to maint v1.7.2.1-45-gb5e233e.
- Backport upstream fix for parsing of ":/token" syntax (closes: #23718).

* Wed Jul 28 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.1-alt1
- Updated to maint v1.7.2.1.
- hooks/pre-commit: when invoked by gear-commit,
  ensure that .gear/tags/ is up to date.

* Thu Jul 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.1.1-alt2
- Updated to maint v1.7.1.1-29-g971ecbd.

* Thu Jul 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.1.1-alt1
- Updated to maint v1.7.1.1.

* Thu May 27 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.0.6-alt1
- Updated to maint v1.7.0.6-4-gdfea790.
- git-core: relocated several utilities to perl-Git.
- git-email: added some perl-libnet's deps (workarounds: #23407).

* Wed Mar 31 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.0.4-alt1
- Updated to maint v1.7.0.4.

* Tue Mar 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.0.3-alt1
- Updated to maint v1.7.0.3.
- Packaged contrib subpackage (closes: #22754).

* Sun Feb 14 2010 Dmitry V. Levin <ldv@altlinux.org> 1.6.6.2-alt1
- Updated to maint v1.6.6.2-3-g341d9a4.
- Made most of subpackages noarch.

* Thu Feb 11 2010 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.8-alt2
- Updated to maint v1.6.5.8-11-g33f0ea4.

* Thu Jan 21 2010 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.8-alt1
- Updated to maint v1.6.5.8.

* Thu Dec 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.7-alt1
- Updated to maint v1.6.5.7.

* Fri Dec 11 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.6-alt1
- Updated to maint v1.6.5.6.

* Thu Dec 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.5-alt1
- Updated to maint v1.6.5.5-7-g5c30b8f.

* Thu Dec 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.4-alt1
- Updated to maint v1.6.5.4.

* Tue Nov 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.3-alt1
- Updated to maint v1.6.5.3.
- Disabled git-svn on ARM by default.

* Mon Nov 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.2-alt2
- Updated to maint v1.6.5.2-10-g7545712.
- libgit-devel: Packaged /usr/include/git/compat symlink.

* Mon Oct 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.5.2-alt1
- Updated to maint v1.6.5.2.
- Enabled Linus's block-sha1 implementation.

* Thu Sep 17 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.4.4-alt1
- Updated to maint v1.6.4.4.

* Mon Sep 14 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.4.3-alt1
- Updated to maint v1.6.4.3.
- Moved "make check" to %%check section.

* Mon Aug 31 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.4.2-alt1
- Updated to maint v1.6.4.2.

* Sun Aug 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.3.4-alt1
- Updated to maint v1.6.3.4-13-g57f6ec0.

* Mon Jun 22 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.3.3-alt1
- Updated to maint v1.6.3.3-3-g1ab012c.

* Mon Jun 15 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.3.2-alt2
- Updated to maint v1.6.3.2-17-g50a991e (closes: #20426).

* Thu Jun 04 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.3.2-alt1
- Updated to maint v1.6.3.2.

* Thu May 14 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.3.1-alt1
- Updated to maint v1.6.3.1.
- Fixed build of documentation with fresh asciidoc and docbook xsl (closes: #17003).

* Wed May 06 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.2.5-alt1
- Updated to maint v1.6.2.5.
- Fixed build of documentation with fresh docbook xsl (closes: #19936).

* Mon Apr 20 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.2.4-alt1
- Updated to maint v1.6.2.4.

* Mon Apr 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.2.3-alt1
- Updated to maint v1.6.2.3.

* Sun Feb 08 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.1.3-alt1
- Updated to maint v1.6.1.3.

* Thu Jan 29 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.1.2-alt1
- Updated to maint v1.6.1.2.

* Mon Jan 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.1.1-alt1
- Updated to maint v1.6.1.1.

* Wed Jan 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.1-alt1
- Updated to maint v1.6.1-23-g152d70f.

* Fri Dec 19 2008 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.6-alt1
- Updated to maint v1.6.0.6.

* Tue Dec 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.5-alt1
- Updated to maint v1.6.0.5.

* Sun Nov 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.4-alt1
- Updated to maint v1.6.0.4.

* Fri Oct 31 2008 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.3-alt2
- Updated to maint v1.6.0.3-13-ge855bfc.

* Wed Oct 22 2008 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.3-alt1
- Updated to maint v1.6.0.3.
- Packaged bash completion for git.
- Changed new builtin merge command to use the same color defaults.
- Fixed build of documentation with fresh asciidoc and docbook xsl (closes: #17003).

* Mon Oct 20 2008 Dmitry V. Levin <ldv@altlinux.org> 1.6.0.2-alt1
- Updated to maint v1.6.0.2-112-g09cff06.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.6.5-alt2
- Updated to maint v1.5.6.5-21-g21926fe.

* Thu Aug 07 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.6.5-alt1
- Updated to maint v1.5.6.5.

* Mon Jul 21 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.6.4-alt1
- Updated to maint v1.5.6.4.

* Fri Jul 18 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.6.3-alt1
- Updated to maint v1.5.6.3-22-g473a189.

* Thu Jul 10 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.6.2-alt1
- Updated to maint v1.5.6.2-24-ge09c4e7.

* Wed Jul 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.5.5-alt1
- Updated to maint v1.5.5.5.

* Fri Jun 13 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.5.4-alt1
- Updated to maint v1.5.5.4-3-g2feaf4e.

* Wed May 28 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.5.3-alt1
- Updated to maint v1.5.5.3.

* Tue May 27 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.5.2-alt1
- Updated to maint v1.5.5.2-13-g109440c.

* Tue May 27 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.4.5-alt3
- Updated to maint v1.5.4.5-44-g5070b49.

* Fri May 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.4.5-alt2
- Updated to maint v1.5.4.5-36-g15ddb6f.

* Fri Mar 28 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.4.5-alt1
- Updated to maint v1.5.4.5.

* Mon Mar 24 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.4.4-alt2
- Updated to maint v1.5.4.4-25-g81d6650.
- Fixes git-fetch exit status (#15037).
- Turned off color diff on git commit -v (kas@).

* Wed Mar 12 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.4.4-alt1
- Updated to maint v1.5.4.4.

* Tue Jan 08 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.8-alt1
- Updated to maint v1.5.3.8.

* Sun Dec 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.7-alt1
- Updated to maint v1.5.3.7.

* Sat Dec 01 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.6-alt2
- buffer_is_binary: Removed buffer size limitation.
- Updated to maint v1.5.3.6-43-g10455d2.

* Mon Nov 19 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.6-alt1
- Updated to maint v1.5.3.6.

* Wed Oct 31 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.5-alt1
- Updated to maint v1.5.3.5.

* Tue Oct 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.4-alt2
- Updated to spearce/maint v1.5.3.4-49-g2ee52eb.
- builtin-push.c: Added "push.thin" config parameter support.
- Install git-sh-setup without execute permissions set.

* Thu Oct 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.4-alt1
- Updated to maint v1.5.3.4.

* Tue Oct 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.3-alt1
- Updated to maint v1.5.3.3-7-g5946d4b.

* Thu Sep 20 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.2-alt1
- Updated to maint v1.5.3.2.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.1-alt2
- git-commit:
  + Disallow amend if it is going to produce an empty non-merge commit.
  + Ensure that new commit is not an empty non-merge commit.
  + Add --fast option.

* Mon Sep 03 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.3.1-alt1
- Updated to maint v1.5.3.1.

* Thu Aug 16 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.2.5-alt1
- Updated to maint v1.5.2.5.

* Tue Aug 07 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.2.4-alt2
- Updated to maint v1.5.2.4-5-g9396943.
- libgit-devel: Packaged cache-tree.h (#12391).
- templates/hooks--pre-rebase: Changed syntax to be "sh -n" safe.

* Sun Jul 15 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.2.4-alt1
- Updated to maint v1.5.2.4.

* Wed May 30 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.6-alt2
- Updated to maint v1.5.1.6-23-g7faf068.

* Mon May 21 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.6-alt1
- Updated to maint v1.5.1.6-6-g5b6dedd.

* Wed May 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.4-alt1
- Updated to maint v1.5.1.4.

* Tue May 01 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.3-alt1
- Updated to maint v1.5.1.3.

* Sun Apr 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.2-alt1
- Updated to maint v1.5.1.2.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.1-alt1
- Updated to maint v1.5.1.1.

* Wed Apr 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.7-alt1
- Updated to maint v1.5.0.7.

* Thu Mar 29 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.6-alt1
- Updated to maint v1.5.0.6.

* Sat Mar 17 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.4-alt1
- Updated to maint v1.5.0.4-1-g2be08a8.

* Mon Mar 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.3-alt1
- Updated to maint v1.5.0.3.

* Tue Feb 27 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.2-alt1
- Updated to maint v1.5.0.2.

* Sat Feb 24 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.1-alt4
- Updated to maint v1.5.0.1-30-g5089277.
- Changed git-receive-pack to run post-update hook iff
  at least one update succeeded.

* Fri Feb 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.1-alt3
- Updated to maint v1.5.0.1-25-g75b62b4.
- Fixed "git-show-ref --verify" error diagnostics.

* Thu Feb 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.1-alt2
- Updated to maint v1.5.0.1-23-g4917d2a.
- git-doc: Packaged RelNotes* and SubmittingPatches files.

* Mon Feb 19 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.1-alt1
- Updated to maint v1.5.0.1.

* Sun Feb 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt2
- Updated to maint v1.5.0-25-g21b4875.

* Sun Feb 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- Updated to maint v1.5.0-13-gde6f0de.
- Added git-gui subpackage.
- Disabled coloring in git-format-patch (fixes: #10743).
- Replaced custom templates/hooks--update with upstream version.

* Tue Jan 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.4.4-alt1
- Updated to maint v1.4.4.4.

* Tue Dec 26 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.4.3-alt1
- Updated to maint v1.4.4.3-ge6d40d6.

* Mon Dec 18 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.4.2-alt1
- Updated to maint v1.4.4.2-g7da41f4.

* Thu Dec 07 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.4.1-alt2
- Updated to maint v1.4.4.1-g562cefb.
- Packaged gitweb subpackage.
- Tweaked templates/ hooks.

* Fri Nov 24 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.4.1-alt1
- Updated to maint v1.4.4.1.

* Sun Nov 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.5-alt1
- Updated to maint v1.4.3.5.
- Fixed git-archive and git-upload-archive packaging (#10260).
- Made perl interface a separate subpackage.

* Sun Nov 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.4-alt1
- Updated to maint v1.4.3.4.
- Packaged emacs modes (#10100).

* Thu Nov 02 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.3-alt2
- Updated to maint v1.4.3.3-ge23ed9a.

* Thu Oct 26 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.3-alt1
- Updated to maint v1.4.3.3.

* Tue Oct 24 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.2-alt1
- Updated to maint v1.4.3.2.

* Mon Oct 23 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.1-alt2
- Updated to maint v1.4.3.1-g0abc026.
- Removed git-merge-recursive-old to avoid python requirements.

* Sat Oct 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.1-alt1
- Updated to maint v1.4.3.1.
- git-email: Do not package Error.pm (at@).

* Sat Oct 21 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt2
- Updated to maint v1.4.3-gb507b46.
- Packaged libgit.a and accompanying header files.

* Fri Oct 20 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- Updated to maint v1.4.3-g6b09c78.

* Tue Oct 17 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2.4-alt1
- Updated to maint v1.4.2.4.

* Tue Oct 03 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2.3-alt1
- Updated to maint v1.4.2.3.

* Sat Sep 30 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2.2-alt1
- Updated to maint v1.4.2.2.
- Moved git-daemon to separate subpackage git-server,
  added xinetd config file.

* Sun Sep 24 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2.1-alt2
- Updated to maint v1.4.2.1-gf2b5792.
- git-tar-tree:
  + Unhardcoded &~022 mode change.
  + Changed default tar_umask to 022.
- git-tag:
  + New option: --full-ref-name, required by gear-release(1).

* Thu Sep 14 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2.1-alt1
- Updated to maint v1.4.2.1.
- core-tutorial, cvs-migration, tutorial-2: Fixed broken links.

* Mon Sep 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt2
- count-objects, describe, merge-tree:
  Fixed to make these commands work in subdirectory.
- git, describe, merge-tree:
  Fixed invalid argc handling.
- BuildRequires: Added subversion for svn-enabled build.

* Wed Aug 23 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- Updated to maint v1.4.2-g60a6bf5.
- Changed default pager from `less' to `less -R'.
- Changed default diff.color from `never' to `auto'.

* Tue Aug 15 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4.1.1-alt1
- Updated to 1.4.1.1.

* Thu May 25 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt3
- hooks--update:
  + Handle the case when git-merge-base fails.
  + Handle mailto file with newlines.

* Fri May 19 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt2
- Updated to maint be0c7e06.
- Hardlinked identical files together.

* Tue May 16 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt1
- Updated to 1.3.3.

* Tue May 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt3
- Updated to maint d1802851.

* Mon May 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt2
- Updated to maint 178613c7.
- Updated git-svn from next.
- Separated object name errors from usage errors.
- Package git-svn.

* Thu May 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Wed Apr 26 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Wed Apr 19 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.
- Replaced default templates/hooks--update with my edition.

* Sat Apr 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.6-alt1
- Updated to 1.2.6.
- git-tar-tree:
  + Clear S_IWGRP|S_IWOTH bits from permissions in archived files.

* Wed Apr 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5.

* Mon Mar 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt2
- Avoid compressing templates (#9231).

* Thu Mar 02 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Thu Feb 23 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3.

* Mon Feb 20 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Fri Feb 17 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.

* Tue Feb 14 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt2
- Workaround grave bug in docbook-style-xsl to fix generated manpages.
- Packaged manpages within core subpackage.
- Renamed docs -> doc.
- Enabled git core tests during build by default.

* Sat Feb 04 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt1
- Updated to 1.1.6.

* Fri Dec 23 2005 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3.

* Sun Dec 04 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.9l-alt1
- Updated to 0.99.9l.
- Changed subpackage names from git-core-<name> to git-<name>.
- Created empty git package which brings in all subpackages.
- Renamed git-tk to gitk.

* Fri Nov 25 2005 Dmitry V. Levin <ldv@altlinux.org> 0.99.9i-alt1
- Updated to 0.99.9i.
- Modularized and cleaned up specfile.

* Thu Nov 10 2005 Chris Wright <chrisw@osdl.org> 0.99.9g-1
- zlib dependency fix
- Minor cleanups from split
- Move arch import to separate package as well

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 0.99.8f-alt1
- 0.99.8f (thanks vsu@ for notifying)
- removed WITH_OWN_SUBPROCESS_PY, use python-2.4's

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 0.99.8e-alt1
- built for ALT Linux
- separate docs subpackage

* Tue Sep 27 2005 Jim Radford <radford@blackbean.org>
- Move programs with non-standard dependencies (svn, cvs, email)
  into separate packages

* Tue Sep 27 2005 H. Peter Anvin <hpa@zytor.com>
- parallelize build
- COPTS -> CFLAGS

* Fri Sep 16 2005 Chris Wright <chrisw@osdl.org> 0.99.6-1
- update to 0.99.6

* Fri Sep 16 2005 Horst H. von Brand <vonbrand@inf.utfsm.cl>
- Linus noticed that less is required, added to the dependencies

* Sun Sep 11 2005 Horst H. von Brand <vonbrand@inf.utfsm.cl>
- Updated dependencies
- Don't assume manpages are gzipped

* Thu Aug 18 2005 Chris Wright <chrisw@osdl.org> 0.99.4-4
- drop sh_utils, sh-utils, diffutils, mktemp, and openssl Requires
- use RPM_OPT_FLAGS in spec file, drop patch0

* Wed Aug 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.99.4-3
- use dist tag to differentiate between branches
- use rpm optflags by default (patch0)
- own %_datadir/git-core/

* Mon Aug 15 2005 Chris Wright <chrisw@osdl.org>
- update spec file to fix Buildroot, Requires, and drop Vendor

* Sun Aug 07 2005 Horst H. von Brand <vonbrand@inf.utfsm.cl>
- Redid the description
- Cut overlong make line, loosened changelog a bit
- I think Junio (or perhaps OSDL?) should be vendor...

* Thu Jul 14 2005 Eric Biederman <ebiederm@xmission.com>
- Add the man pages, and the --without docs build option

* Wed Jul 7 2005 Chris Wright <chris@osdl.org>
- initial git spec file
