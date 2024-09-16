Name: ansible-playbook-example
Version: 1.0
Release: 1%{?dist}
Summary: Ansible playbook to add text to a file
License: GPL
Source0: ansible-playbook-example.tar.gz
BuildArch: noarch

%description
This package contains an Ansible playbook that adds text to /tmp/ansible-test.txt.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/opt/ansible/playbooks
mkdir -p %{buildroot}/etc/systemd/system

# Copy playbook and systemd service file
cp site.yml %{buildroot}/opt/ansible/playbooks/
cp ansible-playbook-example.service %{buildroot}/etc/systemd/system/

%post
# Reload systemd and enable the service automatically
systemctl daemon-reload
systemctl enable ansible-playbook-example.service

%preun
# Stop the service on uninstall
if [ $1 -eq 0 ]; then
    systemctl stop ansible-playbook-example.service
    systemctl disable ansible-playbook-example.service
fi


%files
%dir /opt/ansible/playbooks
/opt/ansible/playbooks/site.yml
/etc/systemd/system/ansible-playbook-example.service

%changelog
