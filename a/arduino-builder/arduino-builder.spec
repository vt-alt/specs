Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: gcc-c++ rpm-build-golang
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           arduino-builder
Version:        1.3.25
Release:        alt3_4
Summary:        A command line tool for compiling Arduino sketches
License:        GPLv2+
URL:            http://www.arduino.cc
Source0:        https://github.com/arduino/arduino-builder/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         fix-paths-to-ctags-avrdude.patch
#Patch2:         make-tools-flag-optional.patch

Requires:       arduino-ctags


BuildRequires:  gcc-common
BuildRequires:  golang >= 1.4.3
BuildRequires:  git

#ExcludeArch: aarch64

# BuildRequires:  golang(github.com/go-errors/errors)

# Needed for unit tests
# BuildRequires:  golang(github.com/stretchr/testify)
Source44: import.info
# These are not available, check will not be enabled
#BuildRequires:  golang(github.com/jstemmer/go-junit-report)
#BuildRequires:  golang(golang.org/x/codereview/patch)
#BuildRequires:  golang(golang.org/x/tools/cmd/vet)


%description
This tool is able to parse Arduino Hardware specifications, properly run
gcc and produce compiled sketches.
An Arduino sketch differs from a standard C program in that it misses a
main (provided by the Arduino core), function prototypes are not mandatory,
and libraries inclusion is automagic (you just have to #include them).
This tool generates function prototypes and gathers library paths,
providing gcc with all the needed -I params.

%prep
%setup -q
%patch1 -p1
# %%patch2 -p1

%build
# set up temporary build gopath, and put our directory there
mkdir -p ./_build
ln -s $(pwd)/src ./_build/

export GOPATH="$(pwd)/_build:%{go_path}:$(pwd)/vendor"
export GO111MODULE=off
# export GOFLAGS="-mod=vendor"

# Fix missing build-id
function gobuild { go build -a -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"; }
pushd src/arduino.cc/arduino-builder
gobuild
popd

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./src/arduino.cc/arduino-builder/arduino-builder %{buildroot}%{_bindir}/arduino-builder

install -d %{buildroot}%{_datadir}/arduino/hardware
install -p src/arduino.cc/builder/hardware/*.txt %{buildroot}%{_datadir}/arduino/hardware


# Check needs golang.org/x/ libraries that are not available
#%%check
#export GOPATH=$(pwd)/_build:%%{go_path}
#go test -v ./src/arduino.cc/builder/test/...


%files
%doc LICENSE.txt
%doc CONTRIBUTING.md README.md
%{_bindir}/arduino-builder
%{_datadir}/arduino/hardware

%changelog
* Thu May 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.3.25-alt3_4
- fixed build

* Fri Jul 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.25-alt2_4
- aarch64 build

* Thu Mar 14 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.25-alt2_1
- Use vendorized BuildRequires
- Add ExcludeArch aarch64

* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.25-alt1_1
- new version

