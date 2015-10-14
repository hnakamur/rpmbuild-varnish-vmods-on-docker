%global libvmod_cookie_git_version 4.1

Name:              libvmod-cookie
Version:           20150915
Release:           1%{?dist}
Summary:           Varnish Cookie VMOD
License:           FreeBSD
URL:               https://www.varnish-cache.org/vmod/cookie
BuildRequires:     varnish-libs-devel
BuildRequires:     git
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     libtool
BuildRequires:     python-docutils

%description
Varnish VMOD for Cookie.

Functions to handle the content of the Cookie header without complex use of regular expressions.
Parses a cookie header into an internal data store, where per-cookie get/set/delete functions are available. A filter_except() method removes all but a set comma-separated list of cookies.

A convenience function for formatting the Set-Cookie Expires date field is also included. It might be needed to use libvmod-header if there might be multiple Set-Cookie response headers.

%prep
rm -rf "%{buildroot}"
rm -rf "%{_builddir}/libvmod-cookie"
cd "%{_builddir}"
git clone https://github.com/lkarsten/libvmod-cookie
cd libvmod-cookie
git checkout %{libvmod_cookie_git_version}

%build
cd "%{_builddir}/libvmod-cookie"
./autogen.sh
./configure --prefix=%{_prefix}
make

%install
cd "%{_builddir}/libvmod-cookie"
make install DESTDIR=%{buildroot}%{_prefix}

%files

%changelog
* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 1.2.6-1
- Initial package

