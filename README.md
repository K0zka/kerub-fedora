# kerub-fedora

[Kerub](https://github.com/K0zka/kerub) packaging for [fedora 23](http://fedoraproject.org)

## Notes

```
* Kerub module needs to be enabled in jetty
```
echo --module=kerub >> /usr/share/jetty/start.ini
```

* Set jetty autostart
```
sysctl enable jetty
```

