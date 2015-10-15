FROM centos:7

RUN yum install -y epel-release yum-utils rpm-build rpmdevtools make gcc autoconf automake libtool python-docutils git curl && \
    yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
    yum install -y --enablerepo=remi redis && \
    yum install -y https://repo.varnish-cache.org/redhat/varnish-4.1.el7.rpm && \
    yum install -y varnish varnish-libs-devel varnish-debug-info && \
    rpmdev-setuptree && \
    curl -s -L -o /root/rpmbuild/SOURCES/hiredis-0.13.3.tar.gz https://github.com/redis/hiredis/archive/v0.13.3.tar.gz

ADD specs/ /root/rpmbuild/SPECS/

RUN redis-server & \
    rpmbuild -ba /root/rpmbuild/SPECS/hiredis.spec && \
    redis-shutdown && \
    rpm -i /root/rpmbuild/RPMS/x86_64/hiredis-*.rpm && \
    rpmbuild -ba /root/rpmbuild/SPECS/libvmod-cookie.spec && \
    rpmbuild -ba /root/rpmbuild/SPECS/libvmod-header.spec && \
    rpmbuild -ba /root/rpmbuild/SPECS/libvmod-redis.spec

RUN yum install -y createrepo && \
    mkdir -p /usr/share/nginx/html/repo/vmods/RPMS && \
    cp /root/rpmbuild/RPMS/x86_64/*.rpm /usr/share/nginx/html/repo/vmods/RPMS/ && \
    createrepo /usr/share/nginx/html/repo/vmods/RPMS/ && \
    mkdir -p /usr/share/nginx/html/repo/vmods/SRPMS && \
    cp /root/rpmbuild/SRPMS/*.rpm /usr/share/nginx/html/repo/vmods/SRPMS/ && \
    createrepo /usr/share/nginx/html/repo/vmods/SRPMS/

RUN yum remove -y varnish-release varnish varnish-libs varnish-libs-devel \
        hiredis hiredis-devel hiredis-debuginfo \
        autoconf automake libtool python-docutils \
        remi-release redis \
        make gcc git \
        epel-release rpm-build rpmdevtools && \
    yum clean all && \
    rm -rf /root/rpmbuild /root/.rpmmacros

ADD nginx.repo /etc/yum.repos.d/
RUN yum update -y && \
    yum install -y nginx && \
    yum clean all

EXPOSE 80
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
