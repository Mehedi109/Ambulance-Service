from django.contrib import admin

from . models import Category
from . models import Quot
from . models import slider
from . models import service_category 

from . models import service_section

from . models import service_area
from . models import service_area_body

from . models import rent_details,article
#from . models import userComment
from . models import postComment
#from . models import reply
from . models import ability_top
from . models import ability_bottom
#from . models import area
from . models import border_top
from . models import border_bottom
from . models import emergency
from . models import general
from . models import freezer
from . models import ICU

#from .models import user

#from . models import details
#from . models import post_comment

admin.site.register(Category)
admin.site.register(Quot)
admin.site.register(service_category)

admin.site.register(service_section)

admin.site.register(service_area)
admin.site.register(service_area_body)

admin .site.register(rent_details)
#admin.site.register(userComment)
'''admin.site.register(user)
admin.site.register(details)
admin.site.register(post_comment)'''
'''class userCommentModel(admin.ModelAdmin):
	list_display=["__str__"]
	search_fields=["__str__"]
	class meta:
		 Model=userComment

admin.site.register(userComment,userCommentModel)'''

admin.site.register(ability_top)
admin.site.register(ability_bottom)
#admin.site.register(area)
admin.site.register(border_top)
admin.site.register(border_bottom)
admin.site.register(slider)
admin.site.register(emergency)
admin.site.register(general)
admin.site.register(freezer)
admin.site.register(ICU)
admin.site.register(article)
admin.site.register(postComment)
