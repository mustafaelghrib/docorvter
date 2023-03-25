from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import File


class FileSerializer(ModelSerializer):
    """Serializer for File model."""

    html_file = SerializerMethodField()
    pdf_file = SerializerMethodField()

    class Meta:
        """Metaclass for FileSerializer."""
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

    def get_html_file(self, file: File) -> str:
        """Get the URL for a File object's html_file field as a hyperlink.

        Args:
            file: A File object.

        Returns:
            The URL for the File object's html_file field as a hyperlink.
        """
        request = self.context.get('request')
        html_file = file.html_file.name.replace('backend/', '')
        return request.build_absolute_uri(html_file)

    def get_pdf_file(self, file: File) -> str:
        """Get the URL for a File object's pdf_file field as a hyperlink.

        Args:
            file: A File object.

        Returns:
            The URL for the File object's pdf_file field as a hyperlink.
        """
        request = self.context.get('request')
        pdf_file = file.pdf_file.name.replace('backend/', '')
        return request.build_absolute_uri(pdf_file)
