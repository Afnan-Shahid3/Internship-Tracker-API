from rest_framework import serializers

from .models import Company, Application, Interview, Contact

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'location', 'created_at']



class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['id', 'application', 'interview_date', 'round_name', 'feedback']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'company', 'name', 'role', 'email', 'linkedin']


class ApplicationSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only= True)
    interview = InterviewSerializer(many = True, read_only= True)
    contacts = serializers.SerializerMethodField()
    class Meta:
        model = Application
        fields = ['id', 'position', 'date_applied', 'status', 'notes','company', 'interview', 'contacts']

    def get_contacts(self, obj):
        return ContactSerializer(
            obj.company.contacts.all(),
            many=True
        ).data