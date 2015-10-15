Name:           hiredis
Version:        0.13.3
Release:        1%{?dist}
Summary:        Minimalistic C client library for Redis
License:        BSD
URL:            https://github.com/redis/hiredis
Source0:        https://github.com/redis/hiredis/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description 
Hiredis is a minimalistic C client library for the Redis database.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX="%{_prefix}" INSTALL_LIBRARY_PATH="%{_libdir}"     \
            OPTIMIZATION="%{optflags}" LDFLAGS="%{?__global_ldflags}"

%install
make install DESTDIR=%{buildroot} PREFIX="%{_prefix}" INSTALL_LIBRARY_PATH="%{buildroot}%{_libdir}"
ln -s libhiredis.so.0.13 "%{buildroot}%{_libdir}/libhiredis.so.0"

# Generate pkgconfig file manually. It's already mentioned in the upstream 
# makefile but make install doesn't do and modification needed for %%_libdir.

#mkdir -p %{buildroot}%{_libdir}/pkgconfig/
#cat >%{buildroot}%{_libdir}/pkgconfig/%{name}.pc<<EOF
#%{name} pkg-config source file
#
#prefix=%{_prefix}
#exec_prefix=%{_prefix}
#libdir=%{_libdir}
#includedir=%{_includedir}
#
#Name: %{name}
#Description: Minimalistic C client library for the Redis database
#Version: %{version}
#Libs: -L\${libdir} -lhiredis
#Cflags: -I\${includedir} -D_FILE_OFFSET_BITS=64
#EOF

find %{buildroot} -name '*.a' -delete -print

%check
# Firewall + Koji isolated environment will cause some tests fail to pass
make test || true

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/libhiredis.so.0.13
%{_libdir}/libhiredis.so.0

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/%{name}/
%{_libdir}/libhiredis.so
%{_libdir}/pkgconfig/hiredis.pc

%changelog
* Thu Oct 15 2015 Hiroaki Nakamura <hnakamur@gmail.com> - 0.13.3-1
- Update to 0.13.3

* Fri Jan 30 2015 Christopher Meng <rpm@cicku.me> - 0.12.1-1
- Update to 0.12.1

* Fri Jan 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.0-4
- Again build for f22-boost

* Fri Jan 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.0-3
- Once build on f22

* Tue Jan 27 2015 David Tardon <dtardon@redhat.com> - 0.12.0-2
- install all headers

* Fri Jan 23 2015 Christopher Meng <rpm@cicku.me> - 0.12.0-1
- Update to 0.12.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 29 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.11.0-1
- Updated to 0.11.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.1-3
- Removed Requires redis.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.1-1
- Updated to upstream 0.10.1-28-gd5d8843.

* Mon May 16 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.0-3
- Removed INSTALL_LIB from install target as we use INSTALL_LIBRARY_PATH.
- Use 'client library' in Summary.

* Wed May 11 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.0-2
- Updated devel sub-package description.
- Added optimization flags.
- Remove manual installation of shared objects.
- Use upstream .tar.gz sources.

* Tue May 10 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.10.0-1.gitdf203bc328
- Updated to upstream gitdf203bc328.
- Added TODO to the files.
- Updated to use libhiredis.so.0, libhiredis.so.0.10.

* Fri Apr 29 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> 0.9.2-1
- First release.
