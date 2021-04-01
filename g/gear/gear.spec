Name: gear
Version: 2.5.0
Release: alt1

Summary: Get Every Archive from git package Repository
License: GPLv2+
Group: Development/Other
Url: http://www.altlinux.org/Gear
BuildArch: noarch

Source: %name-%version.tar

Requires: gear-sh-functions = %EVR

# due to gear-srpmimport.
Requires: faketime

# due to magic signature in pathspec.
Requires: git-core >= 0:1.9.0

# due to quote_shell_args()
Requires: libshell >= 0:0.1.0

# due to default output tarball compressor
Requires: tar >= 1.29.0.19.d061, zstd

# hasher>=1.0.30 supports tar packages made by gear utility.
Conflicts: hasher < 0:1.0.30

BuildPreReq: asciidoc, git-core >= 1.8.0, help2man, libshell >= 0:0.0.3-alt1
%{?!_without_check:%{?!_disable_check:BuildRequires: bzip2, gzip, faketime, unzip, xz, zip, zstd}}

%description
This package contains utilities for building RPM packages from GEAR
repositories and managing GEAR repositories.
See %_docdir/%name-%version/QUICKSTART.ru_RU.UTF-8 for details.

%package sh-functions
Summary: GEAR shell functions
Group: Development/Other
# git-core is optional
%filter_from_requires /^git-core/d

%description sh-functions
This package contains GEAR's shell functions.

%package -n describe-specfile
Summary: Print specfile name and version using gear's parser
Group: Development/Other
Requires: gear-sh-functions = %EVR

%description -n describe-specfile
This package contains utility which uses GEAR's spec parser to determine
specfile for its name and version info.

%prep
%setup

%build
%make_build
asciidoc docs/ABOUT.ru.utf8
asciidoc docs/QUICKSTART.ru.utf8

%check
make check

%install
%makeinstall_std
install -pDm644 contrib/gear-bash_completion \
	%buildroot/etc/bash_completion.d/gear
ln -s gear-store-tags %buildroot%_bindir/gear-update-tag
ln -s gear-store-tags.1 %buildroot%_man1dir/gear-update-tag.1

%define _unpackaged_files_terminate_build 1

