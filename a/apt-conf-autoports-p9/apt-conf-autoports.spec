%define destbranch p9
Name: apt-conf-autoports-%{destbranch}
Summary(ru_RU.UTF-8): Настройки для использования пакетов из репозитория Autoports/%{destbranch}
Summary: Autoports repository for %{destbranch}
Version: 9.0
Release: alt1

Conflicts: apt-conf-autoports < 2.0
Obsoletes: apt-conf-autoports < 2.0
Conflicts: apt-conf-autoports-p7 < 8.0
Obsoletes: apt-conf-autoports-p7 < 8.0
Conflicts: apt-conf-autoports-p8 < 9.0
Obsoletes: apt-conf-autoports-p8 < 9.0
Provides: apt-conf-autoports = %version

URL: http://www.altlinux.org/Autoports
License: GPL
Group: System/Base

#Requires: apt-rsync

%description
%{summary}.
To update packages from %{summary},
uncomment /apt/sources.list.d/autoports.list, update the packages you want
and comment /apt/sources.list.d/autoports.list back to prevent accidental
dist-upgrade.

%description -l ru_RU.UTF-8
Autoports - это постоянно обновляемый репозиторий свежих версий пакетов из Sisyphus,
которые автоматически пересобраны для установки в текущую стабильную ветвь.

Репозиторий Autoports предназначен для точечных обновлений.
Autoports дает возможность попробовать какой-нибудь пакет,
собранный для сизифа без полного перехода на репозиторий Sisyphus.

СтОит попробовать новый пакет из Autoports, только если в бранче такого пакета
нет или имеющийся не устраивает вас функциональностью или наличием ошибок.
Репозиторий Autoports обновляется роботом, который пытается в автоматическом режиме
собирать пакеты из репозитория Sisyphus в окружении текущего бранча. Как следствие,
пакеты из Autoports не тестируются.

Поэтому будьте готовы к тому, что не все пакеты могут оказаться рабочими.
В случае каких-либо проблем, просто уделите пакет, взятый из Autoports,
и замените его старым пакетом из бранча. Пакеты из Autoports легко узнать благодаря
характерному суффиксу вида .A90.1 (для p9), .A60.1 (для t6) или .A51.1 (для 5.1).

%install
mkdir -p %buildroot%_sysconfdir/apt/{sources,vendors}.list.d
cat > %buildroot%_sysconfdir/apt/vendors.list.d/autoports-%{destbranch}.list <<'EOF'
simple-key "cronbuild" {
	Fingerprint "DE73F3444C163CCD751AC483B584C633278EB305";
	Name "Cronbuild Service <cronbuild@altlinux.org>";
}
simple-key "cronport" {
	Fingerprint "F3DBF34AB0CC0CE638DF7D509F61FBE7E2C322D8";
	Name "Cronport Service <cronport@altlinux.org>";
}
EOF
cat > %buildroot%_sysconfdir/apt/sources.list.d/autoports-%{destbranch}.list <<'EOF'
# Do not forget to comment back the lines after package installation,
# or later you will install unwanted and untested packages during upgrade!
#
#rpm [cronbuild] http://autoports.altlinux.org/pub/ALTLinux/autoports/%{destbranch}/ noarch autoports
#rpm [cronbuild] http://autoports.altlinux.org/pub/ALTLinux/autoports/%{destbranch}/ %{_arch} autoports
EOF

%files
%config %_sysconfdir/apt/vendors.list.d/autoports-%{destbranch}.list
%config %_sysconfdir/apt/sources.list.d/autoports-%{destbranch}.list

%changelog
* Thu May 23 2019 Igor Vlasenko <viy@altlinux.ru> 9.0-alt1
- p9 build

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 8.0-alt0.M80P.1
- p8 build

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0.M70P.1
- p7 build
