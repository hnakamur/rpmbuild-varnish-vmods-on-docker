%global libvmod_cookie_git_version 4.1

Name:              libvmod-header
Version:           20150915
Release:           1%{?dist}
Summary:           Varnish Header manipulation VMOD
License:           FreeBSD
URL:               https://www.varnish-cache.org/vmod/header-manipulation
BuildRequires:     varnish-libs-devel
BuildRequires:     git
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     libtool
BuildRequires:     python-docutils

%description
Varnish Module (vmod) for manipulation of duplicated headers (for instance multiple set-cookie headers).

Developed by Varnish Software. Sponsored by Softonic.com

%prep
rm -rf "%{buildroot}"
rm -rf "%{_builddir}/libvmod-header"
cd "%{_builddir}"
git clone https://github.com/varnish/libvmod-header
cd libvmod-header
git checkout %{libvmod_cookie_git_version}

%build
cd "%{_builddir}/libvmod-header"
./autogen.sh
./configure --prefix=%{_prefix}
make

%install
cd "%{_builddir}/libvmod-header"
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/varnish/vmods/libvmod_header.a
rm %{buildroot}%{_libdir}/varnish/vmods/libvmod_header.la

%files
%doc %{_docdir}/libvmod-header/LICENSE
%doc %{_docdir}/libvmod-header/README.rst
%doc %{_mandir}/man3/vmod_header.3.gz
%{_libdir}/varnish/vmods/libvmod_header.so

%changelog
* Thu Oct 15 2015 Hiroaki Nakamura <hnakamur@gmail.com> - 20150915-1
- Initial package

