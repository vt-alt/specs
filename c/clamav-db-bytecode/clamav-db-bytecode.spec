%define dbname		bytecode
%define dir		var/lib/clamav-db
%define sys_clamav 	/var/lib/clamav
%define sys_db		/var/lib/clamav-db
%define checksum	262767a1be28a3e35a4bd2063b30a48e

Name:    clamav-db-%dbname
Version: 20190919
Release: alt1

Summary: Antivirus database for ClamAV (%dbname)
Summary(ru): Антивирусная база для ClamAV (%dbname)
License: distributable
Group:   File tools
Url:     http://www.clamav.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source: %dbname.cvd

Requires: clamav

%description
Database %dbname.cvd for ClamAV virus scanner.

%description -l ru_RU.UTF-8
База для антивирусного сканера ClamAV %dbname.cvd

%prep

%install
install -pD %SOURCE0 %buildroot/%dir/%dbname.cvd

%check
test "$(md5sum "%buildroot%sys_db/%dbname.cvd" | cut -f1 -d' ')" = "%checksum"

%post
for base in %dbname
do
    if test ! -e %sys_clamav/$base.cvd -o %sys_db/$base.cvd -nt %sys_clamav/$base.cvd 
    then
    	yes | cp -fp %sys_db/$base.cvd %sys_clamav/$base.cvd 2>/dev/null
	chmod 0664 %sys_clamav/$base.cvd 2>/dev/null
    fi
done

%files
%attr(664,mail,root) %config(noreplace) /%dir/%dbname.cvd

%changelog
* Fri Nov 08 2019 Andrey Cherepanov <cas@altlinux.org> 20190919-alt1
- Update database.

* Fri May 10 2019 Andrey Cherepanov <cas@altlinux.org> 20190102-alt1
- Update database.

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 20170928-alt1
- Update database

* Wed Apr 06 2016 Andrey Cherepanov <cas@altlinux.org> 20160317-alt1
- Update database
- Test checksum

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 20151102-alt1
- Update database

* Tue Jan 27 2015 Andrey Cherepanov <cas@altlinux.org> 20150105-alt1
- Update database

* Sun Nov 30 2014 Andrey Cherepanov <cas@altlinux.org> 20140625-alt1
- Split clamav-db into undepended packages

