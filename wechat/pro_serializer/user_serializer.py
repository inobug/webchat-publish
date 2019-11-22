# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from rest_framework import serializers
from datetime import datetime, timedelta

from wechat.models import User


class CreateUsersRequestSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['user_name', 'password', 'pet_name', ]