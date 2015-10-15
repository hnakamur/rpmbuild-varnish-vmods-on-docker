%global libvmod_cookie_git_version 4.1

Name:              libvmod-redis
Version:           20151008
Release:           1%{?dist}
Summary:           Varnish redis VMOD
License:           FreeBSD
URL:               https://www.varnish-cache.org/vmod/redis
BuildRequires:     varnish-libs-devel
BuildRequires:     hiredis-devel
BuildRequires:     git
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     libtool
BuildRequires:     python-docutils

%description
Working code that gives you the option to look up data in a Redis database from within VCL. 

Originally developed by ZephirWorks. Maintained by Brandon Wamboldt.

%prep
rm -rf "%{buildroot}"
rm -rf "%{_builddir}/libvmod-redis"
cd "%{_builddir}"
git clone https://github.com/carlosabalde/libvmod-redis
cd libvmod-redis
git checkout %{libvmod_cookie_git_version}

%build
cd "%{_builddir}/libvmod-redis"
./autogen.sh
./configure --prefix=%{_prefix}
make

%install
cd "%{_builddir}/libvmod-redis"
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/varnish/vmods/libvmod_redis.a
rm %{buildroot}%{_libdir}/varnish/vmods/libvmod_redis.la

%files
%doc %{_docdir}/libvmod-redis/LICENSE
%doc %{_docdir}/libvmod-redis/README.rst
%doc %{_mandir}/man3/vmod_redis.3.gz
%{_libdir}/varnish/vmods/libvmod_redis.so

%changelog
* Thu Oct 15 2015 Hiroaki Nakamura <hnakamur@gmail.com> - 20150915-1
- Initial package

