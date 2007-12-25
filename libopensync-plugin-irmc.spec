%define name	libopensync-plugin-irmc
%define version	0.35
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	IRMC plugin for opensync synchronization tool
License:	GPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	openobex-devel
BuildRequires:	cmake
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
Sony Ericsson phones.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
export FFLAGS="%{optflags} -fPIC"
%cmake
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/opensync-1.0/plugins/*
%{_datadir}/opensync-1.0/defaults/*
