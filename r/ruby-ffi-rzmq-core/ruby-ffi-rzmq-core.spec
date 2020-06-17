%define        pkgname ffi-rzmq-core

Name:          ruby-%pkgname
Version:       1.0.7
Release:       alt2
Summary:       FFI wrapper for the ZeroMQ networking library
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)
Requires: libzeromq

%description
This gem provides only the FFI wrapper for the ZeroMQ (0mq) networking library.
Project can be used by any other zeromq gems that want to provide their own high-level Ruby API.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation


%description   doc
Documentation files for %gemname gem.

%prep
%setup
%patch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemsdocdir/*

%changelog
* Wed Feb 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.7-alt2
- fixed load libzmq.so.5
- add requires to libzeromq

* Thu Jan 30 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.7-alt1
- Initial build.
