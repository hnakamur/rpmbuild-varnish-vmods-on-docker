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
    rpmbuild -bb /root/rpmbuild/SPECS/hiredis.spec && \
    redis-shutdown && \
    rpm -i /root/rpmbuild/RPMS/x86_64/hiredis-*.rpm && \
    rpmbuild -bb /root/rpmbuild/SPECS/libvmod-cookie.spec && \
    rpmbuild -bb /root/rpmbuild/SPECS/libvmod-header.spec && \
    rpmbuild -bb /root/rpmbuild/SPECS/libvmod-redis.spec

CMD ["/bin/bash"]