%files
%config /etc/bash_completion.d/*
%_bindir/gear*
%exclude %_bindir/gear-sh-functions
%_datadir/%name
%_mandir/man?/gear*
%doc docs/QUICKSTART* docs/ABOUT*

%files sh-functions
%_bindir/gear-sh-functions

%files -n describe-specfile
%_bindir/describe-specfile*
%_man1dir/describe-specfile*

%changelog
* Wed Mar 17 2021 Dmitry V. Levin <ldv@altlinux.org> 2.5.0-alt1
- Added exclude= option for tar: and zip: directives
  (by Alexey Gladkov; closes: #39801).
- describe-specfile (by Gleb Fotengauer-Malinovskiy):
  + new utility, prints name and version info for specfile.
- gear:
  + change the current workdir back before the last command invocation.
- gear-changelog (by Arseny Maslennikov):
  + added --header-only option to only print changelog header.
- gear-create-tag:
  + refuse to create tags that do not define all specsubst variables;
  + implemented -s/--specsubst option (closes: #39783).
- gear-update-sh-functions (by Gleb Fotengauer-Malinovskiy):
  + fixed permissions (755 -> 644).
- Moved gear-sh-functions and describe-specfile to separate
  subpackages (by Gleb Fotengauer-Malinovskiy).
- Updated bash completions.

* Sun Dec 27 2020 Dmitry V. Levin <ldv@altlinux.org> 2.4.2-alt1
- Updated git-core requirement.
- gear-srpmimport: expanded help text on --stdin option a bit.
- tests: sort output before comparison in one more place (by Ivan Zakharyaschev).

* Sat Dec 26 2020 Vitaly Chikunov <vt@altlinux.org> 2.4.1-alt1
- Re-enable multi-threaded compression for xz and zstd.

* Sat Dec 19 2020 Dmitry V. Levin <ldv@altlinux.org> 2.4.0-alt1
- Added "exclude=" option to "diff" directive
  (by Vladimir D. Seleznev, Alexey Gladkov, and me).

* Mon Feb 10 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.0-alt1
- gear-update: made --ignore-exclude the default behaviour (closes: #37371),
  added --honor-exclude option.

* Tue Mar 06 2018 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt1
- gear-srpmimport: honor RPMFILE_SPECFILE.
- gear-changelog (by Alexey Gladkov):
  + added --no-credits option to omit credits;
  + added --no-header option to omit changelog header;
  + added --since-date option to show commits since a specified date.
- gear-commit (by Alexey Gladkov; closes: #33452):
  + added gear.commit.edit-message config parameter: when set to true,
    an editor is invoked for further editing of the generated commit
    message;
  + added gear.commit.require-message-save config parameter: when set
    to true, the commit is aborted if the generated commit message
    has not been edited by the user.
- Updated bash completion for gear (by Alexey Gladkov).

* Mon Nov 20 2017 Dmitry V. Levin <ldv@altlinux.org> 2.1.1-alt1
- Applied bash4 compatibility workaround (closes: #32147).
- Added SOURCE_DATE_EPOCH support (closes: #34203).

* Wed Mar 22 2017 Dmitry V. Levin <ldv@altlinux.org> 2.1.0-alt1
- Added zstd(1) support in .gear-rules and import tools.
- gear: added support for lz4(1), lzop(1), xz(1), and zstd(1)
  in output tarball compression, changed default from gzip to zstd.
- tests: fixed for git >= 2.10.

* Fri May 06 2016 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt1
- gear-changelog, gear-edit-spec: look for specfile using the same
  algorithm as gear-commit (by Alexey Gladkov and me; closes: #18140).

* Fri Mar 11 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.6-alt1
- gear-edit-spec: new utility, invokes editor for specfile.

* Tue Feb 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0.5-alt1
- gear-changelog-rpm: added support of epoch.

* Sun Aug 31 2014 Dmitry V. Levin <ldv@altlinux.org> 2.0.4-alt1
- gear-update: added --strip-components option (by Alexey Gladkov).
- gear-create-tag:
  + added --quiet option (by Alexey Gladkov);
  + unless in quiet mode, print messages about the tag being created
    both before and after the action (by Alexey Gladkov; closes: #30266).

* Wed May 22 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.3-alt1
- gear-update-src-{cpio,gem,tar,zip}: set safe permissions
  of the unpacked directory tree.
- gear: fixed --export-dir support (by Paul Wolneykien).

* Mon Jan 21 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.2-alt1
- Fixed typo in specsubst support.

* Tue Jan 08 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt1
- test suite: updated for git >= 1.8.0.

* Fri Dec 14 2012 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt1
- gear-sh-functions (expand_rpm_macros): changed macros expansion
  algorithm to expand those macros that are known and leave unknown
  macros unexpanded.
- Implemented .gear/rules specsubst directive that controls
  instantiation of spec file templates with parameters
  defined by tag objects (closes: #20912).

* Tue Dec 04 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.7-alt1
- gear-store-tags: handle the last line of .gear/rules when
  it is not EOL-terminated (closes: #28165).

* Sun Nov 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.6-alt1
- gear-srpmimport: added support of srpms with type RPMLEAD_BINARY.

* Sun Oct 28 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.5-alt1
- gear-commit: improved specfile guess logic (closes: #27754).
- gear-srpmimport: fixed import of archives containing .git
  subdirectories by ignoring these .git subdirectories (closes: #25981).

* Thu Jul 26 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.4-alt1
- gear: allowed path separators in tar base names (closes: #27400).
- test suite: updated for git >= 1.7.11.

* Thu Apr 12 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.1-alt1
- test suite: updated for zip >= 3.0.

* Mon Feb 27 2012 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.0-alt1
- gear-command-remote-build: canonicalize workdir
  (by Alexey Gladkov; closes: #19994).
- gear-update: added --remove-source option (by Alexey Gladkov).
- gear-mock: new utility, implements support for mock build system
  (by Alexey Gladkov).
- gear: pass -n option to gzip(1) by default.
- test suite: updated for git >= 1.7.9.

* Fri Aug 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.6-alt1
- gear-srpmimport: added xz support.
- gear(1): minor documentation enhancements.
- gear: implemented support for specifying a HEAD subtree to --tree-ish
  along with --commit (by Kirill Shutemov).

* Sun Mar 06 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.5-alt1
- gear-merge: fixed incomplete migration to libshell in 1.6.0-alt1
  (by Vladimir Kamarzin; closes: #24268).

* Sat Mar 05 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.4-alt1
- gear-*-rules.5: fixed title line sections.

* Sat Feb 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.3-alt1
- gear: fixed typo in --commit during merge (closes: #25160).
- gear-srpmimport: pass --no-verify option to git-commit.

* Mon Sep 06 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.2-alt1
- gear-import: pass --no-verify option to git-commit.
- Renamed gear-update-tag to gear-store-tags (closes: #18739).
- gear-command-{hasher,rpmbuild}: unset GIT_* environment
  variables used by gear itself (closes: #20884).
- tests: fixed false positive on non-tmpfs filesystems
  (closes: #24012).

* Thu Jul 29 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.1-alt1
- gear-update-tag --verify: Implemented check for missing and
  unnecessary tags.

* Wed Jul 28 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.2-alt1
- gear-commit, gear-merge: export variables for use in git hooks
  (by Alexey Gladkov; closes: #23803).
- gear-sh-functions.in (is_ancestor_commit): rewriten in more reliable
  and efficient way; affects gear(1) and gear-update-tag(1).

* Thu Jul 08 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.1-alt1
- gear: reimplemented --commit option, so it no longer touches
  current branch and git index file.
- gear-rpm: added additional diagnostics about missing command
  (closes: #21892).
- gear-import (remove_suffix): added *.xz and *.txz suffixes.
- gear-update-tag: recognize and ignore "suffix=" tar's rules option.

* Mon Apr 12 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.0-alt1
- Bugfixes:
  + manpages: Quoted dash symbols in command and option names
    (closes: #22526).
- Improvements:
  + Documented git-config options (Alexey Froloff).
  + gear-update:
    - Implemented plugins support (Alexey Gladkov, Alexey Froloff).
    - Added rubygems support (Alexey Froloff).
    - Added tests (Alexey Froloff).
  + gear-import: New utility
    (Alexey Gladkov, Alexey Froloff; closes: #23320).

* Mon Oct 05 2009 Dmitry V. Levin <ldv@altlinux.org> 1.6.0-alt1
- Bugfixes:
  + gear-merge: Use quote_shell_args() from libshell (Alexey Gladkov).
  + gear-command-hasher: Use gear-command-tar.
  + gear-command-tar, gear-command-remote-build: Fixed tar --create.
  + gear --export-dir: Avoid creating useless output tarball.
  + gear: Remove original file after compression.
- Improvements:
  + gear: Enabled quoting support in rules syntax (Alexey Gladkov, me).
  + gear-rules.5.in: Added a note about special characters quoting support.
  + gear, gear-update-tag, gear-rules.5.in:
    Added and documented lzma/xz support.
  + gear-update: Read --exclude pattern defaults from git-config
    variable gear.update.exclude-pattern (Alexey Froloff).
  + gear: Use bold red color in the warning about unreverted
    temporary commit.
  + Added tests for basic gear rules.

* Fri Mar 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.3-alt1
- gear-create-tag: Fixed usage, added --time option (Alexey Gladkov).
- gear-srpmimport: Made --quiet mode more quiet.
- gear-srpmimport: Enhanced changelog name parser.
- gear-commit: Added --no-edit option (Alexey Gladkov).
- gear-remote: Fixed options order (Alexey Gladkov; closes: #19073).
- Added URL, updated %%description (closes: #18852).

* Wed Jan 28 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.2-alt1
- gear: make_compress(): Added keywords support in the name option (Alexey Gladkov).
- gear-update-tag: Added 'compress' directive (Alexey Gladkov; closes: #17624).
- gear-remote: Added --remote-repo (Alexey Gladkov; closes: #17865).
- gear: Fixed "diff" rule misbehavior (closes: ALT#17751).
- gear (get_tar_name, get_diff_name): Do check_path on modified path.
- gear-update-tag: chdir to toplevel directory (closes: ALT#18029).
- gear-commit: Unquote %%%% in changelog text.
- gear-srpmimport, gear-update: Use .gitattributes export-ignore
  instead of .gitignore to import empty directories.
- ABOUT.ru, QUICKSTART.ru: Converted from koi8r to utf8.

* Thu Oct 09 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.1-alt1
- gear-commit: Fix help message (Alexey Gladkov; closes: #16690).
- gear-changelog: Use git-config if GIT_AUTHOR_* is not set (Alexey Gladkov; closes: #16705).
- gear-update (Alexey Gladkov; closes: #17075):
  + Don't try to remove destdir in empty repository.
  + Remove temp directory before adding destdir into repository.
- gear-sh-functions.in (Alexey Froloff):
  + gear_config_option: New function, to use git config for option storage.
  + Fetch --verbose and --quiet options defaults from git config.
- gear-create-tag: Fetch --name and --message defaults from git config (Alexey Froloff).
- gear-changelog: Fetch releaser name and email defaults from git config (Alexey Froloff).
- gear: Fetch compress method and --rules options from git config (Alexey Froloff).
- Fixed signal handler exit code.
- gear-sh-functions.in (get_NVR_from_spec), gear-srpmimport:
  Allow and strip trailing whitespaces in name/version/release.
- gear: Implement keywords substitution in directory names.

* Fri Aug 01 2008 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- gear-changelog: New utility for preparing changelog records
  based on git commit messages (Alexey Gladkov).
- gear-update-tag: New --verify option (Alexey Froloff).
- gear-update: Add .gitignore file into empty directories like
  gear-srpmimport does (Alexey Gladkov).
- gear: New "compress" rule (Alexey Gladkov, me).
- Added bash-completion functions for gear utilities (Alexey Gladkov).
- gear-merge: Numerous changes (Alexey Froloff, Alexey Gladkov).
- Various manpage cleanups (me).

* Mon Mar 17 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt1
- Changes made by Alexey Gladkov:
  + gear-merge: New utility to merge branches.
  + gear-merge-rules(5): New man page which describes
    the .gear/merge file format.
  + gear --command: New option.
  + gear-command-hasher, gear-command-rpmbuild, gear-command-tar:
    New helpers.
  + gear-hsh, gear-rpm, gear-buildreq: New utilities which
    hopefully provide more convenient user interface than
    old --hasher and --rpmbuild options.
  + gear-command-remote-build: New helper.
  + gear-remote, gear-remote-hsh, gear-remote-rpm: New utilities.
  + gear-commit: Use getopt from libshell.
- My changes:
  + gear-create-tag: Fixed -u option support.
  + gear-srpmimport: Add empty .gitignore file to each empty directory.
  + Made readlink(1) usage secure.
  + gear-srpmimport: Added support for git-commit versions
    which do not handle --fast option.
  + Use shell-error, shell-quote and shell-args from libshell
    to replace several functions originally developed within
    hasher and gear projects.
  + Do not use dashed form of git commands.
  + gear: Implemented empty archive suffix support.
  + Renamed: *.ru_RU.KOI8-R -> *.ru.koi8
  + QUICKSTART.ru.koi8: Formatted for AsciiDoc.
  + ABOUT.ru.koi8: Imported thesis about gear from Protva2007
    in AsciiDoc format.
  + Packaged asciidoc-generated QUICKSTART.ru.html and ABOUT.ru.html files.
  + gear-update-tag: Added -q/--quiet and --no-clean options.
  + gear-update-tag: Changed --all option to imply --clean.
- Other minor fixes and cleanups, see git log for details.

* Fri Nov 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- gear-create-tag:
  + Enabled keyword substitution in --name and ----message options (ldv).
- gear-sh-functions.in (get_NVR_from_spec):
  + Added minimal support for RPM macros (vsu).

* Tue Oct 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- Added .gear directory support (ldv).
- Extended rules syntax: made whitespaces between directive
  and its parameters optional (legion, ldv).
- gear-create-tag (show_help): Fixed options output (ldv).
- gear (make_diff): Pass additional options to git-diff-tree,
  this change makes "diff" directive complete (ldv).
- Install gear-sh-functions without execute permissions set (ldv).
- gear-commit: Fixed unbound variable error (legion, #13057).
- gear-update: Added --create option (legion).
- gear-update: Added check for initial commit and
  for changed files in the index (legion, ldv).
- gear-hsh-build (raorn):
  + Honor "prefix" option from ~/.hasher/config.
  + Enhanced --repo handling.
  + exit_handler: Show path to hasher repo if build has failed.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.7-alt1
- gear-srpmimport: Pass --fast option to git-commit (ldv).
- gear-update: Added --all and --exclude options (legion).

* Wed Aug 29 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.6-alt1
- gear-update (legion):
  + Added cpio* types support.
  + Allowed update of top directory.
- gear:
  + Robustify --commit (ldv).
- gear, gear-srpmimport, gear-update:
  + Run grep in C locale, run sort in C collation (ldv).
- gear-create-tag:
  + New utility, creates a signed release tag object (legion, ldv).

* Sun May 20 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- gear-srpmimport:
  + Do not perform a noop merge (#11721).
  + Fixed import of archives with non-directory toplevel files.

* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.4-alt1
- gear-sh-functions.in (chdir_to_toplevel): New function.
- gear, gear-srpmimport, gear-update: Use chdir_to_toplevel().
- gear-commit: Chdir to toplevel directory early.

* Mon Mar 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Added gear-rules(5) man page which describes the .gear-rules
  file format (vsu).

* Sun Mar 11 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Changed "git-COMMAND" style commands to "git COMMAND" style.
- gear-update: Suppressed "git rm" output.
- gear-update, gear-update-tag: Separated "git COMMAND"
  command-line options from lists of files where appropriate.
- QUICKSTART.ru_RU.KOI8-R:
  + Reworded git config recommendations using "git config" commands.
  + Updated examples.

* Sun Mar 04 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- gear: Fixed suffix support (ldv, #11008).

* Wed Feb 28 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- gear-update: New utility, replaces gear-update-archive and
  gear-update-directory (legion, ldv).
- gear-upload: Move to separate package, girar-utils (ldv).
- gear: Chdir to toplevel directory early (ldv).
- gear-srpmimport (ldv):
  + Chdir to toplevel directory early.
  + If --quiet option given, do commit and merge quietly.
  + Rename --no-untar option to --no-unpack.
  + Rewrite archive importer:
    - Use file(1) to recognize file types
      instead of suffix-based switch.
    - Handle zip archives.
    - Support arbitrary archive names.
- QUICKSTART.ru_RU.KOI8-R: Mention ~/.gitconfig (azol).

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
