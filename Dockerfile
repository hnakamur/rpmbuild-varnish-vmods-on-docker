FROM centos:7

RUN yum install -y epel-release yum-utils rpm-build rpmdevtools make gcc autoconf automake libtool python-docutils git && \
    yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
    yum install -y --enablerepo=remi redis && \
    yum install -y https://repo.varnish-cache.org/redhat/varnish-4.1.el7.rpm && \
    yum install -y varnish varnish-libs-devel varnish-debug-info
    rpmdev-setuptree && \
