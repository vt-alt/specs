Name: libcontrol++
Version: 0.24.1
Release: alt1

Summary: control++ common classes and functions library
License: GPLv3
Group: Development/C++
Url: https://www.altlinux.org/Control++

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=libcontrolplusplus.git
Source: %{name}-%{version}.tar

BuildRequires: gcc-c++
BuildRequires: libacl-devel

%description
libcontrol++ provides useful classes and functions, that can be used
not only in control++ but in other applications as well.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n %{name}-devel
Summary: %{name} headers
Group: Development/Other
Requires: %{name}
Requires: libacl-devel
BuildArch: noarch

%description -n %{name}-devel
Development package for %{name}.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build
%make_build

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
# Executables
cp bin/%{name}.so %{buildroot}%{_libdir}
# Includes
cp src/*.h %{buildroot}%{_includedir}/%{name}

%files
%{_libdir}/*.so

%files -n %{name}-devel
%{_includedir}/%{name}/

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Wed Jul 15 2020 Alexey Appolonov <alexey@altlinux.org> 0.24.1-alt1
- Corrected functions 'StripPath' and 'GetWordFromLine';
- Corrected behaviour of 'TPrinter' class in case when winsize cannot be
  properly defined.

* Sat Nov 23 2019 Alexey Appolonov <alexey@altlinux.org> 0.24.0-alt1
- Some of the classes and functions have been relocated, some of the headers
  are gone and the new headers have been added;
- Enhanced trimming functions;
- Minor improvement of TPrinter.

* Wed Sep 18 2019 Alexey Appolonov <alexey@altlinux.org> 0.23.0-alt1
- New abilities of TPrinter (switching off any activity of TPrinter object,
  restoring 'silent' flag).

* Sat Aug 24 2019 Alexey Appolonov <alexey@altlinux.org> 0.22.0-alt1
- Ability to store only the pointer to TFileMode attributes, and not copy
  the data (performance gain up to 100%%);
- New abilities of TPrinter (printing various special messages,
  handling indentation levels, etc.);
- All the printing inside TPrinter is done through one and only point
  of 'cout'-reference;
- Small fixes and optimizations.

* Tue Apr 23 2019 Alexey Appolonov <alexey@altlinux.org> 0.21.0-alt1
- Enhanced TConf class;
- Ability to give instant feedback for an operation.

* Mon Mar 11 2019 Alexey Appolonov <alexey@altlinux.org> 0.20.0-alt1
- Ability to get string with current permission status for applied mode;
- Improved performance.

* Wed Mar 06 2019 Alexey Appolonov <alexey@altlinux.org> 0.19.0-alt1
- Fix of the FormatFilePath function;
- Default mode for whitelists is 'neutral' mode;
- Custom mode for whitelists is allowed again.

* Mon Mar 04 2019 Alexey Appolonov <alexey@altlinux.org> 0.18.0-alt1
- Handling SUID, GUID and Sticky bits;
- Escaping and unescaping special symbols when writing to
  or reading from ini-file;
- Ability to sort lines of file in alphabetical order;
- Custom mode for whitelists is disallowed.

* Mon Dec 10 2018 Alexey Appolonov <alexey@altlinux.org> 0.17.1-alt1
- Simple line (not "left part - tie symbols - right part" structure)
  can be printed with LineEnd method of TPrinter.

* Fri Nov 30 2018 Alexey Appolonov <alexey@altlinux.org> 0.17.0-alt1
- Ability to check controversy between the permission modes;
- Ability to get all names of variables of the ini-file section;
- New interface of the GetUserId and GetGroupId functions;
- Fixed determination of the 'blacklist' section of the permissions
  description file;
- List section of the permissions description file is any kind of list
  not just 'list';
- Sections 'blacklist' & 'whitelist' of the permissions description file
  are considered recursive type.

* Sun Nov 18 2018 Alexey Appolonov <alexey@altlinux.org> 0.16.0-alt1
- TFileMode as common interface for TFilePerm and TFileACL classes;
- TGroupOfFilesMode for handling params of a group of files;
- TSectorType for determining and storing sector types of a mode description;
- Ability to check if file is a dir.

* Sun Nov 11 2018 Alexey Appolonov <alexey@altlinux.org> 0.15.2-alt1
- Fix of the checks made during access to the TRunMode flags;
- Enhanced constructor of the TFilePerm and TFileACL.

* Tue Nov 06 2018 Alexey Appolonov <alexey@altlinux.org> 0.15.1-alt1
- Fixed JoinFilePaths function;
- Duplicate definition of the member variable is removed
  from TGroupOfFilesACL class.

* Sat Oct 27 2018 Alexey Appolonov <alexey@altlinux.org> 0.15.0-alt1
- Functions for searching through file paths;
- Ability to get user/group/other part of the file mode;
- Yes/No dialog;
- Function for comparison of the permission modes;
- Functions for verification of the file's owner/group;
- New section of the project for basic operations with file permissions;
- Ability to restart the print line;
- Class for the variable that can be assigned only once;
- Class for the set of params of a running program;
- Modified FormatFilePath and DirEnding func;
- Function for joining file paths;
- Function for rebasing file paths;
- Ability to set "base directory" for the permission mode;
- Way of determining the neutral mode;
- Ability to use pointer to a struct of params instead of the strings
  for the permission mode;
- Ability to limit the memory step when using PushBack function.

* Sat Oct 13 2018 Alexey Appolonov <alexey@altlinux.org> 0.14.0-alt1
- Writting error messages by the ref instead of outputting;
- More secure way of TFilePerm data access and modification;
- New classes TFileACL and TGroupOfFilesACL;
- Ability to check permission/ACL completeness;
- Set of ACL-related functions;
- Function that forms TFilePerm object for a file;
- Functions to get user id/name and group id/name;
- Modified TPrinter class;
- Modified conf-related classes;
- New common functions - CompareFilenames, Subvector and RemoveEmptyElements;
- Text-processing functions are grouped into the 'text' section;
- Sets-related functions are grouped into the 'sets' section.

* Sun Sep 30 2018 Alexey Appolonov <alexey@altlinux.org> 0.13.0-alt1
- New section for printing functionality;
- API changes (CutExtension, FormatFilePath and GetHomeDir functions);
- Ability to get feedback while changing permissions;
- Function that gets the intersection of two vectors;
- Function that gets vector that consist of elements of first given vector
  that are not presented in the second given vector;
- Function that gets sector of the conf by given name;
- Ability to clean DOM of the TConf object;
- Ability to add message at the top when rewriting conf;
- Various small modifications.

* Mon Sep 10 2018 Alexey Appolonov <alexey@altlinux.org> 0.12.0-alt1
- New section for the filestat-related functions;
- Function for opening the dir and performing the operation inside of it;
- Ability to call the function for the dir or all the files of the dir;
- Ability to add new assgn to the conf DOM and to the conf file;
- Ability to rewrite conf file completely according to DOM;
- Functions for checking/cutting an extension of a filename;
- Function for forming vector of names of all the sectors of the conf file;
- Function for determining special reference dirs;
- Function for converting string to lowercase;
- Lots of small fixes and improvements.

* Fri Jul 27 2018 Alexey Appolonov <alexey@altlinux.org> 0.11.0-alt1
- Introducing refs and const modifier wherever possible;
- Functions for trimming the string;
- Function to access the last element of the conf DOM;
- Attempt to write an empty string to a file not considered as an error;
- Explicit templates instances and unused typedefs was removed.

* Sat Jun 09 2018 Alexey Appolonov <alexey@altlinux.org> 0.10.0-alt1
- Revised PrintOnEntireLine function.

* Sat Jun 09 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.1-alt2
- libcontrol++ is a separate package now.

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
