%define _unpackaged_files_terminate_build 1
%define  pkgname puppetserver-ca-cli

Name:    ruby-%pkgname
Version: 1.4.0
Release: alt1

Summary: A simple Ruby CLI tool to interact with the Puppet Server's included CA
License: Apache-2.0
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/puppetserver-ca-cli

BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel

Requires: ruby-bundler


%description
This gem provides the functionality behind the Puppet Server CA interactions.
The actual CLI executable lives within the Puppet Server project.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc README* LICENSE
%ruby_sitelibdir/*
%rubygem_specdir/*

%exclude %_bindir/*


%changelog
* Mon Aug 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.0-alt1
- Version updated to 1.4.0

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt2
- ca and puppet paths fixed

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt1
- Version updated to 1.3.1

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt1
- Version updated to 1.2.1

* Thu Dec 06 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus
