from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from blog import models
import graphene


class PostType(DjangoObjectType):
	class Meta:
		model = models.Post


class TagType(DjangoObjectType):
	class Meta:
		model = models.Tag


class CatType(DjangoObjectType):
	class Meta:
		model = models.Category


class Query(graphene.ObjectType):
	all_posts = graphene.List(PostType)
	post_by_slug = graphene.Field(PostType, slug=graphene.String())

	def resolve_post_by_slug(root, info, slug):
		return (
			models.Post.objects.prefetch_related("tags")
				.get(slug=slug)
		)


schema = graphene.Schema(query=Query)
