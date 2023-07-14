#import graphene
import strawberry

@strawberry.type
class Book: 
    id: str
    title: str
    subtitle: str
    author: str
    category: str
    publisher: str
    publishedDate: str
    description: str
    image: str
    state: int



'''class Book: 
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
'''