from xml.etree.ElementTree import Comment
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag, Comment


admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)

# Category 모델의 name 필드에 값이 입력됐을 때 자동으로 slug가 만들어지는 클래스
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)