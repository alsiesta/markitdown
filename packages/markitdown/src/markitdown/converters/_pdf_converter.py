import sys
import io

from typing import BinaryIO, Any


from .._base_converter import DocumentConverter, DocumentConverterResult
from .._stream_info import StreamInfo
from .._exceptions import (
    MissingDependencyException,
    MISSING_DEPENDENCY_MESSAGE
)


# Try loading optional (but in this case, required) dependencies
# Save reporting of any exceptions for later
_dependency_exc_info = None
try:
    import pdfminer
    import pdfminer.high_level
except ImportError:
    # Preserve the error and stack trace for later
    _dependency_exc_info = sys.exc_info()


ACCEPTED_MIME_TYPE_PREFIXES = [
    "application/pdf",
    "application/x-pdf",
]

ACCEPTED_FILE_EXTENSIONS = [".pdf"]


class PdfConverter(DocumentConverter):
    """
    Converts PDFs to Markdown. Most style information is ignored,
    so the results are essentially plain-text.
    """

    def accepts(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        **kwargs: Any,  # Options to pass to the converter
    ) -> bool:
        mimetype = (stream_info.mimetype or "").lower()
        extension = (stream_info.extension or "").lower()

        if extension in ACCEPTED_FILE_EXTENSIONS:
            return True

        for prefix in ACCEPTED_MIME_TYPE_PREFIXES:
            if mimetype.startswith(prefix):
                return True

        return False

    def convert(
        self,
        file_stream: BinaryIO,
        stream_info: StreamInfo,
        **kwargs: Any,  # Options to pass to the converter
    ) -> DocumentConverterResult:
        # Check the dependencies
        if _dependency_exc_info is not None:
            raise MissingDependencyException(
                MISSING_DEPENDENCY_MESSAGE.format(
                    converter=type(self).__name__,
                    extension=".pdf",
                    feature="pdf",
                )
            ) from _dependency_exc_info[
                1
            ].with_traceback(  # type: ignore[union-attr]
                _dependency_exc_info[2]
            )

        assert isinstance(file_stream, io.IOBase)  # for mypy
        
        # Try different encoding approaches with pdfminer
        codecs_to_try = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        
        for codec in codecs_to_try:
            try:
                file_stream.seek(0)  # Reset stream position
                extracted_text = pdfminer.high_level.extract_text(
                    file_stream,
                    codec=codec
                )
                
                # Check if extraction was successful (no replacement chars)
                if '�' not in extracted_text:
                    return DocumentConverterResult(markdown=extracted_text)
                    
            except (UnicodeDecodeError, Exception):
                continue
        
        # If all codecs fail, fall back to default extraction
        file_stream.seek(0)
        extracted_text = pdfminer.high_level.extract_text(file_stream)
        
        return DocumentConverterResult(markdown=extracted_text)
