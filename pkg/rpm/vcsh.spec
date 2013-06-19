Name:           vcsh
Version:        1.3
Release:        1%{?dist}
Summary:        Manage config files in homedirs via fake bare git repositories

Group:          Development/Tools
License:        GPLv2+
URL:            https://github.com/RichiH/vcsh
Source0:        https://github.com/RichiH/vcsh/archive/v%{version}-homebrew.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  git
Requires:       git

%description
vcsh allows you to have several git repositories, all maintaining their working
trees in $HOME without clobbering each other. That, in turn, means you can have
one repository per config set (zsh, vim, ssh, etc), picking and choosing which
configs you want to use on which machine.

%prep
%setup -q -n %{name}-%{version}-homebrew

%build
make 

%install
make DESTDIR=%buildroot install
install -D -m 0644 _vcsh %{buildroot}%{_datadir}/zsh/site-functions/_vcsh
mv %{buildroot}%{_datadir}/zsh/vendor-completions %{buildroot}%{_datadir}/zsh/site-functions

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/vcsh
%{_mandir}/man1/vcsh.1.gz
%{_docdir}/vcsh/README.md
%doc LICENSE CONTRIBUTORS changelog
%{_docdir}/vcsh/hooks
%{_datadir}/zsh

%changelog
* Fri Jun 7 2013 Corey Quinn <corey@sequestered.net> - 1.3-1
- Initial package

