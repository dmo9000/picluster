#!/bin/sh
systemctl status --no-pager {{ item }}.service 1>/dev/null 2>&1 
STATUS=$?

case $STATUS in 
    0)
    MAINPID=$( /bin/systemctl show -p MainPID {{ item }}.service | sed -e "s/^.*=//" )
    echo "{{ item }} service is running with pid ${MAINPID}"
    exit 0
    ;;
    3)
    echo "{{ item }} service is not running"
    exit 3
    ;;
    *)
    echo "{{ item }} service in unknown state"
    exit 3
    ;;
esac


# Not reached

exit 3
