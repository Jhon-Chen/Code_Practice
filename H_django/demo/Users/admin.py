from django.contrib import admin
from Users.models import BookInfo, HeroInfo

# Register your models here.

# admin.site.register(BookInfo)
# admin.site.register(HeroInfo)
admin.site.site_title = 'my first Django project'
admin.site.site_header = 'Django_test_pro'
admin.site.index_title = 'Welcome'



class HeroInfoStackInline(admin.StackedInline):
    model = HeroInfo # 要编辑的对象
    extra = 1 # 附加编辑的数量

class HeroInfoTabularInline(admin.TabularInline):
    model = HeroInfo
    extra = 1


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'btitle', 'pub_date']
    # fields = ['btitle', 'bpub_data']
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_data']}),
        ('高级', {'fields': ['bread', 'bcomment', 'image'], 
                  'classes': ('collapse',)})  # 是否折叠显示
    )
    inlines = [HeroInfoStackInline]
    inlines = [HeroInfoTabularInline]


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_filter = ['hbook', 'hgender']
    search_fields = ['hname']

    list_display = ['id', 'hname', 'hbook', 'read']



















