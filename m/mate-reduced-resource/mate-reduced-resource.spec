Name: mate-reduced-resource
Version: 0.1
Release: alt1
Summary: Disable compositing and graphical effects for mate
License: GPL
Group: Graphical desktop/MATE

BuildArch: noarch

Requires(post): dconf
Requires(postun): dconf

%description
%summary

%install
mkdir -p %buildroot%_sysconfdir/dconf/profile

cat > %buildroot%_sysconfdir/dconf/profile/user <<EOF
user-db:user
system-db:local
EOF

mkdir -p %buildroot%_sysconfdir/dconf/db/local.d

cat > %buildroot%_sysconfdir/dconf/db/local.d/01-mate-reduced-resources <<EOF
[org/mate/marco/general]
reduced-resources=true
compositing-manager=false
EOF

%post
dconf update

%postun
dconf update

%files
%_sysconfdir/dconf/profile/user
%_sysconfdir/dconf/db/local.d/01-mate-reduced-resources

%changelog
* Thu Sep 19 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT
