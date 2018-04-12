# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 19:15
from __future__ import unicode_literals

from itertools import chain
from django.db import migrations


def populate_id_verification(apps, schema_editor):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    IDVerification = apps.get_model('verify_student', 'IDVerification')
    SoftwareSecurePhotoVerification = apps.get_model('verify_student', 'SoftwareSecurePhotoVerification')
    SSOVerification = apps.get_model('verify_student', 'SSOVerification')

    software_secure_verifications = SoftwareSecurePhotoVerification.objects.all()
    sso_verifications = SSOVerification.objects.all()
    for verification in chain(software_secure_verifications, sso_verifications):
        content_type = ContentType.objects.get_for_model(verification)
        IDVerification.objects.create(
            status=verification.status,
            user=verification.user,
            name=verification.name,
            created_at=verification.created_at,
            updated_at=verification.updated_at,
            content_type=content_type,
            object_id=verification.id,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('verify_student', '0007_idverification'),
    ]

    operations = [
        migrations.RunPython(populate_id_verification, reverse_code=migrations.RunPython.noop),
    ]