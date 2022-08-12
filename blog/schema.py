from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
# import graphene_django_optimizer as gql_optimizer

from blog import models
import graphene


class Posts(DjangoObjectType):
	class Meta:
		model = models.Post


class TagType(DjangoObjectType):
	class Meta:
		model = models.Tag

class PostTag(DjangoObjectType):
	class Meta:
		model = models.PostTag

class Category(DjangoObjectType):
	class Meta:
		model = models.Category

class PostCategory(DjangoObjectType):
	class Meta:
		model = models.PostCategory


class Query(graphene.ObjectType):
	all_posts = graphene.List(Posts)
	get_category = graphene.List(Category)
	get_postcategory = graphene.List(PostCategory)
	get_posttag = graphene.List(PostTag)

	def resolve_all_posts(root, info):
		return (
			models.Post.objects.all()
		)

	def resolve_get_postcategory(root, info):
		return (
			models.PostCategory.objects.prefetch_related("AsscPost").all()
			#prefetch_related("AsscCategory_id")
			#
			# .all()
		)


schema = graphene.Schema(query=Query)
