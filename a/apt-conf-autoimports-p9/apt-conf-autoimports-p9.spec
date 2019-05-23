%define destbranch p9
Name: apt-conf-autoimports-%destbranch
Summary(ru_RU.UTF-8): Настройки для использования пакетов из репозитория Autoimports/%{destbranch}
Summary: Autoimports repository for %{destbranch}
Version: 1.0
Release: alt1

# branches conflicts with p9
Conflicts: apt-conf-autoimports-p7
Conflicts: apt-conf-autoimports-t7
Conflicts: apt-conf-autoimports-p8
Conflicts: apt-conf-autoimports-p10
Conflicts: apt-conf-autoimports-sisyphus

Requires: apt-rsync

URL: http://www.altlinux.org/Autoimports/%{destbranch}
License: GPL
Group: System/Base

%description
%{summary} contains a lot of automatically maintained packages that
are not presented in the main %{destbranch} repository.
Note that the packages are generally not tested before publishing
in the Autoimports repository. Please, report found bugs to Bugzilla
to help make Autoimports repository better.

%description -l ru_RU.UTF-8
Autoimports - это семейство дополнительных репозиториев пакетов
для платформы Sisyphus и стабильных бранчей.

Репозиторий Autoimports/Sisyphus - это постоянно обновляемый репозиторий
пакетов, собранных под бинарную платформу Sisyphus, дополняющий
основной репозиторий Sisyphus/classic.

Пакеты из репозиториев Autoimports отличаются от пакетов в основном
репозитории тем, что они получены с помощью систем автоматической
сборки пакетов, а также из-за нехватки тестеров и майнтайнеров
не были достаточно протестированы перед попаданием в Autoimports.
Вместо этого обязанность тестирования пакетов из репозиториев
Autoimports возложена на пользователей.

Если вы заметили в пакете из Autoimports ошибку, сообщите, пожалуйста,
об этом в bugzilla.altlinux.org, зарегистрировав ошибку
на product=Autoimports (%{destbranch}),
указав имя пакета, версию-релиз и подробности ошибки.

Open Source модель подразумевает ваше личное участие в создании вашего
дистрибутива. Помогите сделать репозиторий качественнее и надежнее
для вех пользователей!

%install
mkdir -p %buildroot%_sysconfdir/apt/{sources,vendors}.list.d
cat > %buildroot%_sysconfdir/apt/vendors.list.d/autoimports-%{destbranch}.list <<'EOF'
simple-key "cronbuild" {
	Fingerprint "DE73F3444C163CCD751AC483B584C633278EB305";
	Name "Cronbuild Service <cronbuild@altlinux.org>";
}
simple-key "cronport" {
	Fingerprint "F3DBF34AB0CC0CE638DF7D509F61FBE7E2C322D8";
	Name "Cronport Service <cronport@altlinux.org>";
}
EOF
cat > %buildroot%_sysconfdir/apt/sources.list.d/autoimports-%{destbranch}.list <<'EOF'
#rpm [cronbuild] ftp://ftp.altlinux.ru/pub/distributions/ALTLinux/autoimports/%{destbranch}/ noarch autoimports
#rpm [cronbuild] ftp://ftp.altlinux.ru/pub/distributions/ALTLinux/autoimports/%{destbranch}/ %{_arch} autoimports

#rpm [cronbuild] http://ftp.altlinux.ru/pub/distributions/ALTLinux/autoimports/%{destbranch}/ noarch autoimports
#rpm [cronbuild] http://ftp.altlinux.ru/pub/distributions/ALTLinux/autoimports/%{destbranch}/ %{_arch} autoimports

rpm [cronbuild] rsync://ftp.altlinux.ru/ALTLinux/autoimports/%{destbranch}/ noarch autoimports
rpm [cronbuild] rsync://ftp.altlinux.ru/ALTLinux/autoimports/%{destbranch}/ %{_arch} autoimports
EOF

mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
# Double the main part of the number from apt-0.5.15lorg2-alt50.x86_64.rpm
# -- <http://git.altlinux.org/gears/a/apt.git?p=apt.git;a=commitdiff;h=abf6d39f75266c153fbfcb2c0f38131f05b67bd4>.
echo "APT::Cache-Limit $(( (2*64 + 32) * 1024 * 1024 ));" > %buildroot%_sysconfdir/apt/apt.conf.d/50-autoimports-cache-limit.conf

%files
%config %_sysconfdir/apt/vendors.list.d/autoimports-%{destbranch}.list
%config %_sysconfdir/apt/sources.list.d/autoimports-%{destbranch}.list
%config %_sysconfdir/apt/apt.conf.d/50-autoimports-cache-limit.conf

%changelog
* Thu May 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- autoimports/p9

* Thu May 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt6
- added conflicts for p9

* Fri Sep 16 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt5
- Requires: apt-rsync, because rsync has been made the default protocol

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4
- rsync is made default protocol

* Fri Oct 30 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3
- Currently, Sisyphus+Autoimports need a bigger APT cache limit (ALT#31411).

* Sat Oct 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2
- use official mirror on ftp.altlinux.ru

* Sat Oct 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- first build
