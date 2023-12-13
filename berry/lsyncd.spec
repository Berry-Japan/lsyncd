Summary: Live syncing (mirroring) daemon
Name: lsyncd
Version: 1.0
Release: b1
License: GPL
Group: Applications/File
URL: http://www.pri.univie.ac.at/lsyncd/

Packager: Yuichiro Nakada <yui@po.yui.mine.nu>
Vendor: Berry Linux

Source: lsyncd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: rsync
BuildArchitectures: i586

%description
Lsyncd uses rsync to synchronize local directories with a remote machine
running rsyncd. Lsyncd watches multiple directories trees through inotify.

The first step after adding the watches is to, rsync all directories with
the remote host, and then sync single file buy collecting the inotify events.
So lsyncd is a light-weight live mirror solution that should be easy to
install and use while blending well with your system.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc AUTHORS ChangeLog COPYING INSTALL NEWS TODO
%{_bindir}/lsyncd

%changelog
* Sun Aug 10 2008 Yuichiro Nakada <berry@po.yui.mine.nu>
- Create for Berry Linux
