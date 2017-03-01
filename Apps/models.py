from django.db import models


class Apps(models.Model):
    C = {
        'appNameLength': 10,
        'appEnglishNameLength': 20,
        'logoLength': 30,
        'descriptionLength': 1000,
    }
    appName = models.CharField(
        verbose_name="应用名称",
        max_length=C['appNameLength'],
        default=None,
    )
    appEnglishName = models.CharField(
        verbose_name="应用英文名称",
        max_length=C['appEnglishNameLength'],
        default=None,
        unique=True,
    )
    createDatetime = models.DateTimeField(
        verbose_name="创建日期",
        auto_now_add=True,
    )
    isAlive = models.BooleanField(
        verbose_name="是否还在使用",
        default=False,
    )
    logo = models.CharField(
        verbose_name="LOGO地址",
        default=None,
        max_length=C['logoLength'],
        null=True,
        blank=True,
    )
    description = models.CharField(
        verbose_name="应用描述",
        default=None,
        max_length=C['descriptionLength'],
        null=True,
    )

    @classmethod
    def create(cls, appName, appEnglishName, description=None, logo=None):
        app = cls(
            appName=appName,
            appEnglishName=appEnglishName,
            logo=logo,
            isAlive=True,
            description=description)
        app.save()
        return app

    def get_logo_path(self):
        return self.appEnglishName+'_'+self.logo


class Level(models.Model):
    C = {
        'noteLength': 10
    }
    relatedApp = models.ForeignKey(
        Apps,
        verbose_name="关联应用",
        default=None,
        db_index=True,
    )
    level = models.SmallIntegerField(
        verbose_name="更新等级",
        help_text="更新越重要，level越小",
        default=0,
    )
    note = models.CharField(
        verbose_name="简短等级解释",
        max_length=C['noteLength'],
        default=None,
    )

    @classmethod
    def create(cls, relatedApp, level, note):
        o_level = cls(relatedApp=relatedApp, level=level, note=note)
        o_level.save()
        return o_level


class Version(models.Model):
    C = {
        'versionLength': 30,
        'urlLength': 200,
        'descriptionLength': 1000,
        'md5Length': 32,
        'sha1Length': 40
    }
    relatedApp = models.ForeignKey(
        Apps,
        verbose_name="关联应用",
        default=None,
        db_index=True,
    )
    relatedLevel = models.ForeignKey(
        Level,
        verbose_name="关联等级",
        default=None,
    )
    version = models.CharField(
        verbose_name="版本号",
        max_length=C['versionLength'],
        default=None,
    )
    updateDatetime = models.DateTimeField(
        verbose_name="更新日期",
        auto_now_add=True,
    )
    url = models.CharField(
        verbose_name="应用下载地址",
        max_length=C['urlLength'],
        default=None,
    )
    isAlive = models.BooleanField(
        verbose_name="是否还在使用",
        default=True,
    )
    isLevelLatest = models.BooleanField(
        verbose_name="是否当前等级最新版",
        default=True,
    )
    description = models.CharField(
        verbose_name="更新说明",
        default=None,
        max_length=C['descriptionLength'],
    )
    md5 = models.CharField(
        verbose_name="安装包MD5校验",
        default=None,
        max_length=C['md5Length'],
    )
    sha1 = models.CharField(
        verbose_name="安装包SHA1校验",
        default=None,
        max_length=C['sha1Length'],
    )

    @classmethod
    def create(cls, relatedApp, relatedLevel, version, url, md5, sha1, description=None):
        latest_versions = Version.objects.filter(
            relatedApp=relatedApp, relatedLevel=relatedLevel, isLevelLatest=True)
        for v in latest_versions:
            v.isLevelLatest = False
            v.save()
        o_version = cls(
            relatedApp=relatedApp,
            relatedLevel=relatedLevel,
            version=version,
            url=url,
            md5=md5,
            sha1=sha1,
            description=description,
            isAlive=True,
            isLevelLatest=True,
        )
        o_version.save()
        return o_version
