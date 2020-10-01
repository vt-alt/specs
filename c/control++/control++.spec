%define libcontrolppver 0.24
%define confdir %{_sysconfdir}/%{name}
%define statedir %{_localstatedir}/%{name}
%define ulim_statedir %{statedir}/ulimits
%define perm_statedir %{statedir}/permissions
%define testsdir %{statedir}/tests

Name: control++
Version: 0.20.3
Release: alt1.M90P.1

Summary: System configuration tool
License: GPLv3
Group: System/Configuration/Other
Url: https://www.altlinux.org/Control++

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=controlplusplus.git
Source: %{name}-%{version}.tar

BuildRequires: gcc-c++
BuildRequires: libcontrol++-devel >= %{libcontrolppver}

Requires: libcontrol++
# Fulfilling a requirement of a testing routine used for a particular distro
Requires: %{name}-wl

%description
%{name} is a simple system configuration tool that allows administrator
to change system ulimits, set permission modes and, in perspective,
perform other administrative operations.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n %{name}-wl
Summary: Files that can help to configure whitelist permission mode
Group: System/Configuration/Other

Requires(pre): %{name}

%description -n %{name}-wl
Files that can help to configure whitelist permission mode:
1) A sample of a permission mode with an extensive real-life 'whitelist'
section;
2) A shell script that can generate a list of all executable files of the host
system (to be used with the sample described above).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n %{name}-checkinstall
Summary: Tests and test data for %{name}
Group: Other

Requires(pre): %{name}
Requires: python3
Requires: python3-module-ax

