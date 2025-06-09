from rest_framework import serializers
from ..models.veteran import (
    Veteran,
    MilitaryRank,
    BranchOfService,
    Conflict,
    Battle,
    Reward,
    VeteranReward
)


class MilitaryRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryRank
        fields = ['id', 'rank', 'order']
        read_only_fields = ['id', 'order']

    def to_representation(self, instance):
        """Возвращает читаемое название звания"""
        data = super().to_representation(instance)
        data['name'] = instance.get_rank_display()
        return data


class BranchOfServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOfService
        fields = ['id', 'branch']
        read_only_fields = ['id']

    def to_representation(self, instance):
        """Возвращает читаемое название рода войск"""
        data = super().to_representation(instance)
        data['name'] = instance.get_branch_display()
        return data


class ConflictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conflict
        fields = '__all__'


class BattleSerializer(serializers.ModelSerializer):
    conflict = ConflictSerializer(read_only=True)

    class Meta:
        model = Battle
        fields = '__all__'


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'


class VeteranRewardSerializer(serializers.ModelSerializer):
    reward = RewardSerializer(read_only=True)

    class Meta:
        model = VeteranReward
        fields = '__all__'


class VeteranSerializer(serializers.ModelSerializer):
    military_rank = MilitaryRankSerializer(read_only=True)
    branch_of_service = BranchOfServiceSerializer(read_only=True)
    conflict = ConflictSerializer(read_only=True)
    battles = BattleSerializer(many=True, read_only=True)
    rewards = VeteranRewardSerializer(
        source='veteranreward_set',
        many=True,
        read_only=True
    )
    photo_url = serializers.SerializerMethodField()
    veteran_type_display = serializers.CharField(
        source='get_veteran_type_display',
        read_only=True
    )

    class Meta:
        model = Veteran
        fields = [
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'full_name',
            'birth_date',
            'death_date',
            'biography',
            'photo',
            'photo_url',
            'veteran_type',
            'veteran_type_display',
            'military_rank',
            'branch_of_service',
            'conflict',
            'battles',
            'rewards',
            'call_place',
            'service_place',
            'military_unit',
            'is_approved',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'full_name',
            'photo_url'
        ]

    @staticmethod
    def get_photo_url(obj):
        """Возвращает URL фотографии или None"""
        if obj.photo and hasattr(obj.photo, 'url'):
            return obj.photo.url
        return None


class VeteranCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veteran
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'birth_date',
            'death_date',
            'biography',
            'photo',
            'veteran_type',
            'military_rank',
            'branch_of_service',
            'conflict',
            'call_place',
            'service_place',
            'military_unit'
        ]

    def validate(self, data):
        """Дополнительная валидация данных"""
        if data.get('death_date') and data.get('birth_date'):
            if data['death_date'] < data['birth_date']:
                raise serializers.ValidationError(
                    "Дата смерти не может быть раньше даты рождения"
                )
        return data