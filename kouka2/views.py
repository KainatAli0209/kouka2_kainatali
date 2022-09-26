import logging

from django.urls import reverse_lazy

from django.views import generic

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

# from .mixins import OnlyYouMixin

# 同じフォルダのforms.pyからInquiryFormクラスをインポート(InquiryForm, Kouka2CreateFormを＊と記入することもできる)
from .forms import InquiryForm

# from .models import Kouka2

logger = logging.getLogger(__name__)

# indexページを表示するための処理
# TemplateVuew:HTMLを表示するためのクラス


class IndexView(generic.TemplateView):
    # 表示したいHTMLを指定
    template_name = "index.html"

# inquiryページを表示するための処理
# FormView: フォームを使ったページを表示するためのクラス
# LoginRequiedMixin：ログインしていなければ見れないページ


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    # 表示したいフォーム
    form_class = InquiryForm
    # 送信が成功したときに移動するURL
    # reverse_lazy:URLの逆引きを行う関数
    # kouka2アプリのinquiryページのURLを取得
    success_url = reverse_lazy('kouka2:inquiry')

    # 送信が成功したときに行う処理
    # 引数fromに入力した内容が格納される
    def form_valid(self, form):
        # form(InquiryFormクラス)のsend_emailメソッドを実行
        form.send_email()

        # success_urlページで表示するメッセージ
        messages.success(self.request, 'メッセージを送信しました')

        # form.cleand_data['フィールド名']にはエラー処理が完了したデータ保存されている
        logger.info('Inquriry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)




