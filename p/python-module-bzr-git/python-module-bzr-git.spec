# $Id: python-module-bzr-git.spec $
# -*- coding: utf-8 -*-
Name: python-module-bzr-git
Version: 0.6.12
Release: alt5.bzr20150806

%setup_python_module bzr-git
%def_without test

Summary: A GIT branch and repository format implementation for bzr
License: %gpl2plus
Group: Development/Python

Url: https://launchpad.net/bzr-git
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(Pre): rpm-build-licenses
Provides: bzr-git = %version

%description
Using Bazaar with Git.

The bzr-git plugin provides support for using Bazaar with local and remote
Git repositories, as just another format. You can clone, pull from and
push to git repositories as you would with any native Bazaar branch.

The bzr-git plugin also adds three new bzr subcommands:

 * bzr git-objects: Extracts Git objects out of a Bazaar repository
 * bzr git-refs: Display Git refs from a Bazaar branch or repository
 * bzr git-import: Imports a local or remote Git repository to a set of Bazaar
                   branches

The 'git:' revision specifier can be used to find revisions by short or long
GIT SHA1.

This module is built for python %_python_version

%package -n bzr-git-remote
Summary: Remote helper for git to work with bzr repositories
Group: Development/Other
Provides: git-remote-bzr
Requires: %name = %version-%release

%description -n bzr-git-remote
This command provides support for using bzr repositories as Git
remotes, through the bzr-git plugin. At the moment it supports cloning
from, fetching from and pushing into Bazaar repositories. Fetch support
is still experimental, and may be slow.

%package -n python-module-bzr-git-tests
Summary: bzr-git plugin tests
Group: Development/Other
Requires: %name = %version-%release
Requires: python%_python_version(bzrlib.tests)
Requires: python%_python_version(pysqlite2)
Requires: python%_python_version(dulwich.tests)
Requires: python%_python_version(tdb)

%description -n python-module-bzr-git-tests
This package contain tools and test suites for testing bzr-git.

%prep
%setup -n %modulename-%version
%patch0 -p1

%build
%python_build

%if_with tests
rm -rf %buildroot%python_sitelibdir/bzrlib/plugins/git/tests
%endif

%install
%python_install --install-lib %python_sitelibdir
%find_lang %name
install -dm0755 %buildroot%_man1dir
install -m0644 git-remote-bzr.1 %buildroot%_man1dir

%files
%python_sitelibdir/bzrlib/plugins/git
%exclude %python_sitelibdir/bzrlib/plugins/git/tests
%python_sitelibdir/*.egg-info
%doc HACKING INSTALL NEWS README TODO notes/*

%files -n bzr-git-remote
%_bindir/*
%_man1dir/*

%if_with tests
%files -n python-module-bzr-git-tests
%dir %python_sitelibdir/bzrlib/plugins/git
%python_sitelibdir/bzrlib/plugins/git/tests
%endif

%changelog
* Thu Feb 06 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.6.12-alt5.bzr20150806
- Build without tests for python module due module tdb build for python3 only

* Sat Apr 27 2019 Anatoly Kitaykin <cetus@altlinux.org> 0.6.12-alt4.bzr20150806
- Re-package files

* Wed Dec 06 2017 Anatoly Kitaykin <cetus@altlinux.org> 0.6.12-alt3.bzr20150806
- Rename subpackage git-remote-bzr to bzr-git-remote

* Thu Dec 01 2016 Anatoly Kitaykin <cetus@altlinux.org> 0.6.12-alt2
- Update to current repository version

* Wed Oct 02 2013 Anatoly Kitaykin <cetus@altlinux.org> 0.6.12-alt1
- Release 0.6.12

* Wed Oct 17 2012 Anatoly Kitaykin <cetus@altlinux.org> 0.6.9-alt1
- initial build
