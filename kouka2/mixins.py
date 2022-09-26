from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

# # from .models import Kouka2

# #「自身の日記しか見られない」という制限を表現するクラス
# #UserPassesTestMixin：ログイン済みのユーザーのアクセスを制限するクラス
# class OnlyYouMixin(UserPassesTestMixin):
#     #True：エラーページを表示する
#     #False：ログインページを表示する
#     raise_exception = True

#     def test_func(self):
#         # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
#         kouka2 = get_object_or_404(Kouka2, pk=self.kwargs['pk'])
#         # ログインユーザーと日記の作成ユーザーを比較し、異なればraise_exceptionの設定に従う
#         return self.request.user == kouka2.user