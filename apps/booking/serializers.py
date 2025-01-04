from rest_framework import serializers
from .models import Bookings, ClientFeedback, ServiceFeedback, Journals, KVYCodes, Diagnosis, JournalFiles
from apps.userprofile.models import UserProfile


class BookingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'user', 'image',]
        read_only_fields = ('created_at', 'updated_at')


class ClientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFeedback
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ServiceFeedbackSerializer(serializers.ModelSerializer):
    user_first_name= serializers.CharField(source='user.first_name',read_only=True)
    user_last_name= serializers.CharField(source='user.last_name',read_only=True)
    
    class Meta:
        model = ServiceFeedback
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'service': {'required': False}
        }

class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    user_type = serializers.CharField(source='user.user_type', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class BookingsSerializer(serializers.ModelSerializer):
    booking_feedback = ClientFeedbackSerializer(many=True, read_only=True)
    company_name = serializers.CharField(source='service.company.name', read_only=True)
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    service_timing = serializers.CharField(source='service.service_timing', read_only=True)
    company_image = serializers.SerializerMethodField()
    company_id= serializers.IntegerField(source='service.company.id',read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)



    class Meta:
        model = Bookings
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    def get_company_image(self, obj):
        try:
            return obj.service.company.company_images.first().image.url
        except:
            return None



    # def validate(self, attrs):
        
    #     if attrs['booking_date'] < datetime.date.today():
    #         raise serializers.ValidationError('Booking date cannot be in the past')
    #     if attrs['start_booking_slot'] >= attrs['end_booking_slot']:
    #         raise serializers.ValidationError('Start time must be before end time')
    #     if is_slot_available(attrs['service'], attrs['booking_date'], attrs['start_booking_slot'], attrs['end_booking_slot']):
    #         raise serializers.ValidationError('Slot is not available')
    #     return attrs


class KVYCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KVYCodes
        fields = ['id', 'code', 'description', 'is_active']

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['id', 'code', 'description', 'is_active']

class JournalFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalFiles
        fields = ['id', 'file', 'is_active']

class JournalSerializer(serializers.ModelSerializer):
    kvy_code = KVYCodeSerializer(many=True)
    diagnosis = DiagnosisSerializer(many=True)
    journal_files = JournalFilesSerializer(many=True)

    class Meta:
        model = Journals
        fields = [
            'id', 'date', 'booking', 'kvy_code', 'diagnosis', 'contact_name',
            'assessment', 'action', 'description', 'phone', 'user', 'owner', 'price','journal_files'
        ]

class JournalCreateUpdateSerializer(serializers.ModelSerializer):
    kvy_code = serializers.PrimaryKeyRelatedField(queryset=KVYCodes.objects.all(), many=True)
    diagnosis = serializers.PrimaryKeyRelatedField(queryset=Diagnosis.objects.all(), many=True)
    journal_files = JournalFilesSerializer(many=True)

    class Meta:
        model = Journals
        fields = [
            'date', 'booking', 'kvy_code', 'diagnosis', 'contact_name',
            'assessment', 'action', 'description', 'phone', 'user', 'owner', 'price','journal_files'
        ]

    def create(self, validated_data):
        kvy_code = validated_data.pop('kvy_code', [])
        diagnosis = validated_data.pop('diagnosis', [])
        journal_files = validated_data.pop('journal_files', [])
        journal = Journals.objects.create(**validated_data)
        journal.kvy_code.set(kvy_code)
        journal.diagnosis.set(diagnosis)
        if journal_files:
            journal_files = JournalFilesSerializer(data=journal_files, many=True)
            journal_files.is_valid(raise_exception=True)
            journal_files.save(journal=journal)
        return journal

    def update(self, instance, validated_data):
        kvy_code = validated_data.pop('kvy_code', [])
        diagnosis = validated_data.pop('diagnosis', [])
        journal_files = validated_data.pop('journal_files', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        journal_files = JournalFilesSerializer(instance.journal_files.all(), data=journal_files, many=True)
        journal_files.is_valid(raise_exception=True)
        journal_files.save(journal=instance)
        instance.kvy_code.set(kvy_code)
        instance.diagnosis.set(diagnosis)
        return instance