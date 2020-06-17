%define        pkgname timecop

Name:          ruby-%pkgname
Version:       0.9.1
Release:       alt1
Summary:       A gem providing "time travel" and "time freezing" capabilities
Group:         Development/Ruby
License:       BSD
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/travisjeffery/timecop
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)
BuildRequires: gem(rake)

%description
A gem providing "time travel" and "time freezing" capabilities,
making it dead simple to test time-dependent code.
It provides a unified method to mock Time.now, Date.today, and DateTime.now in a single call.

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
* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.1-alt1
- Initial build.
