# kerub-fedora

[Kerub](https://github.com/K0zka/kerub) packaging for [fedora 22](http://fedoraproject.org)

## Notes

* By default jetty does not start on fedora at all, the system adminstrator have to enable httpd_execmem in selinux\
```
setsebool -P httpd_execmem 1
```
* Kerub module needs to be enabled in jetty
```
echo --module=kerub >> /usr/share/jetty/start.ini
```

* Optionally, set jetty autostart
```
sysctl enable jetty
```

