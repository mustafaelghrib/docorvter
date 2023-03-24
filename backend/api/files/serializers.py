from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import File


class FileSerializer(ModelSerializer):

    html_file = SerializerMethodField()
    pdf_file = SerializerMethodField()

    class Meta:
        model = File
        fields = [
            "file_id",
            "html_file",
            "pdf_file",
            "uploaded_at",
            "converted_at",
            "created_at",
            "updated_at"
        ]

    def get_html_file(self, file):
        request = self.context.get('request')
        html_file = file.html_file.name.replace('backend/', '')
        return request.build_absolute_uri(html_file)

    def get_pdf_file(self, file):
        request = self.context.get('request')
        pdf_file = file.pdf_file.name.replace('backend/', '')
        return request.build_absolute_uri(pdf_file)
