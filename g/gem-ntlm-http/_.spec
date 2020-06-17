# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname ntlm-http

Name:          gem-%pkgname
Version:       0.1.3.3
Release:       alt1
Summary:       Ruby/NTLM HTTP provides NTLM authentication over http
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pyu10055/ntlm-http
%vcs           https://github.com/pyu10055/ntlm-http.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.


%package       -n gem-pyu-%gemname
Version:       0.1.3.2
Summary:       %summary
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-pyu-%pkgname
%summary.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspecdir/%gemname-0.1.3.3.gemspec
%ruby_gemslibdir/%gemname-0.1.3.3

%files         -n gem-pyu-%gemname
%doc README*
%ruby_gemspecdir/pyu-%gemname-0.1.3.2.gemspec
%ruby_gemslibdir/pyu-%gemname-0.1.3.2


%changelog
* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.3.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
