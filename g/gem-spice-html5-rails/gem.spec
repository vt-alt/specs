%define        pkgname spice-html5-rails

Name:          gem-%pkgname
Version:       0.1.5
Release:       alt1
Summary:       Spice HTML5 client packed for Rails application
License:       LGPLv3
Group:         Development/Ruby
Url:           https://www.spice-space.org/
%vcs           
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
The SPICE project aims to provide a complete open source solution for remote
access to virtual machines in a seamless way so you can play videos, record
audio, share usb devices and share folders without complications.

SPICE could be divided into 4 different components: Protocol, Client, Server
and Guest. The protocol is the specification in the communication of the three
other components; A client such as remote-viewer is responsible to send data
and translate the data from the Virtual Machine (VM) so you can interact with
it; The SPICE server is the library used by the hypervisor in order to share
the VM under SPICE protocol; And finally, the Guest side is all the software
that must be running in the VM in order to make SPICE fully functional, such as
the QXL driver and SPICE VDAgent.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
