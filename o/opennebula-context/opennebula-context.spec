
Name: opennebula-context
Summary: OpenNebula Contextualization Package
Version: 5.10.0
Release: alt1
License: Apache
Group: System/Servers
Url: http://opennebula.org
# https://github.com/OpenNebula/addon-context-linux.git
Source0: %name-%version.tar
BuildArch: noarch

Provides: one-context = %EVR
Conflicts: cloud-init udev-rule-generator-net udev-rule-generator-cdrom

Requires: util-linux bind-utils cloud-utils-growpart parted
Requires: ruby ruby-json-pure
Requires: qemu-guest-agent
Requires: sudo

%filter_from_requires \,/etc/rc\.d/growfs,d

BuildRequires(pre): rpm-build-ruby

%description
This package prepares a VM image for OpenNebula:
  * Disables udev net and cd persistent rules
  * Deletes udev net and cd persistent rules
  * Unconfigures the network
  * Adds OpenNebula contextualization scripts to startup
    * Configure network
    * Configure dns (from DNS and ETH*_DNS context variables)
    * Set root authorized keys (from SSH_PUBLIC_KEY and EC2_PUBLIC_KEY)
  * Add onegate tool (NEEDS RUBY AND JSON GEM TO WORK)
  * Resize root filesystem
  * Generate host ssh keys in debian distributions

To get support check the OpenNebula web page:
  http://OpenNebula.org

%prep
%setup

%build
%install

install -p -D -m 755 src/etc/one-context.d/loc-05-grow-rootfs \
			%buildroot%_sysconfdir/one-context.d/loc-05-grow-rootfs
install -p -D -m 755 src/etc/one-context.d/loc-09-timezone \
			%buildroot%_sysconfdir/one-context.d/loc-09-timezone
install -p -D -m 755 src/etc/one-context.d/loc-10-network##arch.one \
			%buildroot%_sysconfdir/one-context.d/loc-10-network
install -p -D -m 755 src/etc/one-context.d/loc-10-network-pci##one \
			%buildroot%_sysconfdir/one-context.d/loc-10-network-pci
#install -p -D -m 755 src/etc/one-context.d/loc-11-dns##one \
#			%buildroot%_sysconfdir/one-context.d/loc-11-dns
install -p -D -m 755 src/etc/one-context.d/loc-12-firewall##apk \
            %buildroot%_sysconfdir/one-context.d/loc-12-firewall
install -p -D -m 755 src/etc/one-context.d/loc-14-mount-swap##one \
			%buildroot%_sysconfdir/one-context.d/loc-14-mount-swap
install -p -D -m 755 src/etc/one-context.d/loc-15-ip_forward##apk \
            %buildroot%_sysconfdir/one-context.d/loc-15-ip_forward
install -p -D -m 755 src/etc/one-context.d/loc-15-keepalived##apk \
            %buildroot%_sysconfdir/one-context.d/loc-15-keepalived
install -p -D -m 755 src/etc/one-context.d/loc-16-gen-env \
			%buildroot%_sysconfdir/one-context.d/loc-16-gen-env
install -p -D -m 755 src/etc/one-context.d/loc-20-set-username-password \
			%buildroot%_sysconfdir/one-context.d/loc-20-set-username-password
install -p -D -m 755 src/etc/one-context.d/loc-22-ssh_public_key \
			%buildroot%_sysconfdir/one-context.d/loc-22-ssh_public_key
install -p -D -m 755 src/etc/one-context.d/loc-30-console##one \
			%buildroot%_sysconfdir/one-context.d/loc-30-console
install -p -D -m 755 src/etc/one-context.d/loc-35-securetty \
			%buildroot%_sysconfdir/one-context.d/loc-35-securetty
install -p -D -m 755 src/etc/one-context.d/net-15-hostname \
			%buildroot%_sysconfdir/one-context.d/net-15-hostname
install -p -D -m 755 src/etc/one-context.d/net-97-start-script \
			%buildroot%_sysconfdir/one-context.d/net-97-start-script
install -p -D -m 755 src/etc/one-context.d/net-98-execute-scripts \
			%buildroot%_sysconfdir/one-context.d/net-98-execute-scripts
install -p -D -m 755 src/etc/one-context.d/net-99-report-ready \
			%buildroot%_sysconfdir/one-context.d/net-99-report-ready

install -p -D -m 755 src/usr/bin/onegate %buildroot%_bindir/onegate
install -p -D -m 755 src/usr/bin/onegate.rb %buildroot%_bindir/onegate.rb
install -p -D -m 755 src/usr/sbin/one-context-run##one %buildroot%_sbindir/one-context-run
install -p -D -m 755 src/usr/sbin/one-contextd %buildroot%_sbindir/one-contextd

install -p -D -m 644 src/lib/udev/rules.d/65-context.rules##rpm.systemd.one \
			%buildroot%_udevrulesdir/65-context.rules

install -p -D -m 644 src/usr/lib/systemd/system/one-context-local.service##rpm.systemd.one \
			%buildroot%_unitdir/one-context-local.service
install -p -D -m 644 src/usr/lib/systemd/system/one-context-reconfigure-delayed.service##systemd.one \
			%buildroot%_unitdir/one-context-reconfigure-delayed.service
install -p -D -m 644 src/usr/lib/systemd/system/one-context-reconfigure.service##systemd.one \
			%buildroot%_unitdir/one-context-reconfigure.service
install -p -D -m 644 src/usr/lib/systemd/system/one-context.service##alt.one \
			%buildroot%_unitdir/one-context.service


%post
# Reload udev rules
udevadm control --reload >/dev/null 2>&1 || :

# Register service
systemctl enable one-context-local.service
systemctl enable one-context.service

%preun
systemctl --no-reload disable one-context-local.service one-context.service >/dev/null 2>&1 || :
systemctl daemon-reload >/dev/null 2>&1 || :

%files
%_bindir/*
%_sbindir/*
%config %_sysconfdir/one-context.d/*
%_udevrulesdir/*
%_unitdir/*

%changelog
* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 5.10.0-alt1
- 5.10.0

* Mon Aug 19 2019 Mikhail Gordeev <obirvalger@altlinux.org> 5.8.0-alt1
- 5.8.0

* Tue Nov 27 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt4
- fixed generate network config for systemd-networkd

* Tue Nov 27 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt3
- update systemd units

* Thu Nov 22 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt2
- update one-context.service

* Mon Oct 01 2018 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt1
- 5.6.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.4.2.1-alt1
- Rebuild with new Ruby autorequirements.
- Do not require open-vm-tools for aarch64.

* Tue Apr 10 2018 Alexey Shabalin <shaba@altlinux.ru> 5.4.2.1-alt1
- 5.4.2.1

* Thu Sep 28 2017 Alexey Shabalin <shaba@altlinux.ru> 5.4.1-alt1
- Initial build