%description -n %{name}-checkinstall
Tests and test data for %{name}.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{confdir}
mkdir -p %{buildroot}%{ulim_statedir}
mkdir -p %{buildroot}%{perm_statedir}
mkdir -p %{buildroot}%{testsdir}
mkdir -p %{buildroot}/run/%{name}
# Executables
cp bin/%{name} %{buildroot}%{_bindir}
# Configuration
cp -r samples/* %{buildroot}%{confdir}
# Documentation
cp COPYING %{buildroot}%{_defaultdocdir}/%{name}
cp usage.txt %{buildroot}%{_defaultdocdir}/%{name}
cp readme.txt %{buildroot}%{_defaultdocdir}/%{name}
# Tests
cp -r tests/* %{buildroot}%{testsdir}

%post -n %{name}-checkinstall
%{testsdir}/run --targets all

%files
%{_bindir}/%{name}
%{confdir}
%exclude %{confdir}/wl.sh
%exclude %{confdir}/permissions/wl
%config(noreplace) %{confdir}/%{name}.conf
%dir %{statedir}
%dir %{ulim_statedir}
%dir %{perm_statedir}
%{_defaultdocdir}/%{name}

%files -n %{name}-wl
%{confdir}/wl.sh
%{confdir}/permissions/wl

%files -n %{name}-checkinstall
%{testsdir}/*
%dir /run/%{name}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Thu Sep 24 2020 Alexey Appolonov <alexey@altlinux.org> 0.20.3-alt1.M90P.1
- Port of a new release.

* Thu Sep 24 2020 Alexey Appolonov <alexey@altlinux.org> 0.20.3-alt2
- New bin package 'control++-wl' that contains files that can help to configure
  whitelist permission mode.

* Wed Sep 09 2020 Alexey Appolonov <alexey@altlinux.org> 0.20.3-alt0.M90P.1
- Port of a new version.

* Tue Sep 08 2020 Alexey Appolonov <alexey@altlinux.org> 0.20.3-alt1
- Modified testing procedures that reduce traces of them been running.

* Fri Sep 04 2020 Alexey Appolonov <alexey@altlinux.org> 0.20.2-alt1
- Polished tests.

* Fri Jul 31 2020 Alexey Appolonov <alexey@altlinux.org> 0.19.0-alt1.M90P.1
- Build for all main CPU architectures.

* Sun Nov 24 2019 Alexey Appolonov <alexey@altlinux.org> 0.20.1-alt1
- Corrected flow of printing procedures;
- Tests for a black/white lists mode settings.

* Sat Aug 24 2019 Alexey Appolonov <alexey@altlinux.org> 0.20.0-alt1
- Recursive formation of the modes for directories is optimized
  (performance gain up to 100%%);
- Most of the printing is done with the use of new and previously existed
  abilities of TPrinter class.

* Wed Jul 24 2019 Alexey Appolonov <alexey@altlinux.org> 0.19.0-alt2
- Enhanced manual.

* Tue Apr 23 2019 Alexey Appolonov <alexey@altlinux.org> 0.19.0-alt1
- Ability to perform exclusive mode setting for a unit ('micro mode');
- Ability to check compliance of micro modes;
- Fix of flaw that was manifested during setting of empty permission mode;
- More feedback with 'verbose' option.

* Fri Apr 05 2019 Alexey Appolonov <alexey@altlinux.org> 0.18.1-alt1
- Bug fixes.

* Mon Mar 11 2019 Alexey Appolonov <alexey@altlinux.org> 0.18.0-alt1
- Verbose output option;
- Bug fixes.

* Wed Mar 06 2019 Alexey Appolonov <alexey@altlinux.org> 0.17.0-alt2
- Enhanced manual.

* Wed Mar 06 2019 Alexey Appolonov <alexey@altlinux.org> 0.17.0-alt1
- File links are ignored during recursive mode setting for dirs
  (hence links that are not in the whitelist ignored as well).

* Mon Mar 04 2019 Alexey Appolonov <alexey@altlinux.org> 0.16.0-alt1
- Ability to add comments into lists of files for the permission unit;
- Fixed determination of disallowed essential applications;
- Silent termination in case user chose to abort mode setting;
- Reduced number of warning/error messages displayed on every access error.

* Mon Dec 03 2018 Alexey Appolonov <alexey@altlinux.org> 0.15.0-alt1
- Mode reset is marked by cleared internal configuration file;
- 'mode for dirs' is applicable for all directories, not nested only;
- Attempt to set neutral mode is not qualified as error;
- Fix of the segmentation violation;
- New samples.

* Fri Nov 30 2018 Alexey Appolonov <alexey@altlinux.org> 0.14.0-alt1
- Ability to recursively process listed files ('list_r', 'whitelist' and
  'blacklist' sections) by the permissions unit;
- Ability to alter the order of execution of the units;
- Much more efficient version of UniquifyModes function;
- Memory leakages as well as some segmentation fault errors are eliminated.

* Sun Nov 18 2018 Alexey Appolonov <alexey@altlinux.org> 0.13.0-alt1
- Rewritten permissions unit - there is no separation between handling the ACLs
  or regular permission modes, sector types of the mode description determined
  once and then can be accesed at ease, code became simpler to understand
  and to modify.

* Sun Nov 11 2018 Alexey Appolonov <alexey@altlinux.org> 0.12.2-alt1
- The mode of the top level dir will not be left unchanged during mode setting 
  for the 'dir' section;
- Another fix of the UniquifyPermsOrACLs function;
- Detection of non-unique permission modes is enabled by default.

* Tue Nov 06 2018 Alexey Appolonov <alexey@altlinux.org> 0.12.1-alt1
- Only regular files, symlinks and directories are processed
  for the 'dir'/'dir_r' permission mode setting;
- Mode saving is aborted if mode name cannot be found among names
  of the available modes;
- Fixed UniquifyPermsOrACLs function;
- Extended manual.

* Sun Oct 28 2018 Alexey Appolonov <alexey@altlinux.org> 0.12.0-alt1
- Ability to exclude paths from mode setting;
- Ability to check uniqueness of the given permission modes;
- Handling the controversy between internal and external configs;
- Not printing current submodes if main mode isn't set;
- Using Yes/No dialog function of the libcontrol++;
- Not restoring the state if current mode is unknown;
- Ability to state 'base dir' for the 'list' permission;
- Optimized 'whitelist' permission mode setting.

* Mon Oct 15 2018 Alexey Appolonov <alexey@altlinux.org> 0.11.0-alt1
- Pass setting/checking mode for non existent files;
- It's OK to not have 'reset' file if current mode is not stated;
- Terminating if main or internal conf are not accessible;
- Generated files are stored in /var/lib/control++;
- New functionality of the libcontrol++ TPrinter;
- Adjusted dialogs.

* Mon Oct 1 2018 Alexey Appolonov <alexey@altlinux.org> 0.10.0-alt1
- Units can have many config files;
- Determining available modes by the units themselves;
- Ability to not specify some of the submodes;
- Ability to state '*' bit (that means don't change) in permission mode
  or as owner or group, not stated owner/group is '*' owner/group;
- Ability to change mode for all files of the dir, ability to state different
  modes for nested dirs, ability to change mode for the dir recursively;
- Implementation of the black/white list concept;
- Every unit can reset it's mode (restore the state that held before
  the current mode was set);
- Every unit must reset the current mode before setting up the new one;
- Every unit can check current mode compliance;
- Storing current mode and all the submodes in the internal configuration file
  used for compliance-checking;
- Starter unit is running 'do' file when setting up a mode;
- There is no default mode anymore;
- Term 'corrupted mode' is discarded;
- Proper feedback by all units;
- Delegating some of the functions and classes to the libcontol++;
- Russian manual.

* Wed Aug 08 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.2-alt2
- libcontrol++ is a separate package now.

* Wed Aug 08 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.2-alt1
- Fix of the "starter" unit;
- Excluding aarch64.

* Sat Jun 02 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.1-alt1
- Memory leakage fix.

* Mon May 21 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.0-alt1
- New libcontrol++ features.

* Fri Mar 16 2018 Alexey Appolonov <alexey@altlinux.org> 0.8.0-alt1
- New libcontrol++ features.

* Mon Feb 26 2018 Alexey Appolonov <alexey@altlinux.org> 0.7.0-alt1
- New libcontrol++ features.

* Wed Feb 14 2018 Alexey Appolonov <alexey@altlinux.org> 0.6.0-alt1
- Common classes and functions that can be used in other projects
  compiled as libcontrol++.so
  therefore libcontrol++ and libcontrol++-devel subpackages.

* Fri Jan 26 2018 Alexey Appolonov <alexey@altlinux.org> 0.5.1-alt1
- Code restyling.
- Minor changes in units handling.

* Mon Dec 11 2017 Alexey Appolonov <alexey@altlinux.org> 0.5.0-alt1
- New unit, that runs script stated in configuration file.

* Mon Dec 4 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.2-alt1
- Handling of values in quotes in configuration files.
- Verbose output with -v param when setting mode.

* Thu Nov 30 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.1-alt1
- Comment lines passing in configuration files.

* Thu Nov 30 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.0-alt1
- Ability to set permission modes.

* Mon Nov 27 2017 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- Restructure for better extensibility.

* Mon Nov 27 2017 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Support of INI file format for the configuration file. 

* Fri Nov 17 2017 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial ALT Linux release.
