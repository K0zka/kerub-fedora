# kerub-fedora

[Kerub](https://github.com/K0zka/kerub) packaging for [fedora 22](http://fedoraproject.org)

## Notes

* By default jetty does not start on fedora at all, the system adminstrator have to enable httpd_execmem in selinux\
```
setsebool httpd_execmem 1
```


