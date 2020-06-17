%define        pkgname ffi-rzmq

Name:          ruby-%pkgname
Version:       2.0.7
Release:       alt1
Summary:       Wraps the ZeroMQ networking library using Ruby FFI
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)
BuildRequires: gem(ffi-rzmq-core) >= 1.0.7

%description
This gem wraps the ZeroMQ networking library using the ruby FFI (foreign
function interface). It's a pure ruby wrapper so this gem can be loaded
and run by any ruby runtime that supports FFI.
That's all of the major ones - MRI, Rubinius and JRuby.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation

%description   doc
Documentation files for %gemname gem.

%prep
%setup

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
* Thu Jan 30 2020 Alexey Shabalin <shaba@altlinux.org> 2.0.7-alt1
- Initial build.
