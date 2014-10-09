#!/usr/bin/env sh
# rsync backup script
# usage: ./rbackup.sh /media/backup

sudo sh -c "
    rsync -av --delete-excluded --exclude-from=backup.lst / $1;
        touch $1/BACKUP
	"
