Name: xfce-reduced-resource
Version: 0.2
Release: alt1
Summary: Disable compositing and graphical effects for xfce
License: GPL
Group: Graphical desktop/XFce

BuildArch: noarch

%description
%summary

%install
mkdir -p %buildroot%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml

cat > %buildroot%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>

<channel name="xfwm4" version="1.0">
  <property name="general" type="empty">
    <property name="box_move" type="bool" value="true"/>
    <property name="box_resize" type="bool" value="true"/>
    <property name="use_compositing" type="bool" value="false"/>
  </property>
</channel>
EOF

%files
%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml

%changelog
* Thu Dec 26 2019 Ivan A. Melnikov <iv@altlinux.org> 0.2-alt1
- Hide window contents when moving or resizing

* Thu Sep 19 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT
