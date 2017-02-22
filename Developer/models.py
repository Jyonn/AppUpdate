from django.db import models
from django.utils.crypto import get_random_string


class Developer(models.Model):
    username = models.CharField(
        verbose_name="用户名",
        max_length=16,
        default=None,
    )
    password = models.CharField(
        verbose_name="加密密码",
        max_length=40,
        default=None,
    )
    salt = models.CharField(
        verbose_name="盐密",
        max_length=8,
        default=None,
    )
    isFrozen = models.BooleanField(
        verbose_name="是否被冻结",
        default=False,
    )
    lastLogin = models.DateTimeField(
        verbose_name="上次登录时间",
        default=None,
        null=True,
    )
    lastIpv4 = models.GenericIPAddressField(
        verbose_name="上次登录IP",
        default=None,
        null=True,
    )
    thisLogin = models.DateTimeField(
        verbose_name="本次登录时间",
        default=None,
        null=True,
    )
    thisIpv4 = models.GenericIPAddressField(
        verbose_name="本次登录IP",
        default=None,
        null=True,
    )

    @staticmethod
    def sha_text(salted_raw_password):
        import hashlib
        sha = hashlib.sha1()
        sha.update(salted_raw_password.encode())
        return sha.hexdigest()

    @classmethod
    def create(cls, username, raw_password):
        salt = get_random_string(length=8)
        password = Developer.sha_text(salt+raw_password)
        developer = cls(
            username=username,
            password=password,
            salt=salt,
            isFrozen=False,
        )
        developer.save()
        return developer
