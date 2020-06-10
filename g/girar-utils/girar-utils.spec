Name:     girar-utils
Version:  1.5.10
Release:  alt1

Summary:  git.alt client utilities
License:  GPL
Group:    Development/Other
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: gear, help2man

%description
This package contains client utilities for git.alt.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_mandir/man?/*

%changelog
* Fri Jun 05 2020 Andrey Cherepanov <cas@altlinux.org> 1.5.10-alt1
- girar-show: remove planned subtasks operation
- girar-show: add autodetect of ssh name of build host

* Wed Jun 27 2018 Grigory Ustinov <grenka@altlinux.org> 1.5.9.1-alt1
- Fix little typo.

* Sun Jul 24 2016 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt1
- [girar-show] Remove preceding # from task number
- [girar-show] Add -t argument to show days after last build

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.8-alt1
- girar-import -p,--people[=DIR]: new option; it makes collaboration
  with other people through git.alt more convenient (e.g., the email
  notifications about your new changes will be more interesting).

* Wed Sep 30 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.7-alt1
- [girar-show] support GIT_ALT for git.alt host
- [girar-show] fix log detect

* Thu Oct 02 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.6.1-alt1
- [girar-show] Show only FAILED messages in statistics mode

* Thu Oct 02 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.6-alt1
- girar-show:
  + fix highlight unmets with version and names containing ., _ and :
    symbols
  + add highlight for fatal errors (such as `No such file or directory`)
    and "should be made noarch"
  + <tasknum>@! now display only errors without service message except
    failed subtask
  + do not display removed subtasks in subtask list

* Fri Sep 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- girar-show:
  + fix subtask highlighting
  + support broken dep, Perl requirements and unmet errors highlight

* Tue Jul 22 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.4-alt1
- Add girar-show: show highlighted task list and task log

* Sat Nov 21 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.3-alt1
- girar-import: provide options to try import only from /gears/ or
  /srpms/ hierarchy
- girar-upload: add --origin option to specify git remote name

* Thu Nov 19 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.2.1-alt1
- girar-clone, girar-import: -R requires argument
- girar-import: process -u/--update

* Sat Oct 17 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.2-alt1
- girar-import: reworked to import only one branch, added ability to
  update existing repository
- girar-remote: fixed usage (closes: #20890)
- Updated manpage for girar-import (closes: #20823)

* Sat Jul 18 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.1-alt1
- New utility:
  + girar-import: clone package from girar archive.

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.0-alt1
- Global changes:
  + Configured ssh alias is required, dropped -u/-s/-p options
    in favor of -R.
  + Use git-config to store utility options.
- New utilites:
  + girar-clone: clone other's repository from git.alt server.
  + girar-find-package: date formatting interfase to girar's
    find-package command.
  + girar-remote: execute command on git.alt server.
  + girar-remote-uri: construct git URI out of directory name and
    optional user name.

* Mon Apr 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- girar-upload:
  + Changed to use git-config to save remote origin configuration.
  + Updated for current girar init-db interface.

* Wed Feb 28 2007 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- Renamed package: gear -> girar-utils.
  This package will contain basic git.alt client utilities.

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- gear-update-tag: Fix temporary directory removal (ldv).
- gear-update-tag: Treat "zip" directive as "tar" (raorn).
- gear: Implement suffix= option for tar-like rules (george).

* Wed Nov 22 2006 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- gear, gear-commit, gear-sh-functions.in:
  Reworked to implement .gear-rules "tags:" directive and
  .gear-tags directory support (vsu, raorn).
- gear-update-tag:
  New utility, updates list of stored tags
  in the package repository (vsu).
- gear-update-archive:
  Avoid loss of source files due to .gitignore (vsu).
- gear-release:
  Removed unneeded utility, the idea of release tags
  seems to be dead-end (ldv).
- Renamed info() to msg_info() to avoid ambiguity and
  unwanted package requirements (ldv).
- QUICKSTART.ru_RU.KOI8-R: Fix typos (#10229).
- gear-srpmimport:
  Removed implicit requirement for --branch (ldv, #10274).
- gear:
  Added keyword substitution in directory name (ldv, #10091).
  Replaced deprecated "git-tar-tree" with "git-archive --format=tar" (ldv).
  Implemented zip archive type support (raorn).
- gear-upload:
  New utility to ease initial upload of git repositories to git.alt (legion).

* Thu Oct 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt1
- Update copyright information.
- Add fresh git-core to package requirements.
- gear:
  + Process exclude directives without warnings (vsu).
- gear-sh-functions.in:
  + Fix checks for multiple specfiles (vsu).
- gear-release:
  + Create tags in refs/releases/ directory (ldv).
- gear-update-archive:
  + Fix old source removal (ldv).
  + Fix check for untracked or modified files (legion).
  + Implement top directory update (legion).
  + Fix destination directory validation (legion).
  + Fix typos (vsu).
- gear-hsh-build:
  + more flexible hasher support (raorn).
  + also pass --repo option to hasher (raorn).
  + honor "target" option from hasher config (raorn).
  + use $GIT_DIR/$CWD if no repositories given (raorn).
- Makefile:
  + Specify the program source for man pages (vsu).
  + Remove boldface from the NAME section of man pages (vsu).
- gear.1.inc:
  + Document operating modes of gear (vsu).
  + Document current limitations of gear (vsu).
- gear-commit.1.inc:
  + Fix short description (ldv).
- gear-update-archive.1.inc, gear-update-directory.1.inc:
  + Fix typos (vsu).

* Fri Sep 08 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt1
- gear:
  + New option: --update-spec (legion).
- gear-commit:
  + New option: --spec (legion).
- gear-release:
  + New option: --create (legion).
- gear-update:
  + Rename to gear-update-archive (legion).
- gear-hsh-build:
  + New utility (raorn).

* Mon Aug 28 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- gear-release: Fix typo in option handling (legion).
- gear-update: New utility (legion, ldv).

* Tue Aug 22 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.0-alt1
- Initial revision.
