#!/bin/sh
# rsync backup script
# usage: ./rbackup.sh /media/backup

sudo sh -c "
    rsync -av --delete-excluded --exclude-from=etc.lst /etc $1;
        touch $1/BACKUP
	"