%define        pkgname rqrcode_core

Name:          ruby-%pkgname
Version:       0.1.1
Release:       alt1
Summary:       A library to encode QR Codes
Group:         Development/Ruby
License:       MIT
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)

%description
rqrcode_core is a Ruby library for encoding QR Codes.
The simple interface (with no runtime dependencies)
allows you to create QR Code data structures.

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
* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 0.1.1-alt1
- Initial build.
