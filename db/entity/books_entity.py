import graphene

class Book(graphene.ObjectType): 
    id: graphene.Int()
    title: graphene.String()
    subtitle: graphene.String()
    author: graphene.String()
    category: graphene.String()
    publisher: graphene.String()
    publishedDate: graphene.String()
    description: graphene.String()
    image: graphene.String()
    state: graphene.Int()

