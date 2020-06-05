from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status
from rest_framework.response import Response
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from core.query_core.queryUser import QueryUser
from .serializers import UserSerializer


class ExcelViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    """class create excel"""

    queryset = QueryUser.all_users()
    serializer_class = UserSerializer
    renderer_classes = (XLSXRenderer,)
    # filename = "pdf_user.xlsx"

    column_header = {
        "title": ["A", "B", "C",],
        "column_width": [17, 30, 17],
        "height": 50,
        "style": {
            "fill": {"fill_type": "solid", "start_color": "FFCCFFCC",},
            "alignment": {
                "horizontal": "center",
                "vertical": "center",
                "wrapText": True,
                "shrink_to_fit": True,
            },
            "border_side": {"border_style": "thin", "color": "00000000",},
            "font": {"name": "Roboto", "size": 17, "bold": 410, "color": "FF000000",},
        },
    }
    body = {
        "style": {
            "fill": {"fill_type": "solid", "start_color": "FFCCFFCC",},
            "alignment": {
                "horizontal": "center",
                "vertical": "center",
                "wrapText": True,
                "shrink_to_fit": True,
            },
            "border_side": {"border_style": "thin", "color": "FF000000",},
            "font": {"name": "Roboto", "size": 15, "bold": False, "color": "FF000000",},
        },
        "height": 40,
    }

    def get_header(self):
        """custom header"""
        startime, endtime = parse_times(request=self.request)
        datetime_format = "H%:M%:S% %d.%m.%Y"
        return {
            "tab_title": "my-report",
            "header_title": "Report from {} to {}".format(
                stattime.strftime(datetime_format), endtime.strftime(datetime_format),
            ),
            "height": 45,
            "img": "app/images/angel.png",
            "style": {
                "fill": {"fill_type": "solid", "start_color": "000000",},
                "aligment": {
                    "horizontal": "center",
                    "vertical": "center",
                    "wrapText": True,
                    "shrink_to_fit": True,
                },
                "border_side": {"border_style": "thin", "color": "000000",},
                "font": {
                    "name": "comicsans",
                    "size": 16,
                    "bold": True,
                    "color": "000000",
                },
            },
        }
