from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from forms.forms import *

def index(request):
    return render(request, 'home/circle_hp.html')

def works(request):
    return render(request, 'home/circle_works.html')

def contact(request):
    return render(request, 'home/circle_contact.html')

def about_us(request):
    return render(request, 'home/circle_about_us.html')

def delete_previous_file(function):
    """不要となる古いファイルを削除する為のデコレータ実装.

    :param function: メイン関数
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        """Wrapper 関数.

        :param args: 任意の引数
        :param kwargs: 任意のキーワード引数
        :return: メイン関数実行結果
        """
        self = args[0]

        # 保存前のファイル名を取得
        result = Image.objects.filter(pk=self.pk)
        previous = result[0] if len(result) else None
        super(Image, self).save()

        # 関数実行
        result = function(*args, **kwargs)

        # 保存前のファイルがあったら削除
        if previous:
            os.remove(MEDIA_ROOT + '/' + previous.image.name)
        return result
    return wrapper

    class Image(models.Model):
    @delete_previous_file
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Image, self).save()

    @delete_previous_file
    def delete(self, using=None, keep_parents=False):
        super(Image, self).delete()

    image = models.ImageField('画像', upload_to=get_image_path)


def sample_view(request):
    form = SampleForm
    return render(request,
        project/sample.html,
        {"form" : form}
    )
