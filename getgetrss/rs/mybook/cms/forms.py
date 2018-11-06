from django.forms import ModelForm
from cms.models import priRSS


class rssForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = priRSS
        fields = ('url', 'siteName', 'siteDetail', )
