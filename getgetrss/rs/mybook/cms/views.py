from django.shortcuts import render
from django.http import HttpResponse
from cms.forms import rssForm
from cms.models import priRSS
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect


def rss_list(request):
    """書籍の一覧"""
#    return HttpResponse('取得URL一覧')
    rss=priRSS.objects.all().order_by('id')
    return render(request,
              'cms/rss_list.html',     # 使用するテンプレート
              {'rss': rss})         # テンプレートに渡すデータ


def rss_edit(request, url_id=None):
    """RSS編集"""
    if url_id:   # book_id が指定されている (修正時)
        url = get_object_or_404(priRSS, pk=url_id)
    else:         # book_id が指定されていない (追加時)
        url = priRSS()

    if request.method == 'POST':
        form = rssForm(request.POST, instance=url)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            url = form.save(commit=False)
            url.save()
            return HttpResponseRedirect('/cms/url/')
    else:    # GET の時
        form = rssForm(instance=url)  # book インスタンスからフォームを作成

    return render(request, 'cms/rss_edit.html', dict(form=form, url_id=url_id))


def rss_del(request, url_id):
    """RSS削除"""
    url = get_object_or_404(priRSS, pk=url_id)
    url.delete()
    return HttpResponseRedirect('/cms/url/')
