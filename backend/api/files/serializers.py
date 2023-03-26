"""
A module that contains serializers of the files package.

Classes:
    - `FileSerializer`: A class that serializer the File model.
"""

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import File


class FileSerializer(ModelSerializer):
    """Serializer for the File model.

    Attributes:
        html_file: The html file path
        pdf_file: The pdf file path

    Methods:
        - `get_html_file(file)`: A method to get the html file url
        - `get_pdf_file(file)`: A method to get the pdf file url
    """

    html_file: SerializerMethodField = SerializerMethodField()
    pdf_file: SerializerMethodField = SerializerMethodField()

    class Meta:
        """Metaclass for FileSerializer.

        Attributes:
            model: The File model
            fields: A list of File fields that need to be serialized
        """

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
